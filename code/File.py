import sqlite3
#Shift_JIS(ANSI) 

database_path = __file__.replace('code/File.py', 'DataBase/text_datas.db')

def create_file(file_name:str='', new_name:str='')->None:
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()
    
    cur.execute(
        "SELECT * FROM sqlite_master WHERE type='table'"
    )
    
    if (not(cur.fetchall())):
        cur.execute(
            "CREATE TABLE files (Original_Name text, New_Name text, Sentence text)"
        )
        
    try:
        file_path = __file__.replace('code/File.py', 'AA_dataset/'+file_name+'.txt')
        with open(file_path, mode='r', encoding='Shift_JIS') as file:
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
    conn.close()
    return


def retrieve_file(file_name:str='')->dict:
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()

    cur.execute("SELECT * FROM files WHERE (Original_Name = ?) OR (New_Name = ?)", [file_name, file_name])
    
    file_data = cur.fetchall()
    cur.close()
    conn.close()
    
    if file_data:
        return file_data
    else:
        print(f"ファイル '{file_name}' が見つかりませんでした。")
        return None


def update_file(file_name:str='', new_name:str='')->None:
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()
    cur.execute(
      "UPDATE files SET New_Name = ? WHERE (Original_Name = ?) OR (New_Name = ?)", [new_name, file_name, file_name]
    )
    conn.commit()
    cur.close()
    conn.close()
    return
  
  
def delete_file(file_name:str='')->None:
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM files WHERE (Original_Name = ?) OR (New_Name = ?)", [file_name, file_name]
    )
    conn.commit()
    cur.close()
    conn.close()
    return


def database_init():
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()
    cur.execute(
            "DELETE FROM files"
        )
    conn.commit()
    cur.close()
    conn.close()
    return
  
    
def get_sentence(file_name:str='')->str:
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()
    cur.execute(
        "SELECT Sentence FROM files WHERE (Original_Name = ?) OR (New_Name = ?)", [file_name, file_name]
    )
    sentence = cur.fetchone()
    cur.close()
    conn.close()
    
    return sentence


def main():
    #create_file()テスト用
    #create_file('AnwarKhoirul_20', 'K1')
    #create_file('WirelessComm_unknown', 'Q1')
    #update_file()テスト用
    #update_file('K1', 'Q1')
    #delete_file()テスト用
    #delete_file('Q1')

    return

if (__name__ == "__main__"):
    main()
