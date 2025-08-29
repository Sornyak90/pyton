def cipher_text(plain_text):
    plain_text = list(plain_text.lower())
    text = [ch for ch in plain_text if ch.isalnum()]
    text = str(''.join(text))

    if text == "":
        return ""

    status = False
    for r in range(1,len(text)+1):
        for c in range(1,len(text)+1):
            if ((r*c >= len(text)) and (c >= r) and (c-r<=1)):
                status = True
                break
        if status:
            break
    ch=0
    res_text = [[] for i in range(c)]
    for j in range(r):
        for i in range(c):
            if(ch < len(text)):
                res_text[i].append(text[ch])
                ch+=1
            else:
                res_text[i].append(" ")
                ch+=1

            

    return ' '.join(''.join(text) for text in res_text)



