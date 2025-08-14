"""Functions to keep track and alter inventory."""

def create_inventory(items):
    new_dict = dict()
    for i in items:
        count = items.count(i)
        if i not in new_dict:
            new_dict[i] = count
    return new_dict

def add_items(inventory, items):
    for i in items:
        if i in inventory:
            inventory[i] += 1 
        else:
            inventory[i] =  1 
    return inventory

def decrement_items(inventory, items):
    for i in items:
        if i in inventory and inventory[i] > 0:
            inventory[i] -= 1 
    return inventory

def remove_item(inventory, item):
    if item in inventory:
        inventory.pop(item)
    return inventory

def list_inventory(inventory):
    result_list = []

    for i in inventory:
        if inventory[i] > 0:
            result_list.append((i, inventory[i]))

    return result_list

