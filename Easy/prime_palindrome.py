

def is_prime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    n = str(n)
    if n == n[::-1]:
        return True
    return False

def greatest_prime_palindrome(n):
    prime_palindromes = [p for p in range(2,n) if is_prime(p) and is_palindrome(p)]
    return prime_palindromes[-1]

print(greatest_prime_palindrome(1000))







