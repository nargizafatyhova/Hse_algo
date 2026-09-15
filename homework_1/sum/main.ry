def max_even_sum(nums):
    total = sum(nums)

    if total % 2 == 0:
        return total

    odd = min(x for x in nums if x % 2 != 0)
    return total - odd


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(max_even_sum(nums))
