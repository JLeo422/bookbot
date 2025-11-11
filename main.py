from stats import get_num_words, character_count,sorted_dict
import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    text = get_book_text(book_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    print("----------- Word Count ----------")
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    char_counts = character_count(text)
    sorted_chars = sorted_dict(char_counts)

    for item in sorted_chars:
        char = item["char"]
        num = item["num"]
        if char.isalpha():
            print(f"{char}: {num}")

    print("============= END ===============")
main()
