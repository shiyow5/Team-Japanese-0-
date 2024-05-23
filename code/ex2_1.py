import File
def frequency(text:str = 'text', top_n:int = 0)->list:
    text = File.format(text).split()
    dict = {}

    for s in text:
        if s in dict:
            dict[s] += 1
        else:
            dict.setdefault(s, 1)

    list = sorted(dict.items(), key = lambda x : x[1], reverse=True)
    list = [i for i, j in list]

    return list[:top_n]

def compare(list1,list2):

    x=0

    for word in list1:
        if word in list2:
            x+=1
    
    y=x/len(list1)

    return y

def readfile(file_path: str) -> str:
    with open(file_path, 'r') as file:
        return file.read()
        
def similary(Q_file, K_files):
    Q_text = read_file(Q_file)
    Q_top_words = frequency(Q_text, 20)

    max_similarity = 0
    best_match = ''
    
    similarities = []
    
    for K_file in K_files:
        K_text = read_file(K_file)
        K_top_words = frequency(K_text, 20)
        
        similarity = compare(Q_top_words, K_top_words)
        similarities.append((K_file, similarity))
        
        if similarity > max_similarity:
            max_similarity = similarity
            best_match = K_file

    for K_file, similarity in similarities:
        if K_file != best_match and abs(max_similarity - similarity) <= 0.05:
            
            K_top_words = frequency(read_file(K_file), 40)
            extended_similarity = compare(Q_top_words, K_top_words)
            
            if extended_similarity > max_similarity:
                max_similarity = extended_similarity
                best_match = K_file

    return best_match

if __name__ == "__main__":
    Q_file = 'path/to/Q_file.txt'
    K_files = ['path/to/K1_file.txt', 'path/to/K2_file.txt', 'path/to/K3_file.txt']

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
