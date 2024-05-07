import sqlite3

def create_file(conn:sqlite3.Connection=None, file_path:str='./')->bool:
    cur = conn.cursor()
    
    cur.execute(
        "SELECT * FROM sqlite_master WHERE type='table'"
    )
    
    if (not(cur.fetchall())):
        cur.execute(
            "CREATE TABLE files (Original_Name text, New_Name text, Sentence text)"
        )
    
    cur.execute(
        "INSERT INTO files VALUES (?, ?, ?)", ['test', 'test', 'test']
    )
    
    conn.commit()
    cur.close()
    return

def main():
    database_path = __file__.replace('code/ex01.py', '') + 'dataset/text_datas.db'
    conn = sqlite3.connect(database_path)
    create_file(conn)
    
    conn.close()
    return

if (__name__ == "__main__"):
    main()