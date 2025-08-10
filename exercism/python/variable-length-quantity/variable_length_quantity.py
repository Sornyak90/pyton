def encode(numbers):
    result = []
    for number in numbers:
        parts = []
        while True:
            part = number & 0x7F  # Берем младшие 7 бит
            number >>= 7          # Сдвигаем число на 7 бит вправо
            if number > 0:
                part |= 0x80      # Устанавливаем флаг продолжения
            parts.append(part)
            if number == 0:
                break
        result.extend(reversed(parts))  # Добавляем байты в правильном порядке
    return result

def decode(bytes_):
    result = []
    current = 0
    for byte in bytes_:
        current = (current << 7) | (byte & 0x7F)
        if not (byte & 0x80):  # Если флаг продолжения не установлен
            result.append(current)
            current = 0
    if current != 0:
        raise ValueError("incomplete sequence")
    return result