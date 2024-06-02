import pandas as pd
import File
import NLP

def common_word(sentences:list=[], exclude:int=0):
    
    word_identify = {}
    
    for i, sentence in enumerate(sentences):
        words = NLP.format(sentence).split()
        
        for word in words:
            if (word not in word_identify.keys()):
                word_identify[word] = 0
                
            if (word_identify[word] == i): # 同じファイル内の単語重複カウント禁止
                word_identify[word] += 1
            
    result = [word for word in word_identify.keys() if word_identify[word]>=(len(sentences)-exclude)]
    
    return result


def get_wordTable(exclude:int):
    files = File.get_fileName()
    sentences = files.copy()
    for i, file in enumerate(files):
        sentences[i] = File.get_sentence(file)
        
    words = common_word(sentences=sentences, exclude=len(files))
    
    df = pd.DataFrame(index=words, columns=files)
    df.fillna("´", inplace=True)
    
    for i, file in enumerate(files):
        sentence = NLP.format(sentences[i]).split()
        for word in words:
            if word in sentence:
                df[file][word] = word
            
    
    print(df)
    


if (__name__ == "__main__"):
    get_wordTable()
    """
    files = File.get_fileName()
    for i, file in enumerate(files):
        files[i] = File.get_sentence(file)
    
    print(common_word(files))
    """
    """
    text1 = 'bb cc dd ee ff gg'
    text2 = 'bb qq ww rr dd gg'
    text3 = 'rr bb ff gg rr'

    print(common_word([text1, text2, text3]))
    """