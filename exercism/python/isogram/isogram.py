def is_isogram(string):
    res=True
    cleaned_text = ''.join(char for char in string if char.isalpha())
    cleaned_text = cleaned_text.lower()
    for i in cleaned_text:
        if cleaned_text.count(i) > 1:
            res=False
            break
    return res

print(is_isogram("eleven"))