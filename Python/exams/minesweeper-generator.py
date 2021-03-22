def increase_size(argument, size, matrix):
    if 0 <= argument[0] < size and 0 <= argument[1] < size and matrix[argument[0]][argument[1]] != '*':
        matrix[argument[0]][argument[1]] += 1


size = int(input())
bombs_num = int(input())

matrix = []
bomb_positions = []

# SETTING UP THE MATRIX
for row in range(size):
    matrix.append([])
    for col in range(size):
        matrix[row].append(0)


for _ in range(bombs_num):

    bomb_pos = input()
    bomb_row = int(bomb_pos[1])
    bomb_col = int(bomb_pos[-2])

    for r in range(size):
        for c in range(size):
            if bomb_row == r and bomb_col == c:
                matrix[r][c] = '*'

                current_bomb_position = [r, c]

                left = [r, c - 1]
                right = [r, c + 1]
                up = [r - 1, c]
                down = [r + 1, c]

                left_up_diagonal = [r - 1, c - 1]
                left_down_diagonal = [r + 1, c - 1]
                right_up_diagonal = [r - 1, c + 1]
                right_down_diagonal = [r + 1, c + 1]

                increase_size(left, size, matrix)
                increase_size(right, size, matrix)
                increase_size(down, size, matrix)
                increase_size(up, size, matrix)

                increase_size(left_up_diagonal, size, matrix)
                increase_size(left_down_diagonal, size, matrix)
                increase_size(right_up_diagonal, size, matrix)
                increase_size(right_down_diagonal, size, matrix)


for element in matrix:
    print(' '.join(list(map(str, element))))