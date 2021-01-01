parentheses = input()
stack = []
pairs = {
    "{": "}",
    "(": ")",
    "[": "]"
}
valid = True

for element in parentheses:
    if element in "([{":
        stack.append(element)
    elif element in ")]}":
        if stack:
            current = stack[-1]
            if pairs[current] == element:
                stack.pop()
            else:
                valid = False
                break
        else:
            valid = False
            break

if valid:
    print("YES")
else:
    print("NO")