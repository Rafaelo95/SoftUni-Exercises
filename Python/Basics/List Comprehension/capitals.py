countries = input().split(", ")
cities = input().split(", ")
info = zip(countries, cities)
res = {print(f"{key} -> {value}") for (key, value) in info}