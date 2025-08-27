class PhoneNumber:
    def __init__(self, number):
        self._number = self._clean_and_validate_number(number)

    def _clean_and_validate_number(self, number):
        for num in number: 
            if num.isalpha():
                raise ValueError("letters not permitted")
            elif num in "@:!":
                raise ValueError("punctuations not permitted")

        clean_number = ''.join(num for num in number if num.isdigit())
        
        # Проверка длины номера
        if len(clean_number) < 10:
            raise ValueError("must not be fewer than 10 digits")
        elif len(clean_number) > 11:
            raise ValueError("must not be greater than 11 digits")
        elif len(clean_number) == 11:
            if clean_number[0] != "1":
                raise ValueError("11 digits must start with 1")
            clean_number = clean_number[1:]  # Убираем ведущую 1 для дальнейших проверок
        
        # Проверка кода зоны (первые 3 цифры)
        if clean_number[0] == '0':
            raise ValueError("area code cannot start with zero")
        elif clean_number[0] == '1':
            raise ValueError("area code cannot start with one")
        
        # Проверка кода обмена (следующие 3 цифры, позиции 3-5)
        if clean_number[3] == '0':
            raise ValueError("exchange code cannot start with zero")
        elif clean_number[3] == '1':
            raise ValueError("exchange code cannot start with one")

        return clean_number
   
    @property
    def number(self):
        return self._number
    @property
    def area_code(self):
        return self._number[0:3]

    def pretty(self):
        return f"({self.number[:3]})-{self.number[3:6]}-{self.number[6:]}"
