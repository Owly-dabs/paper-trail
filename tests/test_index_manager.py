from paper_trail.index_manager import create_or_load_index, add_embeddings, search
import numpy as np
import os
import numbers

def test_faiss_index_operations():
    if not os.path.exists("data"):
        os.makedirs("data")

    dimension = 384
    index = create_or_load_index(dimension)

    # Create dummy embeddings
    embeddings = np.random.rand(5, dimension).astype('float32')
    add_embeddings(index, embeddings)

    # Search with a random vector
    query_vector = np.random.rand(dimension).astype('float32')
    indices = search(index, query_vector, k=3)

    assert len(indices) == 3
    assert all(isinstance(i, numbers.Integral) for i in indices)

    # Cleanup
    if os.path.exists("data/faiss.index"):
        os.remove("data/faiss.index")