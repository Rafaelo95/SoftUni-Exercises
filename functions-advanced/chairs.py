from itertools import combinations

people = input().split(', ')
n = int(input())
for x in combinations(people, n):
    print(', '.join(x))
