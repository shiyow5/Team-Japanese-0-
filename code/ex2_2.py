import File
def aaa(Ktextlist):
    wordlist=[]
    item=[]
    listnom=0
    for i in Ktextlist:
        a = File.format(i).split()
        for j in a:
            x=0
            for k in range(listnom):
                if wordlist[k] == j and k<pre:
                    item[k]+=1
                    x=1
            if x == 0:
                wordlist.append(j)
                item.append(1)
                listnom+=1
        pre=listnom
    print("all")
    for i in range(listnom):
        if item[i] == len(Ktextlist):
            print(wordlist[i])
            
    print("all-1")
    for i in range(listnom):
        if item[i] == len(Ktextlist)-1:
            print(wordlist[i])
            
    print("all-2")
    for i in range(listnom):
        if item[i] == len(Ktextlist)-2:
            print(wordlist[i])
    
    return

text1 = 'bb cc dd ee ff gg'
text2 = 'bb qq ww rr dd gg'
text3 = 'rr bb ff gg'

print(aaa([text1, text2, text3]))