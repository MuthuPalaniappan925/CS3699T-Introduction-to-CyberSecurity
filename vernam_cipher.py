class vernam_cipher:
    """
    Vernam_cipher class for implementing Vernam Cipher encryption and decryption.

    Attributes:
    - text (str): The plaintext to be encrypted or the ciphertext to be decrypted.
    - key (str): The key used for encryption or decryption.
    - li_text (list): List of integer values representing the ASCII values of characters in the text.
    - li_key (list): List of integer values representing the ASCII values of characters in the key.
    - li_cipher (list): List of integer values representing the ASCII values of characters in the encrypted text.
    - li_dec (list): List of characters representing the decrypted text.
    - cipher_text (str): The result of the encryption process.
    - decrypt_text (str): The result of the decryption process.

    Methods:
    - encryption(): Encrypts the plaintext using Vernam Cipher.
    - decryption(): Decrypts the ciphertext using Vernam Cipher.
    - test(): Prints the plaintext and key for testing purposes.
    """
    def __init__(self,text,key):
        """
        Initializes the object with the provided plaintext and key.

        Args:
        - text (str): The plaintext to be encrypted or the ciphertext to be decrypted.
        - key (str): The key used for encryption or decryption.
        """
        self.text = text.upper()
        self.key = key.upper()
        self.li_text = [ord(i)-65 for i in self.text]
        self.li_key = [ord(j)-65 for j in self.key]
        self.li_cipher = None
        self.li_dec = None
        self.cipher_text = ""
        self.decryp_text = ""
    
    def encrpytion(self):
        """
        Encrypts the plaintext using Vernam Cipher.

        If the length of the plaintext and key are not equal, a message is printed indicating the mismatch.

        Returns:
        None
        """
        if len(self.text) == len(self.key):
            self.li_cipher = [(i+j) if (i+j) < 26 else (i+j) - 26 for i,j in zip(self.li_text,self.li_key)]
            for i in self.li_cipher:
                self.cipher_text+=chr(i+65)
        else:
            print(f"Key: {self.key} and text: {self.text} are in different shape")
    
    def decryption(self):
        """
        Decrypts the ciphertext using Vernam Cipher.

        If the ciphertext is not available (None), decryption is not performed.

        Returns:
        None
        """
        if(self.li_cipher)!=None:
            self.li_dec = [chr((i-j)+65) if (i-j) >=0 else chr((i-j)+26+65) for (i,j) in zip(self.li_cipher,self.li_key)]
            if(self.li_dec)!=None:
                self.decryp_text = "".join(self.li_dec)
    
    def test(self):
        """
        Prints the plaintext and key for testing purposes.

        Returns:
        None
        """
        print(self.text,self.key)

##Driver Code
a = vernam_cipher("Muthu","Pitch")
##Encryption
a.encrpytion()
print(f"Cipher Text: {a.cipher_text}")
##Decryption
a.decryption()
print(f"Decrypt Text: {a.decryp_text}")
