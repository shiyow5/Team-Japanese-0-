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

if __name__ == "__main__":
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