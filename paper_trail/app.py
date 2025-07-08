import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLineEdit, QTextEdit

from embedding import embed_text
from index_manager import create_or_load_index, add_embeddings, search
from metadata_store import init_db, add_metadata, get_metadata_by_ids

import os

from logging import getLogger
from utils.logger import setup_logging  # rename your logging.py to logging_setup.py if conflicts

setup_logging(log_file="faiss_search.log")

logger = getLogger(__name__)
logger.info("Application started.")

class SemanticSearchApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        init_db()
        self.index = create_or_load_index(384)  # MiniLM has 384-dim output

    def initUI(self):
        self.setWindowTitle("Local Semantic Search")
        layout = QVBoxLayout()

        self.upload_button = QPushButton("Upload Files")
        self.upload_button.clicked.connect(self.upload_files)
        layout.addWidget(self.upload_button)

        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Enter your query here...")
        layout.addWidget(self.search_bar)

        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.run_search)
        layout.addWidget(self.search_button)

        self.results_area = QTextEdit()
        self.results_area.setReadOnly(True)
        layout.addWidget(self.results_area)

        self.setLayout(layout)

    def upload_files(self):
        files, _ = QFileDialog.getOpenFileNames(self, "Select Text Files", "", "Text Files (*.txt)")
        for file_path in files:
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
            snippet = text[:500]  # store preview snippet
            embedding = embed_text([text])[0]
            add_embeddings(self.index, [embedding])
            vector_id = self.index.ntotal - 1
            file_name = os.path.basename(file_path)
            corpus_dir = "data/corpus"
            os.makedirs(corpus_dir, exist_ok=True)
            new_file_path = os.path.join(corpus_dir, file_name)
            if not os.path.exists(new_file_path):
                os.system(f'cp "{file_path}" "{new_file_path}"')
            add_metadata(vector_id, new_file_path, snippet)
        self.results_area.append("Files uploaded and indexed successfully.\n")

    def run_search(self):
        query = self.search_bar.text()
        if not query.strip():
            self.results_area.append("Please enter a search query.\n")
            return
        query_embedding = embed_text([query])[0]
        top_ids = search(self.index, query_embedding, k=5)
        id_list = [int(i) for i in top_ids]
        results = get_metadata_by_ids(id_list)

        # Reorder results to match FAISS order
        result_dict = {vid: (path, snippet) for vid, path, snippet in results}
        
        self.results_area.clear()
        for vid in id_list:
            if vid in result_dict:
                path, snippet = result_dict[vid]
                self.results_area.append(f"File: {path}\nPreview: {snippet[:200]}...\n---\n")
            else:
                self.results_area.append(f"(Missing metadata for vector_id {vid})\n---\n")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SemanticSearchApp()
    ex.resize(600, 400)
    ex.show()
    sys.exit(app.exec_())
