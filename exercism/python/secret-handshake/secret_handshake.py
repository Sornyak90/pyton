def commands(binary_str):
    code_word = ["", "jump", "close your eyes", "double blink", "wink"]
    return [w for i, w in enumerate(code_word[1:], 1) if int(binary_str[i])][::1 if int(binary_str[0]) else -1]