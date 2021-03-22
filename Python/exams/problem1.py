from collections import deque

males = list(map(int, input().split()))
females = deque(map(int, input().split()))
matches = 0

while males and females:

    current_male = males.copy().pop()
    current_female = females.copy().popleft()

    if current_male % 25 == 0 and current_male != 0:
        males.pop()
        males.pop()
        continue

    if current_female % 25 == 0 and current_female != 0:
        females.popleft()
        females.popleft()
        continue

    if current_male <= 0:
        males.pop()
        continue

    if current_female <= 0:
        females.popleft()
        continue

    if current_male == current_female:
        males.pop()
        females.popleft()
        matches += 1
    else:
        females.popleft()
        current_male -= 2
        males[-1] = current_male

print(f"Matches: {matches}")

if not males:
    print("Males left: none")
else:
    print(f"Males left: {', '.join(reversed(list(map(str, males))))}")

if not females:
    print("Females left: none")
else:
    print(f"Females left: {', '.join(list(map(str, females)))}")