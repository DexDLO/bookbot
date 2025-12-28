import sys
from stats import get_total_words, count_characters
def get_book_text(bookpath):
    with open(bookpath) as f:
    # do something with f (the file) here
        file_contents = f.read()

    return file_contents

def main():
    if len(sys.argv) >= 2:
        bookpath = sys.argv[1]
        text = get_book_text(bookpath)
        dict_counts = count_characters(text)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {bookpath}...")
        print("----------- Word Count ----------")
        print(f"Found {get_total_words(text)} total words")
        print("--------- Character Count -------")
        for item in dict_counts:
            print(f"{item['char']}: {item['num']}")
        print("============= END ===============")
        sys.exit(0)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    





if __name__ == "__main__":
    main()