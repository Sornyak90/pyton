"""Functions to help Azara and Rui locate pirate treasure."""
def get_coordinate(record):
    return record[1]

def convert_coordinate(coordinate):
    mulstr = tuple(coordinate) 
    return (mulstr[0],mulstr[1])

def compare_records(azara_record, rui_record):
    mulstr1 = tuple(azara_record) 
    mulstr2 = tuple(rui_record) 
    return tuple(mulstr1[1]) == mulstr2[1]
    
def create_record(azara_record, rui_record):
    if tuple(azara_record[1]) == rui_record[1]:
        res = azara_record + rui_record
    else:
        res = "not a match"

    return res

def clean_up(combined_record_group):
    return '\n'.join(repr((record[0], record[2], record[3], record[4])) 
           for record in combined_record_group) + '\n'
