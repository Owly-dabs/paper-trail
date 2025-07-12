import faiss
import numpy as np
import os
from logging import getLogger
logger = getLogger(__name__)

INDEX_PATH = "data/faiss.index"

def create_or_load_index(dimension: int) -> faiss.Index:
    if os.path.exists(INDEX_PATH):
        index = faiss.read_index(INDEX_PATH)
    else:
        index = faiss.IndexFlatL2(dimension)
    return index

def add_embeddings(index: faiss.Index, embeddings: list) -> None:
    index.add(np.array(embeddings).astype('float32'))
    faiss.write_index(index, INDEX_PATH)

def search(index: faiss.Index, query_embedding: list, k: int = 5) -> list:
    D, I = index.search(np.array([query_embedding]).astype('float32'), k)
    logger.info(f"Query distances: {D[0]}")
    return I[0]