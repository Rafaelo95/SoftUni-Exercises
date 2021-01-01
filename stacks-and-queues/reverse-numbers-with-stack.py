numbers_stack = list(input().split())
reversed_numbers_stack = []

for i in range(len(numbers_stack)):
    reversed_numbers_stack.append(numbers_stack.pop())

print(' '.join(reversed_numbers_stack))