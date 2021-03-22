from collections import deque

customers = deque(map(int, input().split(', ')))
taxis = list(map(int, input().split(', ')))
total_time = 0

is_successful = False

while True:

    if not customers:
        is_successful = True
        print('All customers were driven to their destinations')
        print(f'Total time: {total_time} minutes')
        break
    elif not taxis:
        print('Not all customers were driven to their destinations')
        print(f'Customers left: {", ".join(list(map(str, customers)))}')
        break

    current_customer = customers.popleft()
    current_taxi = taxis.pop()

    if current_taxi >= current_customer:
        total_time += current_customer
    else:
        customers.appendleft(current_customer)


