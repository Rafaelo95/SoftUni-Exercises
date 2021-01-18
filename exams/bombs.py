from collections import deque

bomb_effects = deque(map(int, input().split(", ")))
bomb_casings = list(map(int, input().split(", ")))

bombs_created = {
    "Datura Bombs": 0,
    "Cherry Bombs": 0,
    "Smoke Decoy Bombs": 0
}

is_successful = False

while bomb_effects and bomb_casings:

    if bombs_created["Datura Bombs"] >= 3 and bombs_created["Cherry Bombs"] >= 3 and bombs_created["Smoke Decoy Bombs"] >= 3:
        is_successful = True
        break

    current_effect = bomb_effects.popleft()
    current_casing = bomb_casings.pop()

    result = current_casing + current_effect

    if result == 40:
        bombs_created["Datura Bombs"] += 1
    elif result == 60:
        bombs_created["Cherry Bombs"] += 1
    elif result == 120:
        bombs_created["Smoke Decoy Bombs"] += 1
    else:
        bomb_effects.appendleft(current_effect)
        current_casing -= 5
        bomb_casings.append(current_casing)


if is_successful:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if not bomb_effects:
    print("Bomb Effects: empty")
else:
    print(f"Bomb Effects: {', '.join(list(map(str, bomb_effects)))}")

if not bomb_casings:
    print("Bomb Casings: empty")
else:
    print(f"Bomb Casings: {', '.join(list(map(str, bomb_casings)))}")

for key, value in sorted(bombs_created.items(), key=lambda x: x[0]):
    print(f"{key}: {value}")
