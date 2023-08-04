def gcd_list(numbers):
    if len(numbers) < 2:
        raise ValueError("At least 2 numbers are required in the list.")
    
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = gcd(result, numbers[i])
    
    return result

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def main():
    try:
        numbers = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
        result_gcd = gcd_list(numbers)
        print("Greatest Common Divisor of the numbers:", result_gcd)
    except ValueError as e:
        print(e)
main()
