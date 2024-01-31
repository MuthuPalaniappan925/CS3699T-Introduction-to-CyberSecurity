def rot_13(text):
    result = ''
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            offset = 13
            if is_upper:
                result += chr((ord(char) - ord('A') + offset) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + offset) % 26 + ord('a'))
        else:
            result += char
    return result
