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

def similary(Q_file, K_files):
    """40までしか拡張しないので後で修正"""
    
    Q_text = Q_file.read()
    Q_topwords = frequency(Q_text, 20)

    max_sim = 0
    best_match = ''
     
    similarities = []
    
    for K_file in K_files:
        K_text = K_file.read()
        K_topwords = frequency(K_text, 20)
        
        similarity = compare(Q_topwords, K_topwords)
        similarities.append((K_file, similarity))
        
        if similarity > max_sim:
            max_sim = similarity
            best_match = K_file

    for K_file, similarity in similarities:
        
        if K_file != best_match and abs(max_sim - similarity) <= 0.05:
            K_top_words = frequency(K_file.read(), 40)
            extended_sim = compare(Q_topwords, K_top_words)
            
            if extended_sim > max_sim:
                max_sim = extended_sim
                best_match = K_file

    return best_match

if __name__ == "__main__":
    
    Q_file = open(Q_file_path)
    K_files = open(K_file_path)
    
    highSim_K_file = similary(Q_file, K_files)
    print(f"The most similar file is: {highSim_K_file}")
    
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
