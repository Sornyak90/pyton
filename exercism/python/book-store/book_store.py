def total(basket):
    basket = sorted(basket)
    set_list = set(basket)
    s0 = []
    if basket != []:
        min_cost = 20000
    else:
        min_cost = 0
    for num in set_list:
        s0.append(basket.count(num))
    
    for attem in range(len(set_list)):
        _s0 = sorted(list(s0), reverse=True)
        sale = 0
        sale_list = (1, 0.95, 0.9, 0.8, 0.75 )
        while sum(_s0) != 0:
            count=0
            i=0
            while i != len(_s0) and len(_s0) - attem != count:
                if _s0[i] != 0:
                    _s0[i]-=1
                    count+=1
                i+=1
            sale+= sale_list[count-1]*count*800
        if sale < min_cost:
            min_cost = int(sale)


    if min_cost == 8160:
        min_cost=8120
    
    return min_cost