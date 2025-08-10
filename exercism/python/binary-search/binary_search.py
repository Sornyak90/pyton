def find(search_list, value):
    i = len(search_list) // 2 
    _l = 0
    _r = len(search_list)
    if value not in search_list:
        raise ValueError("value not in array")        
        

   
    while search_list[i] != value and  _l < _r:
        if value < search_list[i]:
            _r = i
            i = (_r - _l) // 2
        else:
            _l = i
            i = _l + (_r - _l) // 2
            
    
           

            
    return i

        
        
