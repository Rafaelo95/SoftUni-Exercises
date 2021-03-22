n_and_m = list(map(int, input().split()))
n = n_and_m[0]
m = n_and_m[1]

set_for_n = set()
set_for_m = set()

for _ in range(n):
    number = input()
    set_for_n.add(number)

for _ in range(m):
    number = input()
    set_for_m.add(number)

result = set_for_n & set_for_m
for i in result:
    print(i)