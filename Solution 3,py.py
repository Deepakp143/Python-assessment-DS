def count_words(word, string):
    count = 0
    index = 0
    while index < len(string):
        index = string.find(word, index)
        if index == -1:
            break
        count += 1
        index += 1
    return count

def check_cat_dog(string):
    cat_count = count_words("cat", string.lower())
    dog_count = count_words("dog", string.lower())

    return cat_count == dog_count

def main():
    input_string = input("Enter a string: ")
    result = check_cat_dog(input_string)
    print("Output:", result)
main()
