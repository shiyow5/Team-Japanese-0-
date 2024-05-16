def compare(list1,list2):

    x=0

    for i in range(list1):
        for j in range(list2):
            if list1[i]==list2[j]:
                x+=1
    
    y=x/len(list1)

    return y
