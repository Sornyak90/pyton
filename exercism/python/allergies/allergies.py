class Allergies:

    def __init__(self, score):
        self.score = score
        self.dict_list = {
                    "eggs": 1,
                    "peanuts": 2,
                    "shellfish": 4,
                    "strawberries": 8,
                    "tomatoes": 16,
                    "chocolate": 32,
                    "pollen": 64,
                    "cats": 128
                }

    def allergic_to(self, item):
        result = self.score & self.dict_list[item]
        return result == self.dict_list[item]

    @property
    def lst(self):
        mask = 0b11111111 
        number = self.score
        number = number & mask
        b=[]
        result=[]
        for i in range(8):
            b.append(number & 1)
            number >>= 1        
        i=0
        for key in self.dict_list.keys():
            if b[i] == 1:
                result.append(key)
            i+=1
        return result

