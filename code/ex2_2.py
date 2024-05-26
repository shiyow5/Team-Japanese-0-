import File
def aaa(Ktextlist):
    wordlist=[]
    item=[]
    listnom=0
    for i in Ktextlist:
        a = File.format(i).split()
        for j in a:
            for k in range(listnom):
                if wordlist[k] == a and k<pre:
                    item[k]+=1
            wordlist.append(j)
            item.append(1)
            listnom+=1
        pre=listnom
    for i in range(listnom):
        print("all")
        if item[i] == len(Ktextlist):
            print(wordlist[i])
    
    return

text1 = 'bb cc dd ee ff gg'
text2 = 'bb qq ww rr dd gg'
text3 = 'rr bb ff gg'

print(aaa([text1, text2, text3]))