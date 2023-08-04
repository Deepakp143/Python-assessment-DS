def prodDigits(n):
    product = 1
    while n != 0:
        digit = n % 10
        product *= digit
        n //= 10
    return product

def MDR(n):
    while n >= 10:
        n = prodDigits(n)
    return n

def MPersistence(n):
    persistence = 0
    while n >= 10:
        n = prodDigits(n)
        persistence += 1
    return persistence

def main():
    num = int(input("Enter a number: "))

    mdr = MDR(num)
    mpersistence = MPersistence(num)

    print("Multiplicative Digital Root:", mdr)
    print("Multiplicative Persistence:", mpersistence)
main()
