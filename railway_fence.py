class RailwayFence:
    """
    RailwayFence class for implementing Railway Fence Cipher encryption and decryption.

    Attributes:
    - text (str): The plaintext to be encrypted or the ciphertext to be decrypted.
    - key (int): The key used for encryption or decryption. It represents the number of rails in the fence.
    - cipher_text (str): The result of the encryption process.
    - decrypt_text (str): The result of the decryption process.
    - direction (int): The direction flag used during encryption.

    Methods:
    - __init__(self, text, key): Initializes the RailwayFence object with the provided plaintext and key.
    - encryption(self): Encrypts the plaintext using Railway Fence Cipher.
    - decryption(self): Decrypts the ciphertext using Railway Fence Cipher.
    """

    def __init__(self, text, key):
        """
        Initializes the RailwayFence object with the provided plaintext and key.

        Args:
        - text (str): The plaintext to be encrypted or the ciphertext to be decrypted.
        - key (int): The key used for encryption or decryption. It represents the number of rails in the fence.
        """
        self.text = text
        self.key = key
        self.cipher_text = ""
        self.decrypt_text = ""
        self.direction = 0

    def encryption(self):
        """
        Encrypts the plaintext using Railway Fence Cipher.

        Returns:
        None
        """
        matrix = [[" " for _ in range(len(self.text))] for _ in range(self.key)]
        row = 0

        for i in range(len(self.text)):
            matrix[row][i] = self.text[i]
            if row == 0:
                self.direction = 0
            elif row == self.key - 1:
                self.direction = 1
            if self.direction == 0:
                row += 1
            else:
                row -= 1

        for i in matrix:
            self.cipher_text += ''.join(c for c in i if c != " ")

    def decryption(self):
        """
        Decrypts the ciphertext using Railway Fence Cipher.

        Returns:
        None
        """
        matrix = [["\n" for _ in range(len(self.cipher_text))] for _ in range(self.key)]
        direction = None
        r, c = 0, 0

        for _ in range(len(self.cipher_text)):
            if r == 0:
                direction = True
            if r == self.key - 1:
                direction = False

            matrix[r][c] = "*"
            c += 1

            if direction:
                r += 1
            else:
                r -= 1

        index = 0
        for i in range(self.key):
            for j in range(len(self.cipher_text)):
                if matrix[i][j] == '*' and index < len(self.cipher_text):
                    matrix[i][j] = self.cipher_text[index]
                    index += 1

        result = []
        row, col = 0, 0

        for i in range(len(self.cipher_text)):
            if row == 0:
                direction = True
            if row == self.key - 1:
                direction = False

            if matrix[row][col] != '*':
                result.append(matrix[row][col])
                col += 1

            if direction:
                row += 1
            else:
                row -= 1

        self.decrypt_text = "".join(result)

a = RailwayFence("MuthuPalaniappanM",3)
a.encryption()
print(f"Cipher Text: {a.cipher_text}")
a.decryption()
print(f"Decrpyt Text: {a.decrypt_text}")
