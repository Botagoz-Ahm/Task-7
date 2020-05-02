n = int(input())
numbers = set(range(1, n + 1))
possibles = numbers
while True:
    variant = input()
    if variant == 'HELP':
        break
    variant = {int(i) for i in variant.split()}
    answer = input()
    if answer == 'YES':
        possibles &= variant
    else:
        possibles &= numbers - variant
print(' '.join([str(i) for i in sorted(possibles)]))
