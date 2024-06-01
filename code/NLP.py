import File

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
        
        if (type == 'word-token'): # 単語ヒットのみ(連語は含まない)
            indexs = [i for i in range(len(sentence)) if sentence[i]==word]
        else:
            indexs = []
        
        for index in indexs:
            result.append(left_right_n_word(sentence, index, extraction_range))
            
    #File.add_history(word=word)

    return result


def main():
    #search_word()テスト用
    print(search_word('given', ['K1']))
    
    return


if (__name__ == "__main__"):
    main()