from functools import wraps


def trace(func):
    depth = 0

    @wraps(func)
    def wrapper(*args):
        nonlocal depth
        indent = "  " * depth
        call = f"{func.__name__}({', '.join(repr(arg) for arg in args)})"

        print(f"{indent}-> {call}")
        depth += 1
        result = func(*args)
        depth -= 1
        print(f"{indent}<- {call}")
        return result

    return wrapper


def permutations(nums, show_trace=False):
    result = []

    def backtrack(remaining, current):
        if not remaining:
            result.append(current.copy())
            return

        for index in range(len(remaining)):
            value = remaining[index]
            next_remaining = remaining[:index] + remaining[index + 1 :]
            current.append(value)
            backtrack(next_remaining, current)
            current.pop()

    if show_trace:
        backtrack = trace(backtrack)

    backtrack(list(nums), [])
    return result


if __name__ == "__main__":
    print(permutations([1, 2, 3], show_trace=True))
