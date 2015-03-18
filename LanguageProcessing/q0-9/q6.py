#文字x-gramを得る関数。第一引数に文、第二引数にxを代入し、リスト型で戻す。
def x_gram(seq,num):
    list = []
    for i in range(len(seq)-num+1):
        list.append(seq[i:i+num])
    return list
#２つの文をインプット
input1 = "paraparaparadise"
input2 = "paragraph"

#リスト型をset()により集合型に変更
x = set(x_gram(input1,2))
y = set(x_gram(input2,2))

#和集合
print("和集合",x | y)

#積集合
print("積集合",x & y)

#差集合
print("差集合",x - y)

#要素の検索：x
if "se" in x :
    print("xにseは含まれます。")
else:
    print("xにseは含まれません。")

#要素の検索：y
if "se" in y :
    print("yにseは含まれます。")
else:
    print("yにseは含まれません。")
