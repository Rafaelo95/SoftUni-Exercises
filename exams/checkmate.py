matrix = []
available_queens = []
king_position = 0

up_left = []
down_right = []
up_right = []
down_left = []

for i in range(8):
    matrix.append(input().split())

for row in range(8):
    for col in range(8):
        if matrix[row][col] == 'K':
            king_position = [row, col]
            for l in range(8):
                up_left.append([row - 1 - l, col - 1 - l]) if row - 1 - l in range(8) and col - 1 - l in range(8) else 0
                down_right.append([row + 1 + l, col + 1 + l]) if row + 1 + l in range(8) and col + 1 + l in range(8) else 0
                up_right.append([row - 1 - l, col + 1 + l]) if row - 1 - l in range(8) and col + 1 + l in range(8) else 0
                down_left.append([row + 1 + l, col - 1 - l]) if row + 1 + l in range(8) and col - 1 - l in range(8) else 0


down = False
right = False
is_down_right = False
is_down_left = False

left_queen = []
up_queen = []
up_right_diagonal = []
up_left_diagonal = []

for r in range(8):
    for c in range(8):
        if matrix[r][c] == 'Q' and king_position[0] == r and king_position[1] < c:
            if not right:
                queen_position = [r, c]
                available_queens.append(queen_position)
                right = True
        if matrix[r][c] == 'Q' and king_position[0] == r and king_position[1] > c:
            queen_position = [r, c]
            left_queen.append(queen_position)
        if matrix[r][c] == 'Q' and king_position[1] == c and king_position[0] < r:
            if not down:
                queen_position = [r, c]
                available_queens.append(queen_position)
                down = True
        if matrix[r][c] == 'Q' and king_position[1] == c and king_position[0] > r:
            queen_position = [r, c]
            up_queen.append(queen_position)

        if matrix[r][c] == 'Q' and [r, c] in up_left:
            queen_position = [r, c]
            up_left_diagonal.append(queen_position)
        if matrix[r][c] == 'Q' and [r, c] in up_right:
            queen_position = [r, c]
            up_right_diagonal.append(queen_position)
        if matrix[r][c] == 'Q' and [r, c] in down_left:
            if not is_down_left:
                queen_position = [r, c]
                available_queens.append(queen_position)
                is_down_left = True
        if matrix[r][c] == 'Q' and [r, c] in down_right:
            if not is_down_right:
                queen_position = [r, c]
                available_queens.append(queen_position)
                is_down_right = True

if left_queen:
    available_queens.append(left_queen[-1])
if up_queen:
    available_queens.append(up_queen[-1])
if up_left_diagonal:
    available_queens.append(up_left_diagonal[-1])
if up_right_diagonal:
    available_queens.append(up_right_diagonal[-1])

if not available_queens:
    print("The king is safe!")
else:
    for item in available_queens:
        print(item)