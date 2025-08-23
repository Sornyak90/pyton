"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    for i in range(number):
        inx = i % 4
        yield chr(65+inx)



def generate_seats(number):
    for i in range(number):
        inx = i % 4
        num = i // 4
        if num > 11:
            num+=1
        yield str(1 + num) + chr(65+inx)

def assign_seats(passengers):
    len_=len(passengers)
    bilet = list(generate_seats(len_))
    result = {}
    for i in range(len_):
        result[passengers[i]] = bilet[i]
    return result
    # как сделать yield
   

def generate_codes(seat_numbers, flight_id):
   for number in seat_numbers:
    len_seat_num = len(number)
    len_flight = len(flight_id)
    zero = 12 - len_seat_num - len_flight
    yield (number + flight_id + "0"*zero)



a = list(generate_codes(["12A", "38B", "69C", "102B"],"KL1022"))
print(a)