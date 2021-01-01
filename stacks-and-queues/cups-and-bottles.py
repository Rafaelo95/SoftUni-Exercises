from collections import deque

cup_capacity = deque([int(x) for x in input().split()])
bottle_with_water = [int(x) for x in input().split()]
wasted_water = 0

while cup_capacity and bottle_with_water:
    current_cup = cup_capacity.popleft()
    current_bottle = bottle_with_water.pop()

    current_cup -= current_bottle

    if current_cup <= 0:
        wasted_water += abs(current_cup)
    else:
        cup_capacity.appendleft(current_cup)

if bottle_with_water:
    print(f"Bottles: {' '.join(list(map(str, reversed(bottle_with_water))))}")
elif cup_capacity:
    print(f"Cups: {' '.join(list(map(str, cup_capacity)))}")
print(f"Wasted litters of water: {wasted_water}")