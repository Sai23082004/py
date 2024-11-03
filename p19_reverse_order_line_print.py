def reverse_lines_to_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        # Read each line from the input file
        for line in infile:
            # Strip the newline character and reverse the line
            reversed_line = line.strip()[::-1]
            # Write the reversed line to the output file
            outfile.write(reversed_line + '\n')

# # Example usage
reverse_lines_to_file('input.txt', 'output.txt')
# Input:
# Hello World
# Python Programming
# OpenAI GPT
# Reverse this line
# output:
# dlroW olleH
# gnimmargorP nohtyP
# TPG IAnepO
# enil siht esreveR
