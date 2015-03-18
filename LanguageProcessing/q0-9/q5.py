def x_gram(seq,num):
    list = []
    for i in range(len(seq)-num+1):
        list.append(seq[i:i+num])
    return list

print (x_gram("I am an NLPer",2))
