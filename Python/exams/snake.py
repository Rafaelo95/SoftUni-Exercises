n = int(input())
matrix = []

food_quantity = 0
snake_position = []
next_snake_position = []
game_over = False

for row in range(n):
    matrix.append(list(input()))

for i in range(n):
    for j in range(n):
        if matrix[i][j] == "S":
            snake_position = [i, j]

while food_quantity < 10:
    command = input()

    if command == "left":
        next_snake_position = [snake_position[0], snake_position[1] - 1]
    elif command == "right":
        next_snake_position = [snake_position[0], snake_position[1] + 1]
    elif command == "up":
        next_snake_position = [snake_position[0] - 1, snake_position[1]]
    elif command == "down":
        next_snake_position = [snake_position[0] + 1, snake_position[1]]

    if next_snake_position[0] in range(n) and next_snake_position[1] in range(n):
        matrix[snake_position[0]][snake_position[1]] = '.'

        if matrix[next_snake_position[0]][next_snake_position[1]] == '*':
            food_quantity += 1
            matrix[next_snake_position[0]][next_snake_position[1]] = 'S'
            snake_position = next_snake_position

        elif matrix[next_snake_position[0]][next_snake_position[1]] == 'B':
            burrow_position = []
            for i in range(n):
                for j in range(n):
                    if matrix[i][j] == "B" and [i, j] != [next_snake_position[0], next_snake_position[1]]:
                        burrow_position = [i, j]

            matrix[next_snake_position[0]][next_snake_position[1]] = '.'
            snake_position = burrow_position
            matrix[snake_position[0]][snake_position[1]] = 'S'

        else:
            snake_position = next_snake_position
    else:
        matrix[snake_position[0]][snake_position[1]] = '.'
        game_over = True
        break

if game_over:
    print("Game over!")
else:
    print("You won! You fed the snake.")
print(f"Food eaten: {food_quantity}")

for item in matrix:
    print(''.join(item))