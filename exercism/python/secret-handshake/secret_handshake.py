def commands(binary_str):
    code_word = [
        " ",
        "jump",
        "close your eyes",
        "double blink",
        "wink"]
    result_list = [code_word[i] for i in range(1,len(binary_str)) if int(binary_str[i])]
    if int(binary_str[0]) == 0: 
        result_list.reverse()
    return result_list




print(commands("00011"))    
    

