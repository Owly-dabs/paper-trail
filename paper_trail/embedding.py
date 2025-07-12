from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_text(texts: list[str]) -> np.ndarray:
    return model.encode(texts)