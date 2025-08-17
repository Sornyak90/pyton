def count_words(sentence):
    list_str = ""
    dict_str = {}
    length = len(sentence)

    for ch in range(length):
        char = sentence[ch]
        if char.isalnum() or char == " ":
            list_str += char
        elif char == "'":
            if 0 < ch < length - 1 and sentence[ch + 1] in 'stre' and sentence[ch - 1].isalnum():
                list_str += char
            else:
                list_str += " "
        else:
            list_str += " "

            
    list_str = list_str.strip().lower()
    list_str = list_str.split(" ")
    list_str = [item for item in list_str if item.strip()]
    for word in list_str:
        dict_str[word] = dict_str.get(word, 0) + 1
    return dict_str


print(count_words("'First: don't laugh. Then: don't cry. You're getting it.'"))
