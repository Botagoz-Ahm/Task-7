inf = open('input.txt', 'r', encoding='utf8')
outputFile = open('output.txt', 'w', encoding='utf8')
text = inf.read().splitlines()
kand = {}
golosa = len(text)

for line in text:
    kand[line] = kand.get(line, 0) + 1

kand = sorted(kand.items(), key=lambda x: x[1], reverse=True)
if kand[0][1] > golosa / 2:
    print(kand[0][0], file=resultFile)
else:
    print(kand[0][0], kand[1][0], sep='\n', file=resultFile)
