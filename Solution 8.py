def checkPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def twinPrime():
    twin_primes = []
    for num in range(3, 1000, 2):
        if checkPrime(num) and checkPrime(num + 2):
            twin_primes.append((num, num + 2))
    return twin_primes

def main():
    twin_primes = twinPrime()
    print("Twin Primes less than 1000:")
    for twin_prime in twin_primes:
        print(twin_prime[0], "and", twin_prime[1])
main()
