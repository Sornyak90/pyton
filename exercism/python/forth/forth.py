class StackUnderflowError(Exception):
    def __init__(self, message):
        self.message = message

def arithmetic(stack, token):
    if len(stack) >= 2:  
        b = stack.pop()  
        a = stack.pop()  
        if str(a).isdecimal and str(b).isdecimal:
            if token == "+":
                result = a + b
            if token == "-":
                result = a - b 
            if token == "*":
                result = a * b 
            if token == "/":
                if b != 0:
                    result = a // b
                else:
                    raise ZeroDivisionError("divide by zero")    
        else: 
            raise StackUnderflowError("Insufficient number of items in stack")
        stack.append(result)
    else:
        raise StackUnderflowError("Insufficient number of items in stack")

    return stack 

def manipulation(stack, token):
    if token == "dup":
        if len(stack) >= 1:
            a = stack.pop()
            stack.append(a)
            stack.append(a) 
        else:
            raise StackUnderflowError("Insufficient number of items in stack")
    if token == "drop":
        if len(stack) >= 1:
            stack.pop()
        else:
            raise StackUnderflowError("Insufficient number of items in stack")
    if token == "swap":
        if len(stack) >= 2:
            b = stack.pop()
            a = stack.pop()
            stack.append(b)
            stack.append(a) 
        else:
            raise StackUnderflowError("Insufficient number of items in stack")
    if token == "over":
        if len(stack) >= 2:
            a = stack[-2]
            stack.append(a) 
        else:
            raise StackUnderflowError("Insufficient number of items in stack")

    return stack 

def definition(input_data):
    defin = {}
    val = []
    for data in input_data:
        tokens = list(data.lower().split())
        if tokens[0] == ":":
            tokens.remove(":")
            if tokens[0].lstrip("-").isdigit():
                raise ValueError("illegal operation")
            key = tokens[0]
            val = []
            del tokens[0]
            for value in tokens:
                if value in defin:
                    value = defin[value][0]               
                if value != ";":
                    val.append(value)
            defin[key] = val
        else:
            for i in reversed(range(len(tokens))):
                if tokens[i] in defin:
                    tokens[i:i+1] = defin[tokens[i]]
    return tokens
            
       
                    
                    



def evaluate(input_data):
    status = False
    for data in input_data:
        tokens = list(data.lower().split())
        arithm = ("+-*/")
        manip = ("dup", "drop", "swap", "over")
        stack = [] 
        
        for token in tokens:
            if token.lstrip('-').isdigit():  
                stack.append(int(token)) 
            elif token in arithm:
                stack = arithmetic(stack, token)
            elif token in manip:
                stack = manipulation(stack, token)
            elif token == ":":
                stack = definition(input_data)
                stack = ' '.join(stack)
                stack = evaluate(([stack]))
                status = True
                break
            else:
                raise ValueError("undefined operation")
        if status:
            break        
    return stack


    
    

print(evaluate([": SWAP DUP Dup dup ;", "1 swap"]))