def count_primes(n):
    if n <= 2:
        return 0

    prime = [True] * n
    prime[0] = False
    prime[1] = False

    p = 2

    while p * p < n:
        if prime[p]:
            for x in range(p * p, n, p):
                prime[x] = False
        p += 1

    return sum(prime)


if __name__ == "__main__":
    n = int(input())
    print(count_primes(n))
