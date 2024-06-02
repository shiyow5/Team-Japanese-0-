from code.lib import NLP
from code.lib import File
import pandas as pd

def test_search_word():
    print(f"\ntest:search_word()\nfile='K1', word='given'")
    result = NLP.search_word(word='given', files=['K1'])
    print(result)
    
def test_frequency():
    print(f"\ntest:frequency()")
    text1 = "I'm a 'perfect human'.\ntanaka tanaka tanaka!!"
    text2 = "tanaka is very pop human. But, he is darty."
    print(f"text1:\n{text1}")
    print(f"text2:\n{text2}")

    word_list1 = NLP.frequency(text1, 3)
    print(f"text1, top3:\n{word_list1}")
    word_list1 = NLP.frequency(text1, 20)
    print(f"text1, top20:\n{word_list1}")
    word_list2 = NLP.frequency(text2, 20)
    print(f"text2, top20:\n{word_list2}")
    
    return [word_list1, word_list2]

def test_compare(word_list1, word_list2):
    print(f"\ntest:compare()")
    result = NLP.compare(word_list1, word_list2)
    print(result)
    
def test_similary():
    print(f"\ntest:similary()")
    K_files = ['AnwarKhoirul_20', 'AokiToshiaki_4', 'AsanoFumihiko_1', 'ChenJiageng_6', 'CheongKaiYuen_1', 'DangJiannwu_5', 'DefagoXavier_1', 'IkedaKokolo_2', 'InoguchiYasushi_1', 'MatsumotoTadashi_19']
    
    print('progress~')
    highSim_K_file = NLP.similary('WirelessComm_unknown', K_files)
    print('~finish')
    print(f"The most similar file is: {highSim_K_file}")
    
def test_common_word():
    print(f"\ntest:common_word()")
    text1 = 'bb cc dd ee ff gg'
    text2 = 'bb qq ww rr dd gg'
    text3 = 'rr bb ff gg rr'
    print(text1)
    print(text2)
    print(text3)

    result = NLP.common_word([text1, text2, text3])
    print(f"common words:\n{result}")
    
    print("for all files")
    files = File.get_fileName()
    for i, file in enumerate(files):
        files[i] = File.get_sentence(file)
    
    result = NLP.common_word(sentences=files,exclude=0)
    print(f"common words:\n{result}")
    
    print("for n-1 files")
    result = NLP.common_word(sentences=files,exclude=1)
    print(f"common words:\n{result}")
    
def test_get_wordTable():
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_colwidth', None)
    pd.set_option('expand_frame_repr', False)
    
    print(f"\ntest:get_wordTable()")
    result = NLP.get_wordTable(exclude=3)
    print(f"exclude3:\n{result}")
    
def main():
    test_search_word()
    list1 = test_frequency()
    test_compare(list1[0], list1[1])
    test_similary()
    test_common_word()
    test_get_wordTable()