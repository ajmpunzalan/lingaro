# Write decorator that counts function executions and prints it alongside with function name

def counter(func):
    func.executions = 1

    def wrapper(*args, **kwargs):
        print(
            f"Function name: {func.__name__}, executions: {func.executions}")
        func.executions += 1
        return func(*args, **kwargs)
    return wrapper


@counter
def test():
    pass


test()
test()
