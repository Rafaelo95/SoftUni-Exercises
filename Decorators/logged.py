def logged(fn):
    def wrapper(*args):
        result = ''
        func_result = fn(*args)
        result += f"you called {fn.__name__}{args}\n"
        result += f"it returned {func_result}"
        return result
    return wrapper



@logged
def func(*args):
    return 3 + len(args)

@logged
def sum_func(a, b):
    return a + b


print(func(4, 4, 4))
print(sum_func(1, 4))
