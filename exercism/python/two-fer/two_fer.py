def two_fer(name="you"):
    if name == "you":
        res = "One for you, one for me."
    if name != "you":
        res = "One for " + name + ", one for me."
    return res
