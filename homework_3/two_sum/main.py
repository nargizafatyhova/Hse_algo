def two_sum(arr, k):
    seen = {}

    for index, value in enumerate(arr):
        second_value = k - value

        if second_value in seen:
            return seen[second_value], index

        seen[value] = index

    raise ValueError("pair not found")


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())
    print(*two_sum(arr, k))
