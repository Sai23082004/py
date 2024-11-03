def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(map(s.count, vowels))
input_string = "MUNEERA"
num_vowels = count_vowels(input_string)
print('Number of vowels in ',input_string,"=",num_vowels)

# OUTPUT:
# Number of vowels in  MUNEERA = 4
