def even_filter(input_list):
    return [num for num in input_list if num % 2 == 0]

def odd_filter(input_dict):
    return {key: value for key, value in input_dict.items() if value % 2 != 0}

def main():
    # Taking user input for list and dictionary
    list_input = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
    dict_input = {}
    n = int(input("Enter the number of key-value pairs in the dictionary: "))
    for i in range(n):
        key = input("Enter key: ")
        value = int(input("Enter value: "))
        dict_input[key] = value

    even_list = even_filter(list_input)
    odd_dict = odd_filter(dict_input)

    print("Even values from the list:", even_list)
    print("Odd values from the dictionary:", odd_dict)
main()
