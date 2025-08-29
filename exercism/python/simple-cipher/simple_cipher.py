import random
class Cipher:
    def __init__(self, key=None):
        alphbit = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.key = key if key != None else random.choice(alphbit)*100

    def encode(self, text):
        key = list(self.key)
        result=[]
        i=len(key)-1
        for ch in text:
            i=0 if i==len(key)-1 else i+1
            a=ord(ch) + (ord(key[i]) - 97)
            if a > 122:
                a-=26
           
            result.append(chr(a))
        return str(''.join(result))

    def decode(self, text):
        key = list(self.key)
        result=[]
        i=len(key)-1
        for ch in text:
            i=0 if i==len(key)-1 else i+1
            a=ord(ch) - (ord(key[i])- 97)
            if a < 97:
                a += 26
           
            result.append(chr(a))
        return str(''.join(result))
