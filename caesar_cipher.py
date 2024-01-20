class Caesar_cipher:
    """
    Caesar_cipher class for implementing Caesar Cipher encryption and decryption.

    Attributes:
    - key (int): The key used for encryption or decryption. It represents the shift value.
    - text (str): The plaintext to be encrypted or the ciphertext to be decrypted.
    - li_enc (list): List of integer values representing the ASCII values of characters in the encrypted text.
    - li_dec (list): List of integer values representing the ASCII values of characters in the decrypted text.
    - cipher_text (str): The result of the encryption process.
    - decrypt_text (str): The result of the decryption process.

    Methods:
    - encryption(): Encrypts the plaintext using Caesar Cipher.
    - decryption(): Decrypts the ciphertext using Caesar Cipher.
    """

    def __init__(self, text, key):
        """
        Initializes the Caesar_cipher object with the provided plaintext and key.

        Args:
        - text (str): The plaintext to be encrypted or the ciphertext to be decrypted.
        - key (int): The key used for encryption or decryption. It represents the shift value.
        """
        self.key = key
        self.text = text.upper()
        self.li_enc = None
        self.li_dec = None
        self.cipher_text = ""
        self.decrypt_text = ""

    def encryption(self):
        """
        Encrypts the plaintext using Caesar Cipher.

        Returns:
        None
        """
        self.li_enc = [ord(i) - 65 for i in self.text]
        self.li_enc = [(i + self.key) % 26 for i in self.li_enc]
        for i in self.li_enc:
            self.cipher_text += chr(i + 65)

    def decryption(self):
        """
        Decrypts the ciphertext using Caesar Cipher.

        Prints the list of decrypted values before constructing the decrypted text.

        Returns:
        None
        """
        self.li_dec = [(i - self.key) % 26 for i in self.li_enc]
        #print(self.li_dec)
        for i in self.li_dec:
            self.decrypt_text += chr(i + 65)

a = Caesar_cipher("Muthu",4)
a.encryption()
print(f"Cipher Text: {a.cipher_text}")
a.decryption()
print(f"Decrpyt Text: {a.decrypt_text}")
