res = [s for s in input().split(', ')]
for i in range(len(res)):
    if i == len(res) - 1:
        print(f"{res[i]} -> {len(res[i])}")
    else:
        print(f"{res[i]} -> {len(res[i])}", end=", ")
