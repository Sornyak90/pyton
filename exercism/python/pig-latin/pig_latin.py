def translate(text):
    vow = ('a', 'e', 'i', 'o', 'u')
    inx=0
    text_new = list(text.split())
    res=''

    for text in text_new:
        for i in range(len(text)):
            if text[:2] == 'xr' or text[:2] == 'yt':
                return text + 'ay'
    
        inx = 0
        for i in range(len(text)):
            if text[i] in vow or (text[i] == 'y' and i != 0):
                inx = i
                break
            if i < len(text) - 1 and text[i:i+2] == 'qu':
                inx = i + 2
                break
    
        res+=text[inx:] + text[:inx] + 'ay ' 

    return res[:-1]  
