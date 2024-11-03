def check_substring(main_string, substring):
    if substring in main_string:
        return True
    else:
        return False
main_string = "This is a sample string"
substring = "python"
if check_substring(main_string, substring):
    print("The substring ",substring,"is present in the main string.")
else:
    print("The substring ",substring," is not present in the main string.")

# OUTPUT:
# The substring  python  is not present in the main string.

