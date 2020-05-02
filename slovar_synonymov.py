kolvo = int(input())
s = {}
for i in range(kolvo):
    perv, vtor = input().split()
    s[perv] = vtor
    s[vtor] = perv
print(s[input()])
