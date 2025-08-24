def say(number):
   
    
    result = []
    digit = number
   
    if digit == 0:
        return "zero"
    if digit == 1000000000000 or digit < 0:
        raise ValueError("input out of range")

    if digit >= 1000000000:
        num = digit // 1000000000
        digit-=1000000000*num
        num = hundred(num)
        result.append(num+" billion")
    if digit >= 1000000:
        num = digit // 1000000
        digit-=1000000*num
        num = hundred(num)
        result.append(num+" million")
    if digit >= 1000:
        num = digit // 1000
        digit-=1000*num
        num = hundred(num)
        result.append(num +" thousand")
    if 1 <= digit < 1000:
       result.append(hundred(digit))
    result = ' '.join(result)
    return result

def hundred(number):
    number_words = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
        6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
        11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
        16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty",
        30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy",
        80: "eighty", 90: "ninety"
    }




    digit = number
    result = []
    if digit >= 100:
        num = digit // 100
        digit-=100*num
        result.append(number_words[num]+" hundred")
    if digit > 20:
        num = digit - (digit % 10)
        result.append(number_words[num])
        digit = digit % 10
    if 0 < digit <= 20:
        result.append(number_words[digit])

    result = ' '.join(result)
    if (21 <= number%100 <= 99) and number % 10 != 0:
        parts = result.rsplit(' ', 1) 
        result = '-'.join(parts)
    return result
    
print(say(171))   