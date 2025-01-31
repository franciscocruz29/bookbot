"""
This script reads a text file, counts the number of words and the frequency
of each character (case-insensitive), and then prints a report of the character
frequencies for alphabetic characters in descending order.
"""

def get_book_text(path: str) -> str:
    """Read and return the contents of the file specified by the given path."""

    with open(path) as f:
        return f.read()


def get_num_words(text: str) -> int:
    """Count and return the number of words in the provided text."""

    words = text.split()
    return len(words)


def get_chars_dict(text: str) -> dict[str, int]:
    """Create a dictionary counting the frequency of each character in the text.
    The count is case-insensitive (all characters are converted to lowercase)."""

    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict: dict[str, int]) -> list[dict[str, int]]:
    """Convert a character frequency dictionary into a sorted list of dictionaries.
    Each dictionary in the returned list has the keys "char" and "num".
    The list is sorted in descending order by the frequency ("num")."""

    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def main() -> None:
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        char = str(item["char"])
        # Only include alphabetic characters in the report.
        if not char.isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


if __name__ == "__main__":
    main()
