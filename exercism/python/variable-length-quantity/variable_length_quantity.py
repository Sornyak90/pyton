import sys


def encode(numbers):
    res_number = []
    for number in reversed(numbers):
        from_decimal = 0
        decimal = number
        binary = []
        # dic -> bite
        while decimal >= 2:
            remains = decimal % 2
            from_decimal = int(decimal / 2)
            binary.insert(0, remains)
            decimal = from_decimal
        else:
            binary.insert(0, from_decimal)

        # count array
        count_array = len(binary) / 7
        # if count_array <= 7 : count_array = 2
        _count_array = int(count_array)
        if _count_array < count_array:
            count_array = int(_count_array + 1)

        #  add 0 binary[]
        len_n = int(8 * count_array - len(binary))
        if len(binary) < 8:
            len_n = 0
        for i in range(len_n):
            binary.insert(0, 0)

        # VLQ
        number = []
        for i in range(len(binary) - 7, -1, -7):
            if i != len(binary) - 7:
                tmp_array = binary[i : i + 7]
                tmp_array.insert(0, 1)
            else:
                tmp_array = binary[i : i + 7]
                tmp_array.insert(0, 0)

            degree = 0
            num = 0
            for i in reversed(tmp_array):
                num += i * 2**degree
                degree += 1

            number.insert(0, num)

        if len(binary) == 1 and binary[0] == 0:
            res_number.insert(0, 0)

        for i in reversed(number):
            res_number.insert(0, i)

    return res_number


def decode(bytes_):

    if len(bytes_) == 1 and (bytes_[0] & 0x80) != 0:
        raise ValueError("incomplete sequence")
    
    bit = []
    flag_end = False
    result = []
    for number in bytes_:
        if number != 0:
            from_decimal = 0
            decimal = number
            binary = []
            # dic -> bite
            while decimal >= 2:
                remains = decimal % 2
                from_decimal = int(decimal / 2)
                binary.insert(0, remains)
                decimal = from_decimal
            else:
                binary.insert(0, from_decimal)
        else:
            binary = [0] * 8

        n = len(binary)
        if n < 8:
            for i in range(8 - n):
                binary.insert(0, 0)
        if binary[0] == 0:
            flag_end = True
        bit += binary[1:]

        if flag_end:
            degree = 0
            num = 0
            from_decimal = 0
            for i in reversed(bit):
                num += i * 2**degree
                degree += 1

            binary.clear()
            while num >= 16:
                remains = num % 16
                from_decimal = int(num / 16)
                binary.insert(0, remains)
                num = from_decimal
            else:
                binary.insert(0, from_decimal)

            hex_digit = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
            num_str = "".join(
                str(hex_digit[i]) if i in hex_digit else str(i) for i in binary
            )
            hex_str = int(f"0x{num_str}", 16)
            result.append(hex_str)
            flag_end = False
            bit.clear()

    return result
