from functools import wraps


def trace(func):
    depth = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal depth

        parts = [repr(arg) for arg in args]
        parts.extend(f"{key}={value!r}" for key, value in kwargs.items())
        call = f"{func.__name__}({', '.join(parts)})"
        indent = "  " * depth

        print(f"{indent}-> {call}")
        depth += 1

        try:
            result = func(*args, **kwargs)
        except Exception as error:
            depth -= 1
            print(f"{indent}<- {call} raised {type(error).__name__}")
            raise

        depth -= 1
        print(f"{indent}<- {call} = {result!r}")
        return result

    return wrapper


if __name__ == "__main__":
    @trace
    def factorial(n):
        if n <= 1:
            return 1
        return n * factorial(n - 1)

    factorial(4)
