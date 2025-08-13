def append(list1, list2):
    return list1 + list2


def concat(lists):
    result = []
    for items in lists:
        for item in items:
            result.append(item) 
        
    return result

def filter(function, list):
    res = []
    for i in list:
        if function(i) : res.append(i)
    return res



def length(list):
    return len(list)


def map(function, list):
    res = []
    for i in list:
        res.append(function(i))
    return res
    


def foldl(function, list, initial):
    res = []
    if list == []:
        list.append(1)
    for i in list:
        res=function(initial,i)
        initial = res
    return res


def foldr(function, list, initial):
    res = []
    if list == []:
        list.append(1)
    for i in reverse(list):
        res=function(initial,i)
        initial = res
    return res


def reverse(list):
    list.reverse()
    return list

