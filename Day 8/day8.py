import string


def caesar_cipher(direction, text, shift):
    # Define the alphabet list for reference
    alphabet = list(string.ascii_lowercase)

    # Adjust shift if it's larger than the alphabet length
    shift = shift % len(alphabet)

    # Initialize the result string
    result = ""

    # Loop through each character in the text
    for char in text:
        # Check if the character is a letter
        if char in alphabet:
            # Find the index of the character
            index = alphabet.index(char)

            # Calculate the new index based on the direction
            if direction == "encode":
                new_index = (index + shift) % len(alphabet)
            elif direction == "decode":
                new_index = (index - shift) % len(alphabet)

            # Append the shifted character to the result
            result += alphabet[new_index]
        else:
            # If the character is not a letter, append it as it is
            result += char

    return result


# Example usage
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Call the function with the example inputs
encoded_message = caesar_cipher(direction, text, shift)
decoded_message = caesar_cipher("decode", encoded_message, shift)

print(encoded_message)
print(decoded_message)

encoded_message, decoded_message
