def flatten(iterable):
    result = []
    for item in iterable:
        if isinstance(item,int):
            result.append(item)
        elif isinstance(item, list):
            result+=flatten(item)
        elif item == None:
            continue
            
    return result
