sequence = []
n = int(input())

for _ in range(n):
    commands = list(map(int, input().split()))

    if commands[0] == 1:
        element = commands[1]
        sequence.append(element)
    elif commands[0] == 2:
        if sequence:
            sequence.pop()
    elif commands[0] == 3:
        if sequence:
            print(max(sequence))
    elif commands[0] == 4:
        if sequence:
            print(min(sequence))


print(', '.join(reversed((list(map(str, sequence))))))
