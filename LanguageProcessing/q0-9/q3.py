def lowsplit(sen):
	sen = sen.lower().replace(","," ").replace("."," ")
	return sen.split()

input = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
tmp = lowsplit(input)
output = ''
for i in range(len(tmp)):
    print(len(tmp[i]))
