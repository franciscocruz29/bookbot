"""
This script reads a text file, counts the number of words and the frequency
of each character (case-insensitive), and then prints a report of the character
frequencies for alphabetic characters in descending order.
"""

from stats import (
    get_num_words,
    get_chars_dict,
    chars_dict_to_sorted_list
)


def main() -> None:
    """
    Main entry point of the program. Reads the book, processes its text,
    and prints a comprehensive analysis report including word count
    and character frequency statistics.

    Returns:
        None
    """
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print_report(book_path, num_words, chars_sorted_list)


def get_book_text(path):
    """
    Reads and returns the contents of the file specified by the given path.

    Args:
        path (str): The path to the book file.

    Returns:
        str: The contents of the file, or an empty string if the file is not found.
    """
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return ""


def print_report(book_path: str, num_words: int, chars_sorted_list: list[dict[str, int]]) -> None:
    """
    Prints a report of the book analysis, including word count and character frequencies.

    Args:
        book_path (str): The path to the analyzed book file.
        num_words (int): The total number of words in the book.
        chars_sorted_list (list[dict[str, int]]): A sorted list of character frequencies.
    """
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("\n----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("\n--------- Character Count -------")
    for item in chars_sorted_list:
        if not str(item["char"]).isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
