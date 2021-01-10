numbers = list(map(int, input().split(", ")))
positive = [x for x in numbers if x >= 0]
negative = [x for x in numbers if x < 0]
even = [x for x in numbers if x % 2 == 0]
odd = [x for x in numbers if x % 2 == 1]

print(f"Positive: {', '.join(list(map(str, positive)))}")
print(f"Negative: {', '.join(list(map(str, negative)))}")
print(f"Even: {', '.join(list(map(str, even)))}")
print(f"Odd: {', '.join(list(map(str, odd)))}")