def abbreviate(words):
    abbr = []
    words = words.replace('-', ' ').replace('_', ' ').split()
    for i in  words:
        abbr+=i[0].upper()
    return ''.join(abbr)