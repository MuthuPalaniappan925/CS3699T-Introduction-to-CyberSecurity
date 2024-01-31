class Vigenere_cipher:
    """
    Vigenere_cipher class for implementing Vigenere Cipher encryption and decryption.

    Attributes:
    - text (str): The plaintext to be encrypted or the ciphertext to be decrypted.
    - key (str): The key used for encryption or decryption.
    - li_text (list): List of characters representing the individual characters in the plaintext.
    - li_key (list): List of characters representing the individual characters in the key.
    - li_enc (list): List of characters representing the individual characters in the encrypted text.
    - li_dec (list): List of characters representing the individual characters in the decrypted text.
    - cipher_text (str): The result of the encryption process.
    - decrypt_text (str): The result of the decryption process.

    Methods:
    - __init__(self, text, key): Initializes the Vigenere_cipher object with the provided plaintext and key.
    - generate_key(self): Generates a key of the same length as the plaintext if the key is shorter.
    - encryption(self): Encrypts the plaintext using Vigenere Cipher.
    - decrypt(self): Decrypts the ciphertext using Vigenere Cipher.
    """

    def __init__(self, text, key):
        """
        Initializes the Vigenere_cipher object with the provided plaintext and key.

        Args:
        - text (str): The plaintext to be encrypted or the ciphertext to be decrypted.
        - key (str): The key used for encryption or decryption.
        """
        self.text = text.upper()
        self.key = key.upper()
        self.li_text = list(self.text)
        self.li_key = list(self.key)
        self.li_enc = []
        self.li_dec = []
        self.cipher_text = ""
        self.decrypt_text = ""
        self.generate_key()

    def generate_key(self):
        """
        Generates a key of the same length as the plaintext if the key is shorter.

        If the key is already longer or equal in length, the original key is kept.

        Returns:
        None
        """
        if len(self.text) > len(self.key):
            k = 0
            for i in range(len(self.text)):
                if i >= len(self.key):
                    self.li_key.append(self.li_key[k])
                    k += 1
            self.key = "".join(self.li_key)
        else:
            return self.key

    def encryption(self):
        """
        Encrypts the plaintext using Vigenere Cipher.

        Returns:
        None
        """
        for i, j in zip(self.li_text, self.li_key):
            temp = chr((ord(i) - 65 + (ord(j) - 65)) % 26 + 65)
            self.li_enc.append(temp)

        self.cipher_text = "".join(self.li_enc)

    def decrypt(self):
        """
        Decrypts the ciphertext using Vigenere Cipher.

        Returns:
        None
        """
        for i, j in zip(self.cipher_text, self.key):
            temp = chr((ord(i) - ord(j) + 26) % 26 + 65)
            self.li_dec.append(temp)

        self.decrypt_text = "".join(self.li_dec)
        
text = "Muthu"
key = "Bfc"

a = Vigenere_cipher(text,key)
a.encryption()
print(f"Cipher Text: {a.cipher_text}")
a.decrypt()
print(f"Decryption Text: {a.decrypt_text}")


"""
if len(text)!=len(key):
    li_test = list(key)
    index = 0
    for i in range(len(text)):
        if i < len(key):
            pass
        else:
            if index <= len(li_test) -1:
                key+=li_test[index]
                index+=1
            
            else:
                index = 0
                key+=li_test[index]
                index+=1
"""
