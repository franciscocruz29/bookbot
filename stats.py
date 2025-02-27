def get_num_words(text: str) -> int:
    """
    Count and return the number of words in the provided text.

    Args:
        text (str): The text content to analyze.

    Returns:
        int: The total number of words found in the text.

    Note:
        Words are considered to be separated by whitespace characters.
    """

    words = text.split()
    return len(words)


def get_chars_dict(text: str) -> dict[str, int]:
    """
    Generate a dictionary with the frequency of each character in the text.

    The function converts all characters to lowercase to ensure case insensitivity.

    Args:
        text (str): The input text to analyze.

    Returns:
        dict[str, int]: A dictionary where keys are characters and values are their frequencies.
    """

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
    """
    Convert a character frequency dictionary into a sorted list of character-frequency pairs.

    The function transforms the dictionary into a list of dictionaries, where each dictionary
    has two keys:
    - "char" (str): The character.
    - "num" (int): The frequency of the character.

    The resulting list is sorted in descending order based on the character frequency.

    Args:
        num_chars_dict (dict[str, int]): Dictionary containing character frequencies.

    Returns:
        list[dict[str, int]]: A list of dictionaries sorted by frequency in descending order.
    """

    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
