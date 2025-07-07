from paper_trail.metadata_store import init_db, add_metadata, get_metadata_by_ids
import os

def test_metadata_operations():
    init_db()
    add_metadata(1, "test_file.txt", "This is a snippet for testing.")
    results = get_metadata_by_ids([1])

    assert len(results) == 1
    vid, path, snippet = results[0]
    assert vid == 1
    assert path == "test_file.txt"
    assert "snippet" in snippet

    # Cleanup
    if os.path.exists("data/metadata.db"):
        os.remove("data/metadata.db")