"""Functions for compiling dishes and ingredients for a catering company."""


from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
    return (dish_name, set(dish_ingredients))

def check_drinks(drink_name, drink_ingredients):
    for drink in drink_ingredients:
        if drink in ALCOHOLS:
            return f"{drink_name} Cocktail"
    return  f"{drink_name} Mocktail"
    
def categorize_dish(dish_name, dish_ingredients):
    """dfDFD"""
    if dish_ingredients.issubset(VEGAN):
        return f"{dish_name}: VEGAN"
    if dish_ingredients.issubset(VEGETARIAN):
        return f"{dish_name}: VEGETARIAN"
    if dish_ingredients.issubset(KETO):
        return f"{dish_name}: KETO"
    if dish_ingredients.issubset(PALEO):
        return f"{dish_name}: PALEO"
    if dish_ingredients.issubset(OMNIVORE):
        return f"{dish_name}: OMNIVORE"
    return None

def tag_special_ingredients(dish):
    name, ingredient = dish
    ingtid_alirg = set()
    for product in ingredient:
        if product in SPECIAL_INGREDIENTS:
            ingtid_alirg.add(product)
    return (name, set(sorted(list(ingtid_alirg))))

def compile_ingredients(dishes):
    list_ingr =set()
    for dishe in dishes:
        for ingr in dishe:
            list_ingr.add(ingr)

    return list_ingr
    
def separate_appetizers(dishes, appetizers):
    res = set()
    for dishe in dishes:
        if dishe not in appetizers:
            res.add(dishe)
    return list(res)

def singleton_ingredients(dishes, intersection):
    all_ingr = set().union(*dishes)
    res = all_ingr - intersection
    return res