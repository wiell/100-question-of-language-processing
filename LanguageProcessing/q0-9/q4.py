input = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
input = input.replace(".","").replace(",","")
input = input.split()
dic = {}
for i in range(len(input)):
    tmp = ""
    if i == 0:
        tmp = input[i]
        tmp = tmp[:1]
    elif i == 4:
        tmp = input[i]
        tmp = tmp[:1]
    elif i == 5:
        tmp = input[i]
        tmp = tmp[:1]
    elif i == 6:
        tmp = input[i]
        tmp = tmp[:1]
    elif i == 7:
        tmp = input[i]
        tmp = tmp[:1]
    elif i == 8:
        tmp = input[i]
        tmp = tmp[:1]
    elif i == 14:
        tmp = input[i]
        tmp = tmp[:1]
    elif i == 15:
        tmp = input[i]
        tmp = tmp[:1]
    elif i == 18:
        tmp = input[i]
        tmp = tmp[:1]
    else:
        tmp = input[i]
        tmp = tmp[:2]

    dic.setdefault(tmp,i+1)

print(dic)
