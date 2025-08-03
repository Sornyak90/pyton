def response(hey_bob):
    hey_bob_stripped = hey_bob.strip()  
    is_shouting = hey_bob_stripped.isupper()  
    is_question = hey_bob_stripped.endswith('?') if hey_bob_stripped else False  
    
    if not hey_bob_stripped:  
        return "Fine. Be that way!"
    elif is_shouting and is_question: 
        return "Calm down, I know what I'm doing!"
    elif is_shouting: 
        return "Whoa, chill out!"
    elif is_question: 
        return "Sure."
    else:  
        return "Whatever."