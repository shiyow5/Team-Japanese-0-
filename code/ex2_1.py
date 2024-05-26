import sqlite3
import File

def frequency(text:str = 'text', top_n:int = 0)->list:
    text = File.format(text).split()
    word_dict = {}

    for s in text:
        if s in word_dict:
            word_dict[s] += 1
        else:
            word_dict.setdefault(s, 1)

    word_list = sorted(word_dict.items(), key = lambda x : x[1], reverse=True)
    word_list = [i for i, j in word_list]

    return word_list[:top_n]

def compare(list1,list2):

    x=0

    for word in list1:
        if word in list2:
            x+=1
    
    y=x/len(list1)

    return y

def similary(conn:sqlite3.Connection=None, Q_file:str='', K_files:list=[], Recursive_arg:int=20)->str:
    
    cur = conn.cursor()
    
    cur.execute(
        "SELECT Sentence FROM files WHERE (Original_Name = ?) OR (New_Name = ?)", [Q_file, Q_file]
    )
    Q_text = cur.fetchone()[0]
    
    sim_list = []
    
    for K_file in K_files:
        cur.execute(
            "SELECT Sentence FROM files WHERE (Original_Name = ?) OR (New_Name = ?)", [K_file, K_file]
        )
        K_text = cur.fetchone()[0]
        
        score = compare(frequency(Q_text, Recursive_arg), frequency(K_text, Recursive_arg))
        sim_list.append((K_file, score))
        
    cur.close()
        
    sim_list = sorted(sim_list, key = lambda x:x[1], reverse=True)
    print(f'top{Recursive_arg}:\n{sim_list}')
    
    next_K_files = []
    for sim_data in sim_list:
        if (sim_data == sim_list[0]):
            high_score = sim_data[1]
        if ((high_score - sim_data[1]) <= 0.05):#類似度の高い上位のファイル同士のスコアの差が5%以下なら残す
            next_K_files.append(sim_data[0])
            
    if (len(next_K_files) >= 2 and len(File.format(Q_text).split()) >= Recursive_arg):
        return similary(conn, Q_file, next_K_files, Recursive_arg+20)
    
    highSim_K_file = sim_list[0]
    
    return highSim_K_file


if __name__ == "__main__":
    database_path = __file__.replace('code/ex2_1.py', 'DataBase/text_datas.db')
    conn = sqlite3.connect(database_path)
    
    K_files = ['AnwarKhoirul_20', 'AokiToshiaki_4', 'AsanoFumihiko_1', 'ChenJiageng_6', 'CheongKaiYuen_1', 'DangJiannwu_5', 'DefagoXavier_1', 'IkedaKokolo_2', 'InoguchiYasushi_1', 'MatsumotoTadashi_19']
    
    print('progress~')
    highSim_K_file = similary(conn, 'WirelessComm_unknown', K_files)
    print('~finish')
    print(f"The most similar file is: {highSim_K_file}")
    '''
    text1 = "I'm a 'perfect human'.\ntanaka tanaka tanaka!!"
    text2 = "tanaka is very pop human. But, he like kill."
    print(f"\n{text1}")
    print(f"{text2}\n")

    word_list1 = frequency(text1, 3)
    print(word_list1)
    word_list1 = frequency(text1, 20)
    print(word_list1)
    word_list2 = frequency(text2, 20)
    print(word_list2)
    print(compare(word_list1, word_list2))
    '''
