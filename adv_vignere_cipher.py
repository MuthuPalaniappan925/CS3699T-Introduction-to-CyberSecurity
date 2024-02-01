def adv_vigenere_cipher(message, key, encrypt=True):
    result = ""
    key_index = 0

    for char in message:
        if char.isalpha():
            is_lower = char.islower()
            case_offset = 97 if is_lower else 65
            key_char = key[key_index % len(key)]
            key_offset = ord(key_char) - case_offset

            if encrypt:
                new_char = chr((ord(char) - case_offset + key_offset) % 26 + case_offset)
            else:
                new_char = chr((ord(char) - case_offset - key_offset) % 26 + case_offset)

            result += new_char
            key_index += 1
        else:
            result += char

    return result

message = "Hello, World!"
key = "Key"
encrypted_message = vigenere_cipher(message, key, encrypt=True)
decrypted_message = vigenere_cipher(encrypted_message, key, encrypt=False)
