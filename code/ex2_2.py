import File
import NLP

def common_word(sentences:list=[], exclude:int=0):
    
    word_identify = {}
    
    for sentence in sentences:
        words = NLP.format(sentence).split()
        
        for word in words:
            if (word not in word_identify.keys()):
                word_identify[word] = 0
                
            word_identify[word] += 1
            
    result = [word for word in word_identify.keys() if word_identify[word]>=(len(sentences)-exclude)]
    
    return result


if (__name__ == "__main__"):
    
    K_files = ['AnwarKhoirul_20', 'AokiToshiaki_4', 'AsanoFumihiko_1', 'ChenJiageng_6', 'CheongKaiYuen_1', 'DangJiannwu_5', 'DefagoXavier_1', 'IkedaKokolo_2', 'InoguchiYasushi_1', 'MatsumotoTadashi_19']
    for i, K_file in enumerate(K_files):
        K_files[i] = File.get_sentence(K_file)
    
    print(common_word(K_files))

    """
    text1 = 'bb cc dd ee ff gg'
    text2 = 'bb qq ww rr dd gg'
    text3 = 'rr bb ff gg'

    print(common_word([text1, text2, text3]))
    """