def tags(tag):
    def decorator(fn):
        def wrapper(*args):
            result_of_fn = fn(*args)
            result_of_dec = f"<{tag}>{result_of_fn}</{tag}>"
            return result_of_dec
        return wrapper
    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))