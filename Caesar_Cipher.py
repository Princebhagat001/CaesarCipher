"""
Student Name: PrinceBhagat
Student ID: 2603801 
Description: Caesar Cipher 
"""
def welcome():
    """Displaying a welcome message to the user & explaining what the program does."""
    print(
        "Welcome to the Caesar Cipher\n"
        "This program encrypts and decrypts text with the Caesar Cipher.\n"
    )

def enter_message():
    """
    Taking user input for mode, message, and shift value &
    returning (mode, message, shift value)
    """
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d): ").lower()
        if mode in ("e", "d"):
            break
        print("Invalid Mode")
    message = input(
        f"What message would you like to "
        f"{'encrypt' if mode == 'e' else 'decrypt'}: "
    ).upper()
    while True:
        shift_input = input("What is the shift number: ")
        if shift_input.isdigit():
            shift = int(shift_input)
            break
        print("Invalid Shift")
    return mode, message, shift

def encrypt(message, shift):
    """Encrypting the text by moving letters in the alphabet using the Caesar Cipher algorithm."""
    encrypted = ""
    for char in message:
        if char.isalpha():
            encrypted += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            encrypted += char
    return encrypted

def decrypt(message, shift):
    """Decrypting the text by moving letters back to there original position using the Caesar Cipher algorithm."""
    decrypted = ""
    for char in message:
        if char.isalpha():
            decrypted += chr((ord(char) - 65 - shift) % 26 + 65)
        else:
            decrypted += char
    return decrypted

def is_file(filename):
    """Checking whether file name is real and exists in the current directory(Filehanding seaction)."""
    try:
        with open(filename, "r"):
            return True
    except FileNotFoundError:
        return False

def process_file(filename, mode):
    """
    Reads each line from a file and encrypts/decrypts them, then returns the output.
    """
    while True:
        shift_input = input("What is the shift number: ")
        if shift_input.isdigit():
            shift = int(shift_input)
            break
        print("Invalid Shift")
    results = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip().upper()
            if mode == "e":
                results.append(encrypt(line, shift))
            else:
                results.append(decrypt(line, shift))

    return results

def write_messages(messages):
    """Saves output into results.txt."""
    with open("results.txt", "w", encoding="utf-8") as file:
        for message in messages:
            file.write(message + "\n")

def message_or_file():
    """
    Asks the user if they want to encrypt/decrypt and if input comes from console or file.
    Returns: (mode, message or None, filename or None)
    """
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d): ").lower()
        if mode in ("e", "d"):
            break
        print("Invalid Mode")
    while True:
        choice = input(
            "Would you like to read from a file (f) or the console (c)? "
        ).lower()
        if choice == "c":
            message = input(
                f"What message would you like to "
                f"{'encrypt' if mode == 'e' else 'decrypt'}: "
            ).upper()
            return mode, message, None
        if choice == "f":
            while True:
                filename = input("Enter a filename: ")
                if is_file(filename):
                    return mode, None, filename
                print("Invalid Filename")
            """Filehandling seaction ends here"""
        print("Invalid Choice")

def main():
    """Main controls of program and it's function."""
    welcome()
    while True:
        mode, message, filename = message_or_file()

        if filename is not None:
            results = process_file(filename, mode)
            write_messages(results)
            print("Output written to results.txt")
        else:
            while True:
                shift_input = input("What is the shift number: ")
                if shift_input.isdigit():
                    shift = int(shift_input)
                    break
                print("Invalid Shift")
            if mode == "e":
                print(encrypt(message, shift))
            else:
                print(decrypt(message, shift))

        while True:
            cont = input(
                "Would you like to encrypt or decrypt another message? (y/n): "
            ).lower()
            if cont in ("y", "n"):
                break
            print("Invalid input")
        if cont == "n":
            print("Thanks for using the program, goodbye!")
            break
main()