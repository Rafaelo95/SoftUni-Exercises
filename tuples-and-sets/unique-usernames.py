n_usernames = int(input())

unique_usernames = set()

for n in range(n_usernames):
    username = input()
    unique_usernames.add(username)

for name in unique_usernames:
    print(name)
