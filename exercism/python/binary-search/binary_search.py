def find(search_list, value):
    _l = 0
    _r = len(search_list) - 1  # правая граница включительно

    while _l <= _r:
        i = _l + (_r - _l) // 2
        if search_list[i] == value:
            return i
        elif value < search_list[i]:
            _r = i - 1
        else:
            _l = i + 1

    raise ValueError("value not in array")