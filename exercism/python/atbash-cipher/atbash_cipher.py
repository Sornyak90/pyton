plain = 'abcdefghijklmnopqrstuvwxyz'
cipher = 'zyxwvutsrqponmlkjihgfedcba'

def encode(plain_text):
    plain_text = [ alnum for alnum in plain_text if alnum.isalnum()]
    ecod = []
    for alnum in plain_text:
        alnum = alnum.lower()
        if alnum.isalpha():
            p_inx = plain.index(alnum)
            ecod.append(cipher[p_inx])
        else:
            ecod.append(alnum)
    
    d = len(ecod) // 5
    inx=5
    for i in range(d):
        ecod.insert(inx, " ")
        inx+=6
        
    return ''.join(i for i in ecod)



def decode(ciphered_text):
    ciphered_text = [ alnum for alnum in ciphered_text if alnum.isalnum()]
    dcod = ''
    for alnum in ciphered_text:
        if alnum.isalpha():
            c_inx = cipher.index(alnum)
            dcod+=plain[c_inx]
        else:
            dcod+=alnum

    return dcod

print(decode("gvhgr mt123 gvhgr mt"))