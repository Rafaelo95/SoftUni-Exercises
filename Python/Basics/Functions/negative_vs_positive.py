numbers = list(map(int, input().split()))

positive_numbers_sum = sum(filter(lambda x: x > 0, numbers))
negative_numbers_sum = sum(filter(lambda x: x < 0, numbers))

print(negative_numbers_sum)
print(positive_numbers_sum)

if positive_numbers_sum > abs(negative_numbers_sum):
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")