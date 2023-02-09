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
            # 
            ascii_code=ord(character) - ord('a')
            ascii_code += key
            ascii_code = ascii_code % 26
            ascii_code += ord('a')
            output += chr(ascii_code)
        else:
            output+=character
    return output
        

    

def _main():
    load_dotenv()
    # read your secret encryption key from the .env file
    k = os.getenv("CIPHER_KEY")
    k = int(k)
    # read from encrypt_input.txt
    with open("./encryption/encrypt_input.txt") as input:
        with open("./encryption/encrypt_output.txt", "w") as output:
            for line in input.readlines():
                # call encrypt on each line with your key
                encrypted_line = encrypt(line, k)
                # write the encrypted lines to encrypt_output.txtc
                output.write(encrypted_line)
                
if __name__ == "__main__":
    _main()
