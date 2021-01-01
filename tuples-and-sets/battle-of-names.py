n = int(input())

odd_set = set()
even_set = set()

for i in range(1, n + 1):
    ascii_value = 0
    name = input()
    for ch in name:
        ascii_value += ord(ch)

    result = int(ascii_value / i)
    if result % 2 == 0:
        even_set.add(result)
    elif result % 2 == 1:
        odd_set.add(result)

if sum(odd_set) == sum(even_set):
    res = odd_set.union(even_set)
    print(f"{', '.join(map(str, res))}")
elif sum(odd_set) > sum(even_set):
    res = odd_set.difference(even_set)
    print(f"{', '.join(map(str, res))}")
elif sum(odd_set) < sum(even_set):
    res = odd_set.symmetric_difference(even_set)
    print(f"{', '.join(map(str, res))}")
