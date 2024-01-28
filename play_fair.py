import numpy as np

def playfair_key_matrix(key):

    J = ord("j") - ord("a")
    I = ord("i") - ord("a")

    key = key.lower()
    
    # Forming key matrix
    key = [ord(k) - ord("a") for k in key]
    for _ in range(26):
        if _ not in key:
            key += [_]
    while J in key:
        key[key.index(J)] = I
    KEY_MATRIX = []
    for k in key:
        if k not in KEY_MATRIX:
            KEY_MATRIX += [k]
    KEY_MATRIX = np.array(KEY_MATRIX)
    KEY_MATRIX = np.reshape(KEY_MATRIX, (5,5))

    return KEY_MATRIX

def playfair_cipher(value, key):

    J = ord("j") - ord("a")
    I = ord("i") - ord("a")

    KEY_MATRIX = playfair_key_matrix(key)


    value = value.lower()
    # Form couplets
    value = [ord(v) - ord("a") for v in value]
    if len(value)%2 != 0:
        value += [ord("z") - ord("a")]
    value = np.reshape(np.array(value), (-1,2))
    for v in range(len(value)):
        if value[v][0] == value[v][1]:
            value[v][1] = ord("x") - ord("a")
        if value[v][0] == J:
            value[v][0] = I
        if value[v][1] == J:
            value[v][1] = I

        char0 = np.where(KEY_MATRIX == value[v][0])
        char0 = (char0[0][0], char0[1][0])
        char1 = np.where(KEY_MATRIX == value[v][1])
        char1 = (char1[0][0], char1[1][0])

        # Same row
        if char0[0] == char1[0]:
            value[v][0] = KEY_MATRIX[char0[0]][(char0[1] + 1) % 5]
            value[v][1] = KEY_MATRIX[char1[0]][(char1[1] + 1) % 5]

        # same column
        elif char0[1] == char1[1]:
            value[v][0] = KEY_MATRIX[(char0[0] + 1) % 5][char0[1]]
            value[v][1] = KEY_MATRIX[(char1[0] + 1) % 5][char1[1]]

        # standard case
        else:
            value[v][0] = KEY_MATRIX[char0[0]][char1[1]]
            value[v][1] = KEY_MATRIX[char1[0]][char0[1]]

    value = np.reshape(value, (-1))

    value = "".join([chr(ord("a") + v) for v in value])

    return value

def playfair_decipher(value, key):

    KEY_MATRIX = playfair_key_matrix(key)

    # Form couplets
    value = [ord(v) - ord("a") for v in value]

    value = np.reshape(np.array(value), (-1,2))
    for v in range(len(value)):

        char0 = np.where(KEY_MATRIX == value[v][0])
        char0 = (char0[0][0], char0[1][0])
        char1 = np.where(KEY_MATRIX == value[v][1])
        char1 = (char1[0][0], char1[1][0])

        # Same row
        if char0[0] == char1[0]:
            value[v][0] = KEY_MATRIX[char0[0]][(char0[1] - 1) % 5]
            value[v][1] = KEY_MATRIX[char1[0]][(char1[1] - 1) % 5]

        # same column
        elif char0[1] == char1[1]:
            value[v][0] = KEY_MATRIX[(char0[0] - 1) % 5][char0[1]]
            value[v][1] = KEY_MATRIX[(char1[0] - 1) % 5][char1[1]]

        # standard case
        else:
            value[v][0] = KEY_MATRIX[char0[0]][char1[1]]
            value[v][1] = KEY_MATRIX[char1[0]][char0[1]]

    value = np.reshape(value, (-1))

    value = "".join([chr(ord("a") + v) for v in value])

    

    return value


def hill_cipher(value, key):

    value = value.lower()
    size = key.shape[0]

    value = [ord(v) - ord("a") + 1 for v in value]
    while len(value)%size != 0:
        value += [ord("z") - ord("a")]

    value = np.array(value).reshape((-1,size))

    enc = (key @ value.T).T % 26

    enc = "".join([chr(ord("a") - 1 + e) for e in np.reshape(enc, (-1))])

    return enc

def hill_decipher(value, key):

    # getting decipher matrix
    det = int(np.linalg.det(key))
    det %= 26
    for num in range(1,10000):
        if (num * det) % 26 == 1:
            break
    dec = np.linalg.inv(key) * np.linalg.det(key)
    dec *= num
    dec = dec.astype(int)
    dec %= 26

    # forming groups
    value = value.lower()
    size = key.shape[0]

    value = [ord(v) - ord("a") for v in value]
    value = np.array(value).reshape((-1,size))

    # deciphering
    decipher = (value @ dec) % 26

    decipher = decipher + ord("a")
    decipher = decipher.reshape(-1)

    print(decipher)
    
    # text conversion 
    decipher = "".join([chr(v) for v in decipher])
    return decipher
