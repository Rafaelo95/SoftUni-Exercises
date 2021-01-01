phonebook = {}

while True:
    input_command = input().split("-")
    name = input_command[0]
    if name.isdigit():
        n = int(name)
        for _ in range(n):
            search = input()
            if search in phonebook:
                print(f"{search} -> {phonebook[search]}")
            else:
                print(f"Contact {search} does not exist.")
        break
    phone = input_command[1]
    for _ in input_command:
        phonebook[name] = phone

