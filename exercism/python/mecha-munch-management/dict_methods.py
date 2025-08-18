"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    for item in items_to_add:
      current_cart[item] = current_cart.setdefault(item, 0) + 1
    return current_cart

def read_notes(notes):
    list_eat = {}
    for item in notes:
      list_eat[item] = list_eat.setdefault(item, 0) + 1
    return list_eat

def update_recipes(ideas, recipe_updates):
    for recipe_name, new_ingredients in recipe_updates:
        print(recipe_name)
        print(new_ingredients)
        ideas[recipe_name] = new_ingredients 
    return ideas

def sort_entries(cart):
    return dict(sorted(cart.items()))

def send_to_store(cart, aisle_mapping):
    updated_items = {}
    
    for item, quantity in cart.items():
        if item in aisle_mapping:
            item_data = aisle_mapping[item].copy()
            item_data.insert(0, quantity) 
            updated_items[item] = item_data
    return dict(sorted(updated_items.items(), reverse=True))
        
def update_store_inventory(fulfillment_cart, store_inventory):
    for k, v in fulfillment_cart.items():
        count_stor = store_inventory[k][0] - v[0]
        if count_stor != 0:
            store_inventory[k][0] = count_stor
        else:
            store_inventory[k][0] = 'Out of Stock'
    return store_inventory