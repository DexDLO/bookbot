def get_total_words(str_book):
    return len(str_book.split())

def count_characters(text):
    letter_count = {}
    
    # Count each character in the text
    for word in text.split():
        for letter in word:
            if letter.isalpha():  # Ensure we're only counting alphabetic characters
                letter = letter.lower()
                letter_count[letter] = letter_count.get(letter, 0) + 1
    

    letter_list = [{"char": key, "num": value} for key, value in letter_count.items()]
    letter_list.sort(reverse=True, key=sort_on)
    return letter_list

# Example usage:
# text = "Hello world. This is a test."
# result = count_characters(text)

# for letter, count in result.items():
#     print(f"{letter}: {count}")

    #print("Printing letter_list")
    #print(letter_list)
    #print("---------END--------")

def sort_on(items):
    return items["num"]
