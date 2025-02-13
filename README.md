# Text File Analyzer

This Python script reads a text file, counts the number of words, and calculates the frequency of each alphabetic character (case-insensitive). It then generates a report of the character frequencies in descending order.

## Features

- **Word Count**: Counts the total number of words in the text file.
- **Character Frequency Analysis**: Calculates the frequency of each alphabetic character, ignoring case.
- **Sorted Report**: Generates a report of character frequencies sorted in descending order.

## Usage

1. **Place the Text File**: Ensure the text file you want to analyze is placed in the `books/` directory. By default, the script looks for a file named `frankenstein.txt`.

2. **Run the Script**: Execute the script using Python 3.

   ```bash
   python3 main.py
   ```

3. **View the Report**: The script will output a report to the console, showing the total number of words and the frequency of each alphabetic character in the text.

## Functions

- **`get_book_text(path: str) -> str`**: Reads and returns the contents of the file specified by the given path.

- **`get_num_words(text: str) -> int`**: Counts and returns the number of words in the provided text.

- **`get_chars_dict(text: str) -> dict[str, int]`**: Creates a dictionary counting the frequency of each character in the text. The count is case-insensitive.

- **`chars_dict_to_sorted_list(num_chars_dict: dict[str, int]) -> list[dict[str, int]]`**: Converts a character frequency dictionary into a sorted list of dictionaries. Each dictionary in the returned list has the keys `"char"` and `"num"`. The list is sorted in descending order by the frequency (`"num"`).

- **`main() -> None`**: The main function that orchestrates reading the file, counting words, analyzing character frequencies, and printing the report.

## Example Output

```
--- Begin report of books/frankenstein.txt ---
78900 words found in the document

The 'e' character was found 46043 times
The 't' character was found 30365 times
The 'a' character was found 26743 times
The 'o' character was found 25225 times
The 'i' character was found 24673 times
...
--- End report ---
```

## Requirements

- Python 3.x

## License

This script is provided under the MIT License. Feel free to modify and distribute it as needed.

## Author

Francisco Cruz
