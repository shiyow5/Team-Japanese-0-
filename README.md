# Team Japanese [0]  
※mainブランチでは作業しないようにしましょう  
タスクが完了したらプルリクエストをしてください。s1300221がレビューの後にマージします。  
## Level-1
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
```python
import os  
import sqlite3  
conn = sqlite3.connect('text_datas.db')  
```
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

## Level1-2
### ディレクトリ構造    
Team_Japanese_0  
　　　|  
　　　|---code  
　　　|　　　|--ex01.py  
　　　|　　　|--ex02.py  
　　　|  
　　　|---dataset  
　　　|　　　|--text_datas.db  
　　　|  
　　　|---input_files  
　　　　　　　|--Q1.txt, etc...  

### 前提  
### タスク割り当て  

## Level2-1
### ディレクトリ構造    
Team_Japanese_0  
　　　|  
　　　|---code  
　　　|　　　|--ex01.py  
　　　|　　　|--ex02.py  
　　　|　　　|--ex03.py  
　　　|  
　　　|---dataset  
　　　|　　　|--text_datas.db  
　　　|  
　　　|---input_files  
　　　　　　　|--Q1.txt, etc...  

### 前提  
```python
file = open(file_path)
text = read(file)
```
### タスク割り当て 
- text内の単語の出現頻度に対して上位n単語を返す。  
  frequency(text, top_n)  
  return word_list  
  
- 単語のリストword_list1とword_list2内の単語を比べword_list1に対するword_list2の類似率を返す。  
  compare(word_list1, word_list2)  
  return match_rate  
  担当：s1300023  
  
- ファイル名Q_fileとファイル名のリストK_filesを受け取り、Q_fileに対して一番類似率の高いK_fileを返す。また類似率の差が５％以下の別のK_fileが存在する場合、上位+20単語に拡張し、類似率を再計算する。  
  similary(Q_file, K_files)  
  return highSim_K_file  
  担当：s1280126  
