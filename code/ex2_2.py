import File

def common_word(sentences:list=[], exclude:int=0):
    
    word_identify = {}
    
    for sentence in sentences:
        words = File.format(sentence).split()
        
        for word in words:
            if (word not in word_identify.keys()):
                word_identify[word] = 0
                
            word_identify[word] += 1
            
    result = [word for word in word_identify.keys() if word_identify[word]>=(len(sentences)-exclude)]
    
    return result

text1 = 'bb cc dd ee ff gg'
text2 = 'bb qq ww rr dd gg'
text3 = 'rr bb ff gg'

print(common_word([text1, text2, text3]))