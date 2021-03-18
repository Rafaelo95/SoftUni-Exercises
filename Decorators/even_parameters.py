def even_parameters(function):
    def wrapper(*args):
        is_not_even = False
        numbers = args
        result = 0
        for n in numbers:
            if not isinstance(n, int) or n % 2 != 0:
                result = "Please use only even numbers!"
                is_not_even = True
                break
        if not is_not_even:
            result = function(*args)
        return result
    return wrapper


@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add("Peter", 1))


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
