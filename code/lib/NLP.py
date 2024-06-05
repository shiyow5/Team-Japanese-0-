import pandas as pd
from . import File

def format(sentence:str="")->str:
    '''
    Format sentences to insert space between word tokens
    '''
    
    sentence = ' ' + sentence.strip() + ' '
    i = 0
    while True:
        if (i == len(sentence)):
            break
        
        if (sentence[i].isnumeric() or (sentence[i]=='.' and sentence[i-1].isnumeric() and sentence[i+1].isnumeric())): # 数字の処理
            if ((not sentence[i-1].isnumeric()) and sentence[i-1] != ' ' and sentence[i-1] != '.'):
                sentence = sentence[:i] + ' ' + sentence[i:]
            if ((not sentence[i+1].isnumeric()) and sentence[i+1] != ' ' and sentence[i+1] != '.'):
                sentence = sentence[:i+1] + ' ' + sentence[i+1:]
        
        elif ((not sentence[i].isalpha()) and (sentence[i] != ' ')): # アルファベット以外の処理(数字を除く)         
            if (sentence[i-1] == ' ' and sentence[i+1] != ' '):
                sentence = sentence[:i+1] + ' ' + sentence[i+1:]
            elif (sentence[i-1] != ' ' and sentence[i+1] == ' '):
                sentence = sentence[:i] + ' ' + sentence[i:]
            elif (sentence[i-1] != ' ' and sentence[i+1] != ' '):
                sentence = sentence[:i] + ' ' + sentence[i] + ' ' + sentence[i+1:]
            
        i += 1
            
    return sentence

def left_right_n_word(sentence:list=[], index:int=0, n:int=0)->tuple:
    '''
    Cut n-tokens from left and right
    '''
    
    left_n = ' '.join(sentence[index-n:index])
    right_n = ' '.join(sentence[index+1:index+n+1])
    
    return (left_n, right_n)

def search_word(word:str='', files:list=[], type:str='word-token')->list:
    '''
    Search for a word and get sentences around that word
    '''
    
    extraction_range = 10

    sentences = []
    for file in files:
        sentences.append(File.get_sentence(file))
    
    result = []
    
    for sentence in sentences:
        sentence = format(sentence).split()
        
        if (type == 'word-token'): # 単語ヒットのみ(連語は含まない)(大文字、小文字の区別なし)
            indexs = [i for i in range(len(sentence)) if sentence[i].lower()==word.lower()]
        else:
            indexs = []
        
        for index in indexs:
            result.append(left_right_n_word(sentence, index, extraction_range))
            
    File.add_history(word=word)

    return result

def frequency(text:str = 'text', top_n:int = 0, word_identify:bool = False):
    text = format(text).split()
    word_dict = {}

    for s in text:
        s = s.lower() # 大文字、小文字の区別なし
        if s in word_dict:
            word_dict[s] += 1
        else:
            word_dict.setdefault(s, 1)
            
    if (word_identify):
        return word_dict

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

def similary(Q_file:str='', K_files:list=[], Recursive_arg:int=20)->str:
    
    Q_text = File.get_sentence(Q_file)
    
    sim_list = []
    
    for K_file in K_files:
        K_text = File.get_sentence(K_file)
        
        score = compare(frequency(Q_text, Recursive_arg), frequency(K_text, Recursive_arg))
        sim_list.append((K_file, score))
        
    sim_list = sorted(sim_list, key = lambda x:x[1], reverse=True)
    print(f'top{Recursive_arg}:\n{sim_list}')
    
    next_K_files = []
    for sim_data in sim_list:
        if (sim_data == sim_list[0]):
            high_score = sim_data[1]
        if ((high_score - sim_data[1]) <= 0.051):#類似度の高い上位のファイル同士のスコアの差が5%以下なら残す
            next_K_files.append(sim_data[0])
            
    if (len(next_K_files) >= 2 and len(format(Q_text).split()) >= Recursive_arg):
        return similary(Q_file, next_K_files, Recursive_arg+20)
    
    highSim_K_file = sim_list[0]
    
    return highSim_K_file

def common_word(sentences:list=[], exclude:int=0):
    
    word_identify = {}
    
    for sentence in sentences:
        words = frequency(text=sentence, word_identify=True).keys()
        
        for word in words:
            if (word not in word_identify.keys()):
                word_identify[word] = 0
                
            word_identify[word] += 1
            
    result = [word for word in word_identify.keys() if word_identify[word]==(len(sentences)-exclude)]
    
    return result


def get_wordTable(exclude:int):
    files = File.get_fileName()
    sentences = files.copy()
    for i, file in enumerate(files):
        sentences[i] = File.get_sentence(file)
        
    words = common_word(sentences=sentences, exclude=exclude)
    
    df = pd.DataFrame(index=words, columns=files)
    df.fillna("´", inplace=True)
    
    for i, file in enumerate(files):
        sentence = format(sentences[i]).split()
        for word in words:
            if word in sentence:
                df[file][word] = word
            
    return df