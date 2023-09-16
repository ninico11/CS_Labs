def get_key(val, alphabet_dict):
   
    for key, value in alphabet_dict.items():
        if val == value:
            return key
 
    return "key doesn't exist"

def optional_denc(alpha, word):
    new_alpha_dict = {}
    word = word.replace(" ", "")
    word = word.upper()
    word = ''.join(sorted(set(word), key=word.index))
    position = 1
    for letter in word:
        if letter.isalpha(): 
            new_alpha_dict[letter] = position
            position += 1
        else:
            continue 
    for key in alpha:
        if key in new_alpha_dict:
            continue
        else:
            new_alpha_dict[key] = position
            position += 1    
    return new_alpha_dict

alphabet_dict = {}
for i, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    alphabet_dict[letter] = i + 1

#{'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11,
#'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
def cesarencrypt(message, enckey, optionalkey = None):
    if optionalkey is None:
        new_aplha_dict = alphabet_dict
    else:
        new_aplha_dict = optional_denc(alphabet_dict, optionalkey)
        for key in new_aplha_dict:
            print(key, end = " ")
    encmess = ""
    message = message.replace(" ", "")
    message = message.upper()
    for letter in message:
        if letter.isalpha():  
            if letter in alphabet_dict:
                if (alphabet_dict[letter] + enckey) > 26:
                    value = (alphabet_dict[letter] + enckey) % 26
                    letter = get_key(value, new_aplha_dict)
                    encmess += letter 
                else:
                    value = alphabet_dict[letter] + enckey
                    letter = get_key(value, new_aplha_dict)
                    encmess += letter
            else:
                print(f"'{letter}' is not in the english alphabet")
        else:
            print(f"'{letter}' is not a letter")
    return encmess
def cesardecrypt(message, deckey, optionalkey = None):
    if optionalkey is None:
        new_aplha_dict = alphabet_dict
    else:
        new_aplha_dict = optional_denc(alphabet_dict, optionalkey)
        for key in new_aplha_dict:
            print(key, end = " ")
    encmess = ""
    message = message.replace(" ", "")
    message = message.upper()
    for letter in message:
        if letter.isalpha():  
            if letter in alphabet_dict:
                if (alphabet_dict[letter] - deckey) < 0:
                    value = (alphabet_dict[letter] - deckey) % 26
                    letter = get_key(value, new_aplha_dict)
                    encmess += letter 
                else:
                    value = alphabet_dict[letter] - deckey
                    letter = get_key(value, new_aplha_dict)
                    encmess += letter
            else:
                print(f"'{letter}' is not in the english alphabet")
        else:
            print(f"'{letter}' is not a letter")
    return encmess

def display_menu():
    print("MENU:")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. EXIT")

while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        message = str(input("Input the message: "))
        key = int(input("Input the encrypt key(int): "))
        optional = str(input("Input optional key(str): "))
        letters = 1
        for letter in optional:
            if letter.isalpha():
                letters = 1
                break
            else:
                letters = 0
        if letters == 0:
            print("Optional key need to have at least one character from alphabet")
            optional = None
            print("\n" + cesarencrypt(message, key, optional))
        else:
            print("\n" + cesarencrypt(message, key, optional))
        
    elif choice == '2':
        message = str(input("Input the message: "))
        key = int(input("Input the encrypt key(int): "))
        optional = str(input("Input optional key(str): "))
        letters = 1
        for letter in optional:
            if letter.isalpha():
                letters = 1
                break
            else:
                letters = 0
        if letters == 0:
            print("Optional key need to have at least one character from alphabet")
            optional = None
            print("\n" + cesardecrypt(message, key, optional))
        else:
            print("\n" + cesardecrypt(message, key, optional))
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3).")


