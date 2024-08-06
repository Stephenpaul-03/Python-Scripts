import pyperclip
import time as T
import os

MORSE_CODE_DICT = {
    'A': '.-', 
    'B': '-...', 
    'C': '-.-.', 
    'D': '-..', 
    'E': '.', 
    'F': '..-.', 
    'G': '--.', 
    'H': '....', 
    'I': '..', 
    'J': '.---',
    'K': '-.-', 
    'L': '.-..', 
    'M': '--', 
    'N': '-.', 
    'O': '---', 
    'P': '.--.', 
    'Q': '--.-', 
    'R': '.-.', 
    'S': '...', 
    'T': '-',
    'U': '..-', 
    'V': '...-', 
    'W': '.--', 
    'X': '-..-', 
    'Y': '-.--', 
    'Z': '--..',
    '0': '-----', 
    '1': '.----', 
    '2': '..---', 
    '3': '...--', 
    '4': '....-', 
    '5': '.....', 
    '6': '-....', 
    '7': '--...', 
    '8': '---..', 
    '9': '----.',
    ' ': '/'
}

def text_to_morse(text):
    morse_code = ' '.join([MORSE_CODE_DICT[char.upper()] for char in text if char.upper() in MORSE_CODE_DICT])
    return morse_code

def morse_to_text(morse_code):
    morse_code = morse_code.split(' ')
    text = ''.join([key for value in morse_code for key, val in MORSE_CODE_DICT.items() if val == value])
    return text

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def main():
    while True:
        print("\nMorse Code Translator")
        print("1. Text to Morse Code")
        print("2. Morse Code to Text")
        print("3. Exit\n")
        choice = input("Enter your choice (1,2 or 3):")
        if choice == '1':
            text_input = input("\nEnter the text to convert to Morse Code: ")
            morse_output = text_to_morse(text_input)
            print(f"\nMorse Code: {morse_output}")
            pyperclip.copy(morse_output)
            print("\nMorse Code copied to clipboard.")
            T.sleep(1)
            continue

        elif choice == '2':
            morse_input = input("\nEnter the Morse Code to convert to text: ")
            text_output = morse_to_text(morse_input)
            
            print(f"\nText: {text_output}")
            pyperclip.copy(morse_output)
            print("\nText copied to clipboard.")
            T.sleep(1)
            continue
        
        elif choice == '3':
            print("\nClosing Program.Thank you")
            T.sleep(2)
            break
        else:
            print("\nInvalid choice. Please enter 1,2 or 3.")
            T.sleep(1)
            clear_screen()
            continue

if __name__ == "__main__":
    main()
