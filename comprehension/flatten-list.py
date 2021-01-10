line = input()
result = [element for x in reversed(line.split("|")) for element in x.split(" ") if element != ""]
print(' '.join(result))