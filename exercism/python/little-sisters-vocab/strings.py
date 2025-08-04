"""asassss"""
def add_prefix_un(word):
    return 'un' + word


def make_word_groups(vocab_words):
    expected = vocab_words[0]
    for inx in vocab_words[1:]:
        expected+= ' :: ' + vocab_words[0] + inx

    return expected

def remove_suffix_ness(word):
    num = word.find('ness')
    if num != -1:  
        word = word[:num]  
        if num > 0 and word[-1] == 'i':  
            word = word[:-1] + 'y' 
    return word
        
def adjective_to_verb(sentence, index):
    if sentence[-1] == '.':
        sentence=sentence[:-1]
    list_word = sentence.split()
    return list_word[index] + 'en'
