# caesarCipher v3. This version without hardcode SYMBOLS
import sys
from colorama  import Fore, init

def caesar_cipher(text, key):
    result = ""
    for character in text:
        #print("%s" % (ord(character)))
        if character.isupper():
            #upper character
            result += chr((ord(character) - 65 + key) % 26 + 65)
        elif character.islower():
            #lower character
            result += chr((ord(character) - 97 + key) % 26 + 97)
        elif ord(character) in range(33, 57):
            #special character
            result += chr((ord(character) - 33 + key) % 25 + 33)
        else:
            #not found cant encrypt
            result += character
    return result

def main():
    try:
        # Get user input
        text = input("Enter the text to encrypt or decrypt:")
        key = int(input("Enter the key value(positive for encryption, negative for decryption):"))

        #caesar function
        cipher_text = caesar_cipher(text, key)

        #print the result
        print(f"{Fore.GREEN}Result:{Fore.RESET} {cipher_text}")
    except ValueError:
        print(f"{Fore.RED}Error:{Fore.RESET} Invalid input. Please enter a valid key value (integer)")

if __name__ == "__main__":
    main()