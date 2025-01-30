from collections import Counter

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    char_frequencies = count_character_frequencies(text)
    print(char_frequencies)


def count_character_frequencies(text: str) -> dict[str, int]:
    """text = text.lower()
    char_counts = {}
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts"""
    return dict(Counter(text.lower()))


def get_num_words(text: str) -> int:
    words = text.split()
    return len(words)


def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()


main()
