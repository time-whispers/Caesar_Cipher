
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
num_letters = len(letters)

# The heart of this program
def encrypt_decrypt(text, mode, key):
    result = ''
    if mode == 'd':
        key = -key

    for letter in text:
        letter = letter  #.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                result += letter
            else:
                new_index = index + key
                if new_index >= num_letters:
                    new_index -= num_letters
                elif new_index < 0:
                    new_index += num_letters
                result += letters[new_index]
    return result

print('\n', '*** WELCOME TO CAESAR CIPHER PROGRAM ***', '\n', '*** HOPE YOU FOUND IT ENJOYABLE :) ***', '\n')

# Used to start the program
print('Do you want to Encrypt or Decrypt?')
user_input = input('E/D: ').lower()
print()

# Encryption
if user_input == 'e':
    print('Encryption Mode Selected', '\n')

    key = int(input('Enter the key (1 - 26): '))
    text = input('Enter the text you want to encrypt: ')
    ciphertext = encrypt_decrypt(text, user_input, key)
    print(f'Cipher Text: {ciphertext}')

# Decryption
elif user_input == 'd':
    print('Decryption Mode Selected', '\n')

    key = int(input('Enter the key (1 - 26): '))
    text = input('Enter the text you want to decrypt: ')
    Enterplaintext = encrypt_decrypt(text, user_input, key)
    print(f'Plain Text: {Enterplaintext}')