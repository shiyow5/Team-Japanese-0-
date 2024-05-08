import sqlite3

def create_file(conn:sqlite3.Connection=None, file_name:str='text', new_name:str='Q1')->None:
    cur = conn.cursor()
    
    cur.execute(
        "SELECT * FROM sqlite_master WHERE type='table'"
    )
    
    if (not(cur.fetchall())):
        cur.execute(
            "CREATE TABLE files (Original_Name text, New_Name text, Sentence text)"
        )
        
    try:
        file_path = __file__.replace('code/ex01.py', 'input_files/'+file_name+'.txt')
        with open(file_path, mode='r', encoding='UTF-8') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"ファイル '{file_path}' が見つかりませんでした。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")
    
    cur.execute(
        "INSERT INTO files VALUES (?, ?, ?)", [file_name, new_name, content]
    )
    
    conn.commit()
    cur.close()
    return



def main():
    database_path = __file__.replace('code/ex01.py', 'dataset/text_datas.db')
    
    conn = sqlite3.connect(database_path)
    
    #create_file()テスト用
    #create_file(conn, 'Author_1', 'K1')
    
    conn.close()
    return

if (__name__ == "__main__"):
    main()
