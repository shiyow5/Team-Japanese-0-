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


def retrieve_file(conn:sqlite3.Connection=None, file_name:str='Q1')->dict:
    cur = conn.cursor()

    cur.execute("SELECT * FROM files WHERE (Original_Name = ?) OR (New_Name = ?)", [file_name, file_name])
    
    file_data = cur.fetchall()
    cur.close()
    
    if file_data:
        return file_data
    else:
        print(f"ファイル '{file_name}' が見つかりませんでした。")
        return None


def update_file(conn:sqlite3.Connection=None, file_name:str='text', new_name:str='Q1')->None:
    cur = conn.cursor()
    cur.execute(
      "UPDATE files SET New_Name = ? WHERE (Original_Name = ?) OR (New_Name = ?)", [new_name, file_name, file_name]
    )
    conn.commit()
    cur.close()
    return
  
def delete_file(conn:sqlite3.Connection=None, file_name:str='text')->None:
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM files WHERE (Original_Name = ?) OR (New_Name = ?)", [file_name, file_name]
    )
    conn.commit()
    cur.close()
    return

def format(sentence:str="")->str:
    '''
    Format sentences to insert space between word tokens
    '''
    
    sentence = ' ' + sentence.strip() + ' '
    i = 0
    while True:
        if (i == len(sentence)):
            break
        
        if ((not sentence[i].isalpha()) and (sentence[i] != ' ')):
            if (sentence[i-1] == ' ' and sentence[i+1] != ' '):
                sentence = sentence[:i+1] + ' ' + sentence[i+1:]
            elif (sentence[i-1] != ' ' and sentence[i+1] == ' '):
                sentence = sentence[:i] + ' ' + sentence[i:]
            elif (sentence[i-1] != ' ' and sentence[i+1] != ' '):
                sentence = sentence[:i] + ' ' + sentence[i] + ' ' + sentence[i+1:]
            
        i += 1
            
    return sentence

def left_right_n_word(sentence:str="", index:int=0, n:int=0)->tuple:
    left_n = ' '.join(sentence[index-n:index])
    right_n = ' '.join(sentence[index+1:index+n+1])
    
    return (left_n, right_n)

def search_word(conn:sqlite3.Connection=None, word:str='', files:list=[], type:str='word-token')->list:
    extraction_range = 5
    
    cur = conn.cursor()

    sentences = []
    for file in files:
        cur.execute(
            "SELECT Sentence FROM files WHERE (Original_Name = ?) OR (New_Name = ?)", [file, file]
        )
        
        sentences.append(cur.fetchone())
    
    result = []
    
    for sentence in sentences:
        sentence = format(sentence[0]).split()
        indexs = [i for i in range(len(sentence)) if sentence[i]==word]
        
        for index in indexs:
            result.append(left_right_n_word(sentence, index, extraction_range))
    
    cur.close()
    return result

def main():
    database_path = __file__.replace('code/File.py', 'dataset/text_datas.db')
    
    conn = sqlite3.connect(database_path)
    
    #create_file()テスト用
    #create_file(conn, 'Author_1', 'K1')
    #update_file()テスト用
    #update_file(conn, 'K1', 'Q1')
    #delete_file()テスト用
    #delete_file(conn, 'Q1')
    #search_word()テスト用
    #print(search_word(conn, ['K1'], 'give'))
    
    conn.close()
    return

if (__name__ == "__main__"):
    main()
