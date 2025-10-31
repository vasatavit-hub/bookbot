from stats import get_char_count
from stats import get_word_count

import sys

def main():
    try:
        filepath = sys.argv[1]
    except Exception:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        pass
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print (f"Found {get_word_count(filepath)} total words")
    print("--------- Character Count -------")
    char_count = get_char_count(filepath)
    for char in char_count:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")
    pass

main ()