from collections import Counter

def create_shopping_list(recipe_book):

    shopping_list = []

    for recipe in recipe_book[:7]:

        if (recipe["name"] == "tacos"):

            shopping_list.append("meat - ground beef")
            shopping_list.append("taco shells - crunchy or corn tortillas")
            shopping_list.append("taco shells - soft flour tortillas")
            shopping_list.append("seasoning - taco")
            shopping_list.append("dairy - sour cream")
            shopping_list.append("topping - taco sauce")
            shopping_list.append("topping - salsa")
            shopping_list.append("topping - queso")
            shopping_list.append("cheese - shredded fiesta or cheddar")
            shopping_list.append("vegetable - onion")
            shopping_list.append("vegetable - lettuce")
            shopping_list.append("vegetable - tomato")

        elif (recipe["name"] == "spaghetti in the crockpot"):

            shopping_list.append("meat - ground beef")
            shopping_list.append("pasta - spaghetti")
            shopping_list.append("sauce - spaghetti/marinara")
            shopping_list.append("frozen - garlic bread")
            shopping_list.append("topping - parmesan/romano cheese")
            shopping_list.append("seasoning - red pepper")
            shopping_list.append("can - diced tomatoes")
            shopping_list.append("can - mushrooms")

        elif (recipe["name"] == "meatloaf in the crocpot"):

            shopping_list.append("meat - ground beef")
            shopping_list.append("dairy - eggs")
            shopping_list.append("dairy - milk")
            shopping_list.append("baking - italian bread crumbs")
            shopping_list.append("seasoning - salt")
            shopping_list.append("seasoning - pepper")
            shopping_list.append("seasoning - italian")
            shopping_list.append("seasoning - oregano")
            shopping_list.append("baking - brown sugar")
            shopping_list.append("condiment - ketchup")
            shopping_list.append("seasoning - parsley")
            shopping_list.append("seasoning - tajin")
            shopping_list.append("seasoning - garlic powder")
            shopping_list.append("seasoning - onion powder")
            shopping_list.append("seasoning - beef boullion")

        elif (recipe["name"] == "hamburger helper"):

            shopping_list.append("meat - ground beef")
            shopping_list.append("box - hamburger helper / velveeta skillet")
            shopping_list.append("dairy - milk")
            shopping_list.append("frozen - garlic bread")
            shopping_list.append("frozen - vegetable")
            shopping_list.append("seasoning - garlic powder")
            shopping_list.append("seasoning - onion powder")
            shopping_list.append("seasoning - beef boullion")
            shopping_list.append("seasoning - salt")
            shopping_list.append("seasoning - pepper")
            shopping_list.append("seasoning - italian")

    #initial approach is to rempove duplicates from the list//
    #decided in favor of counting the number of recipes per ingredient

    #unique_shopping_list = list(set(shopping_list))

    #create a counter object to tally the number of unique ingredients
    shopping_list_counts = Counter(shopping_list)

    return shopping_list_counts