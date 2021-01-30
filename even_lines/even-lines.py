with open("text.txt", "r") as file:
    for idx, line in enumerate(file):
        if idx % 2 == 0:
            for element in "-,.!?":
                line = line.replace(element, "@")

            words = reversed(line.split())
            print(' '.join(words))