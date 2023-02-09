
text = "Supercalifragilistichespiralidoso"
key = 3

def encrypt(text: str, key: int) -> str:
    """Applies a shift cipher (also known as Caesar cipher) to the input text,
    by rotating it LEFT of key number of positions.
    Returns the rotated text.
    """
    a = ord('a')
    #    chr(ord(character) - key)
    return ''.join(chr((ord(char) - a + key) % 26 + a) for char in input.lower())    
