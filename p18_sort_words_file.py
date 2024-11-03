# Function to sort words and save to a new file
def sort_words(input_file, output_file):
    with open(input_file, 'r') as infile:
        # Read all words, convert to lowercase, and split into a list of words
        words = infile.read().lower().split()

    # Sort the list of words alphabetically
    words.sort()

    # Write the sorted words to the output file
    with open(output_file, 'w') as outfile:
        outfile.write("\n".join(words))

# # Example usage
# sort_words('input.txt', 'output.txt')
# input.txt:
# Zebra apple Mango orange BANANA
# output:
# apple
# banana
# mango
# orange
# zebra
