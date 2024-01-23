def encrpytion(text,key):
    cipher_text = ""
    text_len = float(len(text))
    li_text = list(text)
    li_key = sorted(list(key))
    
    col = len(key)
    row = int(math.ceil(text_len / col))
    
    li_cipher = []
    fill_null = int((row * col) - text_len)
    li_cipher.extend("_" * fill_null)
    
    matrix = [li_text[i:i+col] for i in range(0,len(li_text),col)]
    
    k_indx = 0
    for _ in range(col):
        cur_indx = key.index(li_key[k_indx])
        cipher_text+="".join([row[cur_indx] for row in matrix])
        k_indx+=1
    
    return cipher_text

def decrypt(cipher,key):
    msg = ""
    k_indx = 0
    msg_indx = 0
    msg_len = float(len(cipher))
    msg_lst = list(cipher)
 
    col = len(key)
    row = int(math.ceil(msg_len / col))
    key_lst = sorted(list(key))
    dec_cipher = []
    for _ in range(row):
        dec_cipher += [[None] * col]
 
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
 
        for j in range(row):
            dec_cipher[j][curr_idx] = msg_lst[msg_indx]
            msg_indx += 1
        k_indx += 1
 
    try:
        msg = ''.join(sum(dec_cipher, []))
    except TypeError:
        raise TypeError("This program cannot",
                        "handle repeating words.")
 
    null_count = msg.count('_')
 
    if null_count > 0:
        return msg[: -null_count]
 
    return msg
