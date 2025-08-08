def rows(letter):
    inx = 2 * (ord(letter) - 65) + 1
    cent = inx // 2
    n_l = cent
    n_r = cent
    result = []

    for i in range(cent+1):
        list1 = list(" " * inx)
        list1[n_l] = chr(65 + i)
        list1[n_r] = chr(65 + i)
        n_l-=1
        n_r+=1
        str1 = "".join(i for i in list1)
        result.append(str1)
    for i in result[-2::-1]:
        result.append(i)

    return result
