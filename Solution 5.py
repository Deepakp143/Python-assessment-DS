def calculate_trek_length(A, B, C):
    total_length = A + B + C
    return total_length

def main():
    A = int(input("Enter the distance Amit beats Suman: "))
    B = int(input("Enter the distance Amit beats Ravi: "))
    C = int(input("Enter the distance Suman beats Ravi: "))

    total_trek_length = calculate_trek_length(A, B, C)
    print("Total length of the trek =", total_trek_length, "m")
main()
