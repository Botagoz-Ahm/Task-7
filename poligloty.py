n = [{input() for j in range(int(input()))} for i in range(int(input()))]
knows_everyone, knows_someone = set.intersection(*n), set.union(*n)
print(len(knows_everyone), *sorted(knows_everyone), sep='\n')
print(len(knows_someone), *sorted(knows_someone), sep='\n')
