# Team Japanese [0]
## Ex1
データベースはsqlite3を使用する  
database Name : text_datas.db  

### ディレクトリ構造    
Team_Japanese_0  
      |  
      |---code  
      |     |--ex01.py  
      |  
      |---datase  
      |     |--text_datas.db  
      |  
      |---input_files  

### 前提  
  import os  
  import sqlite3  
  conn = sqlite3.connect('text_datas.db')  

### タスク割り当て  
- Create files (e.g. upload TXT file)  
  内容：txtファイルの内容をdatabaseに登録  
  担当：s1300221  
  def create_file(connectオブジェクト, file_name, new_name)  
  return True of False
  
- Retrieve files (e.g. search for uploaded file)  
  内容：database内のファイルを検索  
  担当：s1280126  
  def retrieve_file(connectオブジェクト, file_name)  
  return file_data or None  
  
- Update files (e.g. rename file in experiment)  
  内容：database内の特定のファイル名を更新  
  担当：s1300023  
  def update_file(connectオブジェクト, file_name, new_name)  
  return True or False  
  
- Delete files  
  内容：database内のファイルデータの削除  
  担当：s1300097  
  def delete_file(connectオブジェクト, file_name)  
  return True or False
