from dotenv import load_dotenv
import os
import string


def encrypt(text: str, key: int) -> str:
    """Applies a shift cipher (also known as Caesar cipher) to the input text,
    by rotating it LEFT of key number of positions.
    Returns the rotated text.
    """
    # Inizialized empty final variable for output
    output = ""
    # Iterate for every character in the line
    for character in text:
        # Check if a character is an alphabetic character
        if character.isalpha():
            # Ascii code of the character, then subtract 97, or the ascii code of a (first character of the alphabet)
            ascii_code=ord(character) - ord('a')
            # Add to the ascii code the value of the key
            ascii_code += key
            # Returns to the beginning of the alphabet once the ascii code has passed the value of 26 i.e. the letter "z".
            ascii_code = ascii_code % 26
            # Re-add the ascii value of "a"
            ascii_code += ord('a')
            # Add the value of ascii_code to the output
            output += chr(ascii_code)
        else:
            output+=character
    return output
        

    

def _main():
    load_dotenv()
    # Read your secret encryption key from the .env file
    k = os.getenv("CIPHER_KEY")
    # Cast k to int
    k = int(k)
    # Read from encrypt_input.txt
    with open("./encryption/encrypt_input.txt") as input:
        with open("./encryption/encrypt_output.txt", "w") as output:
            for line in input.readlines():
                # Call encrypt on each line with your key
                encrypted_line = encrypt(line, k)
                # Write the encrypted lines to encrypt_output.txtc
                output.write(encrypted_line)
                
if __name__ == "__main__":
    _main()
