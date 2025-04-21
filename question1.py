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

INPUT_FILE = "raw_text.txt"
ENCRYPTED_FILE = "encrypted_text.txt"

def shift_letter(letter, shift, base, range_size=13):
    return chr(((ord(letter) - base + shift) % range_size) + base)

def encrypt_letter(letter, n, m):
    if letter.islower():
        if 'a' <= letter <= 'm':
            return shift_letter(letter, n * m, ord('a'))
        elif 'n' <= letter <= 'z':
            return shift_letter(letter, -(n + m), ord('n'))
    elif letter.isupper():
        if 'A' <= letter <= 'M':
            return shift_letter(letter, -n, ord('A'))
        elif 'N' <= letter <= 'Z':
            return shift_letter(letter, m ** 2, ord('N'))
    return letter

def decrypt_letter(letter, n, m):
    if letter.islower():
        if 'a' <= letter <= 'm':
            return shift_letter(letter, -(n * m), ord('a'))
        elif 'n' <= letter <= 'z':
            return shift_letter(letter, (n + m), ord('n'))
    elif letter.isupper():
        if 'A' <= letter <= 'M':
            return shift_letter(letter, n, ord('A'))
        elif 'N' <= letter <= 'Z':
            return shift_letter(letter, -(m ** 2), ord('N'))
    return letter

def encrypt_text(text, n, m):
    return ''.join(encrypt_letter(char, n, m) for char in text)

def decrypt_text(text, n, m):
    return ''.join(decrypt_letter(char, n, m) for char in text)

def main():
    try:
        n = int(input("Enter value for n: "))
        m = int(input("Enter value for m: "))

        with open(INPUT_FILE, "r", encoding="utf-8") as file:
            original_text = file.read()

        encrypted = encrypt_text(original_text, n, m)

        with open(ENCRYPTED_FILE, "w", encoding="utf-8") as file:
            file.write(encrypted)

        decrypted = decrypt_text(encrypted, n, m)

        if original_text == decrypted:
            print("✅ Encryption and decryption successful!")
        else:
            print("❌ Error: Decrypted text does not match the original.")

    except ValueError:
        print(" Please enter valid integers for n and m.")
    except FileNotFoundError:
        print("Input file not found.")
    except UnicodeDecodeError:
        print("Special characters found that couldn't be decoded.")
    except IOError:
        print("File read/write error occurred.")
    except PermissionError:
        print("Cannot write to file (permission denied).")


main()
