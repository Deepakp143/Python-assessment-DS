def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def permutations(n, r):
    if n < r:
        return 0
    return factorial(n) // factorial(n - r)

def combinations(n, r):
    if n < r:
        return 0
    return permutations(n, r) // factorial(r)

def main():
    n = int(input("Enter the value of n: "))
    r = int(input("Enter the value of r: "))

    perm = permutations(n, r)
    comb = combinations(n, r)

    print("Number of permutations of {} objects taken {} at a time: {}".format(n, r, perm))
    print("Number of combinations of {} objects taken {} at a time: {}".format(n, r, comb))
main()
