import faiss
import numpy as np
import os
from logging import getLogger
logger = getLogger(__name__)

INDEX_PATH = "data/faiss.index"

def create_or_load_index(dimension):
    if os.path.exists(INDEX_PATH):
        index = faiss.read_index(INDEX_PATH)
    else:
        index = faiss.IndexFlatL2(dimension)
    return index

def add_embeddings(index, embeddings):
    index.add(np.array(embeddings).astype('float32'))
    faiss.write_index(index, INDEX_PATH)

def search(index, query_embedding, k=5): # k is the number of nearest neighbors to return
    D, I = index.search(np.array([query_embedding]).astype('float32'), k)
    logger.info(f"Query distances: {D[0]}")
    return I[0]