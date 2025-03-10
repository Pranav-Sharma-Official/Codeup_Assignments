def string_expand(st):

    """
    Expands a given string where each character is followed by a digit.
    The character is repeated based on the digit's value.

    Example:
    Input:  "a3b2c4"
    Output: "aaabbcccc"
    """

    string = ""     # Initialize an empty string to store the expanded result.

    # Iterating through the string with a step of 2.
    for i in range(0, len(st), 2):

    # Checking if the current character is a letter and the next one is a digit.
        if(st[i].isalpha() and st[i + 1].isdigit()):
            string += st[i] * int(st[i + 1])        # Repeat character by the number next to it.
        else:
            print("Enter a valid string with a correct format, for example: a3b5cc8!")
    return string       # Return the final expanded string.

input_string = input("Enter a string (eg. a3b5c8): ")       # Get input from the user.
print(string_expand(input_string))      # Call the function and print the expanded string.
