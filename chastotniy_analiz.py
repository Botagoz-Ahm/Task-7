inputFile = open('input.txt', 'r', encoding='utf8')
outputFile = open('output.txt', 'w', encoding='utf8')
words = {}
for line in inputFile:
    line = line.split()
    for now in line:
        words[now] = words.get(now, 0) + 1


def makeSort(dict):
    return (-dict[1], dict[0])


words = sorted(words.items(), key=makeSort)

for word in words:
    print(word[0], file=outputFile)

inputFile.close()
outputFile.close()
