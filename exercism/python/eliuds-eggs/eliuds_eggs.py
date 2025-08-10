def egg_count(display_value):
    decimal = 0
    binary = []
    # dic -> bite
    while display_value >= 2:
        remains = display_value % 2
        decimal = int(display_value / 2)
        binary.insert(0, remains)
        display_value = decimal
    else:
        binary.insert(0, decimal)
    return binary.count(1)