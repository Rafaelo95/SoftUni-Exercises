n = int(input())

unique_chemicals = set()

for _ in range(n):
    chemicals = input().split()
    for i in chemicals:
        unique_chemicals.add(i)

for c in unique_chemicals:
    print(c)