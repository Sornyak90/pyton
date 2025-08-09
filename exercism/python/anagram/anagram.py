def find_anagrams(word, candidates):
    res = True
    result = []
    for row in candidates:
        row_list = list(row.lower())
        for i in word.lower():
            if i in row_list:
                row_list.remove(i)
                res = True
                continue
            else:
                res = False
                break
        else:
            if res and row.lower() != word.lower() and len(row) == len(word) and len(row_list) < 1:
                result.append(row)
    return result

candidates = ["Banana"]
print(find_anagrams("BANANA", candidates))