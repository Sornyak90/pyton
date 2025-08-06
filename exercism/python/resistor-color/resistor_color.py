def color_code(color):
    return colors().index(color)


def colors():
    expected = [
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white",
    ]
    return expected


print(color_code("black"))