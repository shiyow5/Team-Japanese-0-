import File
def frequency(text:str = 'text', top_n:int = 0)->list:
    text = File.format(text)
    dict = {}

    for s in text:
        if s in dict:
            dict[s] += 1
        else:
            dict.setdefault(s, 1)

    list = sorted(dict.items(), key = lambda x : x[1], reverse=True)
    list = [i for i, j in list]

    return list[:top_n]

if __name__ == "__main__":
    text = "I'm a perfect human.\ntanaka tanaka tanaka!"
    print(f"\n{text}\n")

    word_list = frequency(text, 3)
    print(word_list)
    word_list = frequency(text, 20)
    print(word_list)