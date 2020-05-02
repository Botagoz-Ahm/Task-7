nomer = {}
for slovo in input().split():
    nomer[slovo] = nomer.get(slovo, 0) + 1
    print(nomer[slovo] - 1, end=' ')
