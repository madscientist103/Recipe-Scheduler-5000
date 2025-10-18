import random

# add your recipes here!
# also  make sure to add the  ingrtedients for any added recipes//
# //in the create_shopping_list function!

def create_recipe_book():

    recipe_book = [
    {"name": "tacos", "complexity": "low", "time": "30 minutes"},
    {"name": "spaghetti in the crockpot", "complexity": "low", "time": "6 hours"},
    {"name": "meatloaf in the crockpot", "complexity": "medium", "time": "6 hours"},
    {"name": "hamburger helper", "complexity": "low", "time": "30 minutes"},
    {"name": "mac and hot dogs", "complexity": "low", "time": "30 minutes"},
    {"name": "stroganoff", "complexity": "low", "time": "30 minutes"},
    {"name": "chicken parmesan in the crockpot", "complexity": "low", "time": "6 hours"},
    {"name": "wet burritoes", "complexity": "medium", "time": "1 hour"},
    {"name": "buffalo/bbq chicken tacos", "complexity": "high", "time": "1 hour"},
    {"name": "chicken and rice in the crockpot", "complexity": "medium", "time": "6 hours"},
    {"name": "chili in the crockpot", "complexity": "medium", "time": "6 hours"},
    {"name": "cottage pie", "complexity": "medium", "time": "1 hour"},
    {"name": "ravioli", "complexity": "low", "time": "6 hours"},
    {"name": "shrimp alfredo", "complexity": "low", "time": "30 minutes"}

]
    
    # randomize so we don't get the same schedule every run!
    random.shuffle(recipe_book)

    return recipe_book