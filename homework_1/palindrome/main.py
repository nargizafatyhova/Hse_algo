def is_palindrome(n):
    x = n
    rev = 0

    while x > 0:
        rev = rev * 10 + x % 10
        x //= 10

    return n == rev


n = int(input())
print(is_palindrome(n))
