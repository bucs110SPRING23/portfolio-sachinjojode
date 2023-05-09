import json


def caesar_cipher(text, shift):
    """
    Encrypts or decrypts a message using the Caesar cipher technique.

    args:
        text:str = the message to encrypt or decrypt
        shift:int = the number of positions to shift each letter
    return:
        :str = the encrypted or decrypted message
    """
    
    """
    Make it so that each letter is shifted using the 3n + 1 rule
    """

    result = ""
    for i, char in enumerate(text):
        if char.isalpha() and i % 2 != 0:
        # Determine the case of the character
            start = ord('A') if char.isupper() else ord('a')
        # Calculate the new position of the character after the shift
            new_pos = (ord(char) - start + shift) % 26
        # Convert the new position back to a character
            char = chr(start + new_pos)
        result += char
    return result

def main():
    file_pointer = open("encrypted.txt","w")
    result = caesar_cipher("abcdefg", 3)
    file_pointer.write(result)
    file_pointer.close()
    
main()


print()