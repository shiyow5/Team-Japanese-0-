# Team Japanese [0]  
※mainブランチでは作業しないようにしましょう  
タスクが完了したらプルリクエストをしてください。s1300221がレビューの後にマージします。  
## Ex1
データベースはsqlite3を使用する  
database Name : text_datas.db  

### ディレクトリ構造    
Team_Japanese_0  
　　　|  
　　　|---code  
　　　|　　　|--ex01.py  
　　　|  
　　　|---dataset  
　　　|　　　|--text_datas.db  
　　　|  
　　　|---input_files  
　　　　　　　|--Q1.txt, etc...  
現在、datasetやinput_filesなどの具体的なデータが入るディレクトリには適当に作成されたテストファイルが一時的に格納されています  

### 前提  
  import os  
  import sqlite3  
  conn = sqlite3.connect('text_datas.db')  

### タスク割り当て  
- Create files (e.g. upload TXT file)  
  内容：txtファイルの内容をdatabaseに登録  
  担当：s1300221  
  def create_file(connectオブジェクト, file_name, new_name)  
  return None  
  進捗：マージ済み
  
- Retrieve files (e.g. search for uploaded file)  
  内容：database内のファイルを検索  
  担当：s1280126  
  def retrieve_file(connectオブジェクト, file_name)  
  return file_data or None  
  進捗：マージ済み
  
- Update files (e.g. rename file in experiment)  
  内容：database内の特定のファイル名を更新  
  担当：s1300023  
  def update_file(connectオブジェクト, file_name, new_name)  
  return None  
  進捗：マージ済み
  
- Delete files  
  内容：database内のファイルデータの削除  
  担当：s1300097  
  def delete_file(connectオブジェクト, file_name)  
  return None  
  進捗：マージ済み
