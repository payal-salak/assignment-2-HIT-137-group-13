"""
HIT137 Assignment 2 - Question 1
A program that reads the text file “raw_text.txt”, encrypts its contents using a 
simple encryption method, and writes the encrypted text to a new file 
“encrypted_text.txt”. Then create a function to decrypt the content, and a function to 
check the correctness of decrypted text.

Group number CAS/DAN 13
S361253 Ashton Searle
s389249 payal 
S391075 Amanparteek singh
S390786 Anshul
S391273 komalpreet kaur
"""

import string

input_file = "raw_text.txt"
encrypted_file = "encrypted_text.txt"

def encrypt_function(n, m, original_text):
    encrypted_text = ""
    for letter in original_text:
        if letter.islower():
            if 'a' <= letter <= 'm':
                shift = n * m
                base = ord('a')
            elif 'n' <= letter <= 'z':
                shift = -(n + m)
                base = ord('n')

        elif letter.isupper():
            if 'A' <= letter <= 'M':
                shift = -n
                base = ord('A')
            elif 'N' <= letter <= 'Z':
                shift = m ** 2
                base = ord('N')

        else:
            encrypted_text += letter
            continue
            
        encrypted_text += chr(((ord(letter) - base + shift) % 13) + base)
    return encrypted_text


def decrypt_function(n, m, encrypted_text):
    decrypted_text = ""
    for letter in encrypted_text:
        if letter.islower():
            if 'a' <= letter <= 'm':
                shift = -(n * m)
                base = ord('a')
            elif 'n' <= letter <= 'z':
                shift = (n + m)
                base = ord('n')

        elif letter.isupper():
            if 'A' <= letter <= 'M':
                shift = n
                base = ord('A')
            elif 'N' <= letter <= 'Z':
                shift = -(m ** 2)
                base = ord('N')

        else:
            decrypted_text += letter
            continue
            
        decrypted_text += chr(((ord(letter) - base + shift) % 13) + base)
    return decrypted_text

def main():
    try:
        n = int(input("Enter value for n: "))
        m = int(input("Enter value for m: "))
        
        with open(input_file, "r", encoding="utf8") as file:
            original_text = file.read()

        encrypted_text = encrypt_function(n, m, original_text)

        with open(encrypted_file, "w", encoding="utf8") as file:
            file.write(encrypted_text)

        decrypted_text = decrypt_function(n, m, encrypted_text)

        if original_text == decrypted_text:
            print("Encryption and decryption successful")
        else:
            print("Error: Decrypted text does not match original.")

    except ValueError:
        print("n or m user input is not an integer") 

    except FileNotFoundError:      
        print("Input file not found")

    except UnicodeDecodeError:     
        print("Input file has special characters that cannot be parsed by this program.") #This disappears when using encoding="utf8" however those special characters are incorrectly encoded

    except IOError:                
        print("Read/Write error")

    except PermissionError:        
        print("File is read-only")
    pass

if __name__ == "__main__":
    main()
