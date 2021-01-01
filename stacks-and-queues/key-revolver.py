from collections import deque

bullet_price = int(input())
barrel_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])
intelligence = int(input())
counter = 0
bullets_used = 0

while bullets:
    counter += 1

    if counter % (barrel_size + 1) == 0:
        print("Reloading!")
        counter = 1

    current_bullet = bullets.pop()

    if not locks:
        bullets.append(current_bullet)
        break

    bullets_used += 1
    current_lock = locks[0]

    if current_bullet <= current_lock:
        locks.popleft()
        print("Bang!")
    else:
        print("Ping!")

bullets_price = bullets_used * bullet_price
money_earned = intelligence - bullets_price

if not locks:
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")