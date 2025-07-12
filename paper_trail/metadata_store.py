import sqlite3

DB_PATH = "data/metadata.db"

def init_db() -> None:
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS metadata (
            vector_id INTEGER PRIMARY KEY,
            file_path TEXT,
            snippet TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_metadata(vector_id: int, file_path: str, snippet: str) -> None:
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('INSERT INTO metadata (vector_id, file_path, snippet) VALUES (?, ?, ?)',
              (vector_id, file_path, snippet))
    conn.commit()
    conn.close()

def get_metadata_by_ids(ids: list[int]) -> list[tuple[int, str, str]]:
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    placeholders = ','.join('?' for _ in ids)
    c.execute(f'SELECT vector_id, file_path, snippet FROM metadata WHERE vector_id IN ({placeholders})', ids)
    results = c.fetchall()
    conn.close()
    return results