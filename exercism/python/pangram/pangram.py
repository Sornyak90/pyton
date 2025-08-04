def is_pangram(sentence):
    cleaned_text = ''.join(char for char in sentence if char.isalpha())
    alpha = set(cleaned_text.lower())
    return len(alpha) == 26