def merge_dict(list1, list2):
    if len(list1) != len(list2):
        print("List1 and List2 are the same size.")
        return None

    if len(set(list1)) != len(list1):
        print("Error: The first list must contain unique elements.")
        return None
    merged_dict = dict(zip(list1, list2))

    return merged_dict

def main():
    size = int(input("Enter the size of the lists: "))
    print("Enter elements for the first list:")
    list1 = [input(f"Element {i + 1}: ") for i in range(size)]
    print("Enter elements for the second list:")
    list2 = [input(f"Element {i + 1}: ") for i in range(size)]
    
    merged_dict = merge_dict(list1, list2)

    if merged_dict:
        print("Merged Dictionary:", merged_dict)
main()
