#2つのinputを1文字目から重ねていく
input1 = 'パトカー'
input2 = 'タクシー'
output = ''
for i in range(4):
    output = output + input1[i] + input2[i]
print(output)
