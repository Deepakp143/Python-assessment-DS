def paragraph_list(paragraph):
    words = paragraph.split()
    
    result_list = [word for word in words if len(word) > 4]

    return result_list

def main():
    paragraph = input("Enter a paragraph: ")

    result_list = paragraph_list(paragraph)

    print("Result List:", result_list)
main()
