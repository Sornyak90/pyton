def rotate(text, key):
    text_new = ''
    for ch in text:
        if not ch.isalpha():
            text_new+=ch
        else:
            if 65 <= ord(ch) <= 90: #A-Z
                if ord(ch) + key > 90:
                    ch = chr(ord(ch) - 26)
            elif 97 <= ord(ch) <= 122: #a-z
                if ord(ch) + key > 122:
                    ch = chr(ord(ch) - 26)
            text_new+=chr(ord(ch) + key)
    return text_new

        
