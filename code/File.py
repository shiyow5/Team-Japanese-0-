import datetime
import sqlite3
#Shift_JIS(ANSI) 

data_path = __file__.replace('code/File.py', 'DataBase/Authorship_Anarysis.db')

def create_file(file_name:str='', new_name:str='')->None:
    conn = sqlite3.connect(data_path)
    cur = conn.cursor()
    
    cur.execute(
        "SELECT name FROM sqlite_master WHERE type='table'"
    )
    
    if (tuple(['files']) not in cur.fetchall()):
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
    conn = sqlite3.connect(data_path)
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
    conn = sqlite3.connect(data_path)
    cur = conn.cursor()
    cur.execute(
      "UPDATE files SET New_Name = ? WHERE (Original_Name = ?) OR (New_Name = ?)", [new_name, file_name, file_name]
    )
    conn.commit()
    cur.close()
    conn.close()
    return
  
  
def delete_file(file_name:str='')->None:
    conn = sqlite3.connect(data_path)
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM files WHERE (Original_Name = ?) OR (New_Name = ?)", [file_name, file_name]
    )
    conn.commit()
    cur.close()
    conn.close()
    return


def database_init():
    conn = sqlite3.connect(data_path)
    cur = conn.cursor()
    cur.execute(
            "DELETE FROM files"
        )
    conn.commit()
    cur.close()
    conn.close()
    return
  
    
def get_sentence(file_name:str='')->str:
    conn = sqlite3.connect(data_path)
    cur = conn.cursor()
    cur.execute(
        "SELECT Sentence FROM files WHERE (Original_Name = ?) OR (New_Name = ?)", [file_name, file_name]
    )
    sentence = cur.fetchone()
    cur.close()
    conn.close()
    
    return sentence


def add_history(word:str)->None:
    conn = sqlite3.connect(data_path)
    cur = conn.cursor()
    
    cur.execute(
        "SELECT name FROM sqlite_master WHERE type='table'"
    )
    
    if (tuple(['history']) not in cur.fetchall()):
        cur.execute(
            "CREATE TABLE history (Number text, Date text, Time text, Word text)"
        )
    
    cur.execute(
        "SELECT COUNT(Number) FROM history"
    )
    
    dt_now = datetime.datetime.now()
    number = f"{int(cur.fetchone()[0])+1:03}"
    date = dt_now.strftime("%Y%m%d")
    time = dt_now.strftime("%H%M")
    
    cur.execute(
        "INSERT INTO history VALUES (?, ?, ?, ?)", [number, date, time, word]
    )
    
    conn.commit()
    cur.close()
    conn.close()
    return


def get_history():
    conn = sqlite3.connect(data_path)
    cur = conn.cursor()

    cur.execute("SELECT * FROM history")
    
    file_data = cur.fetchall()
    cur.close()
    conn.close()
    
    return file_data


def history_init():
    conn = sqlite3.connect(data_path)
    cur = conn.cursor()
    cur.execute(
            "DELETE FROM history"
        )
    conn.commit()
    cur.close()
    conn.close()
    return


def main():
    #create_file()テスト用
    #create_file('AnwarKhoirul_20', 'K1')
    #create_file('WirelessComm_unknown', 'Q1')
    #update_file()テスト用
    #update_file('K1', 'Q1')
    #delete_file()テスト用
    #delete_file('Q1')
    
    #add_history("test")
    print(get_history())

    return

if (__name__ == "__main__"):
    main()
