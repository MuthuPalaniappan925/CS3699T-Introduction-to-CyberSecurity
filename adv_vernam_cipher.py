def adv_enc_vernam(text,key):
    encrypted_message = ''.join(chr(ord(m) ^ ord(k)) for m, k in zip(text, key))
    return encrypted_message

def adv_dec_vernam(cipher,key):
    decrypted_message = ''.join(chr(ord(m) ^ ord(k)) for m, k in zip(cipher, key))
    return decrypted_message

text = "muthu"
key = "honey"

en_txt = adv_enc_vernam(text,key)
print(en_txt)
dec_txt = adv_dec_vernam(en_txt,key)
print(dec_txt)
