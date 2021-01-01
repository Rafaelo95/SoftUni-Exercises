from collections import deque

food_quantity = int(input())
order_quantity = deque(map(int, input().split()))
copy = order_quantity.copy()

print(max(order_quantity))

for order in order_quantity:
    if food_quantity >= order:
        copy.popleft()
        food_quantity -= order
    else:
        break

if not copy:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join([str(x) for x in copy])}")