# 🧾 PaperTrail

**PaperTrail** is a cross-platform desktop application that helps you search through your local documents using **semantic search** — powered by embeddings and FAISS — rather than just keyword matching.

---

## 🔍 Features

* Upload and index your local `.txt` documents
* Perform semantic search using natural language queries
* Powered by [FAISS](https://github.com/facebookresearch/faiss) for fast vector similarity
* Uses local or API-based embedding models (e.g., HuggingFace or OpenAI)
* Intuitive PyQt5-based desktop interface
* Lightweight and fully offline-capable

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/paper-trail.git
cd paper-trail
```

### 2. Install dependencies using `uv`

```bash
pip install uv
uv venv .venv
source .venv/bin/activate
uv pip install -r pyproject.toml
```

### 3. Run the application

```bash
python paper_trail/app
```

---

## 🧪 Run Tests

```bash
PYTHONPATH=$(pwd) uv run pytest tests/
```

---

## 🛠 Tech Stack

* **PyQt5** – Cross-platform desktop GUI
* **FAISS** – Vector similarity search
* **sentence-transformers** – Text embedding (supports local or remote models)
* **SQLite** – Metadata storage
* **Ruff + Pytest** – Linting and testing
* **uv** – Fast package manager

---

## 📦 Planned Features

Feature roadmap is tracked under [GitHub Issues](https://github.com/Owly-dabs/paper-trail/issues).

---

## 🤝 Contributing

Want to help build a smarter document search experience?

We welcome contributions of all kinds:

* UI improvements
* Additional features (e.g. file format support, metadata filtering)
* Bug fixes and optimizations
* Writing or improving documentation

### 🛠 How to contribute

1. Fork the repository and create a new branch
2. Make your changes and add tests if applicable
3. Ensure all tests pass: `PYTHONPATH=$(pwd) uv run pytest tests/`
4. Open a pull request with a clear description of your changes

Please refer to open [Issues](https://github.com/your-username/paper-trail/issues) for ideas on what to work on.

---

## 📜 License

This project is currently not licensed. Please contact the maintainer for usage terms.
