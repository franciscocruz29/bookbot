# Algorithm: Count the number of words in a text string using string splitting
# Input: A string of text
# Output: The number of words in the input
#
# Step 1: Normalize the text
# - Strip leading and trailing spaces from the text.
# - Replace multiple spaces with a single space to avoid empty strings during splitting.
#
# Step 2: Split the text into words
# - Use the space character as a delimiter to split the text into a list of words.
#
# Step 3: Count the words
# - Calculate the length of the list of words.
#
# Step 4: Return the word count
# - Output the total number of words in the text.

def count_words(text: str) -> int:
    normalized_text = ' '.join(text.split())
    words = normalized_text.split(' ')
    word_count = len(words)
    return word_count

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(count_words(file_contents))


main()
