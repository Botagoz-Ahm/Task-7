mySet = [int(i) for i in input().split()]
vstr = set()
for now in mySet:
    if now in vstr:
        print('YES')
    else:
        print('NO')
        vstr.add(now)
