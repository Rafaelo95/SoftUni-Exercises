def get_magic_triangle(n):

    triangle = [[1], [1, 1]]
    next_number_position = []
    result = 0

    for i in range(3, n + 1):
        triangle.append([1] * i)


    for row in range(1, n):
        for col in range(len(triangle[row])):
            if col + 1 in range(len(triangle[row])):
                result = triangle[row][col] + triangle[row][col + 1]
                if row + 1 in range(1, n):
                    triangle[row + 1][col + 1] = result

    return print(triangle)

get_magic_triangle(5)