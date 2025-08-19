"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*wagons):
    return list(wagons)

def fix_list_of_wagons(each_wagons_id, missing_wagons):
    a,b, one, *c = each_wagons_id
    return  [one] + missing_wagons + c + [a] + [b]

def add_missing_stops(dist, **stops):
    sorted_stops = [value for _, value in sorted(stops.items())]
    dist["stops"] = sorted_stops
    return dist
    
def extend_route_information(route, more_route_information):
    return {**route, **more_route_information}

def fix_wagon_depot(wagons_rows):
    return [list(row) for row in zip(*wagons_rows)]
