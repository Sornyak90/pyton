class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        result = False
        num = self.card_num.replace(" ","")
        if len(num) > 1 and num.isdigit():
            str_num = list(map(int,num))
            for i in range(len(str_num)-2,-1,-2):
                str_num[i]*=2
                if str_num[i] > 9:
                    str_num[i]-= 9
            sum_num = sum(str_num) 
            if sum_num % 10 == 0 : result = True  
        return result
