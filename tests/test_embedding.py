from embedding import embed_text

def test_embedding_shape():
    texts = ["This is a test sentence."]
    embeddings = embed_text(texts)
    assert embeddings.shape[0] == 1
    assert embeddings.shape[1] > 0