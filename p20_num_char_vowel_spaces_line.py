def count_file_stats(input_file):
    # Open the file and read its content
    with open(input_file, 'r') as infile:
        text = infile.read()

    # Calculate the number of lines
    num_lines = text.count('\n') + 1

    # Calculate the number of words
    num_words = len(text.split())

    # Calculate the number of characters
    num_chars = len(text)

    # Print the results
    print("Lines: ",num_lines)
    print("Words: ",num_words)
    print("Characters: ",num_chars)

# # Example usage
count_file_stats('input.txt')
# input:
# Hello World
# Python programming is interesting.
# How many words are here?
# output:
# Lines:  3
# Words:  11
# Characters:  71
