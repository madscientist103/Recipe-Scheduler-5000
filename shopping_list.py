from collections import Counter
import usual_items

# add ingredients for all recipes in this function

# create a list of grocery items for purchase
# check which recipes are on the weekly schedule
# add the regular items if needed
# add the ingredients based on the recipes on schedule. 
def create_shopping_list(recipe_book, output_file):

    # create the shopping list
    shopping_list = []

    # check if we should add the usual items
    print("Would you also like to add your usual items to the shopping list  for the week?\n")
    print("1 - Yes")
    print("2 - No")
    usual_shopping_selection = int(input("Choose 1 or 2\n"))

    if (usual_shopping_selection == 1):

        print("Adding usual shopping items to the list!\n")

        with open(output_file, "a") as f:
            f.write("\nAdding usual shopping items to the list!\n")

        shopping_list = usual_items.add_usual_items(shopping_list)

    #iterate through the recipe book and add ingredients
    for recipe in recipe_book[:7]:

        if (recipe["name"] == "tacos"):

            shopping_list.append("meat - ground beef or turkey")
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

            shopping_list.append("meat - ground beef or turkey")
            shopping_list.append("meat - spicy italian sausage (optional)")
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

            shopping_list.append("meat - ground beef or turkey")
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

        elif (recipe["name"] == "mac and hot dogs"):

            shopping_list.append("meat - beef hot dogs")
            shopping_list.append("box - mac")
            shopping_list.append("bread - hot dog buns")
            shopping_list.append("frozen - vegetable")
            shopping_list.append("condiment - ketchup")
            shopping_list.append("condiment - mustard")
            shopping_list.append("topping - chili sauce (optional)")
            shopping_list.append("topping - diced onion (optional)")

        elif (recipe["name"] == "stroganoff"):

            shopping_list.append("meat - ground beef")
            shopping_list.append("pasta - egg noodles")
            #shopping_list.append("")
            #shopping_list.append("")
            #shopping_list.append("")
            #shopping_list.append("")
            #shopping_list.append("")
            #shopping_list.append("")
            
        elif (recipe["name"] == "chicken parmesan in the crockpot"):

            shopping_list.append("meat - chicken")
            #shopping_list.append("")
            #shopping_list.append("")
            #shopping_list.append("")
            #shopping_list.append("")
            #shopping_list.append("")
            #shopping_list.append("")
            #shopping_list.append("")

        elif (recipe["name"] == "wet burritoes"):

            shopping_list.append("meat - ground beef")
            #shopping_list.append("")
            #shopping_list.append("")
            #shopping_list.append("")
            #shopping_list.append("")
            #shopping_list.append("")
            #shopping_list.append("")
            #shopping_list.append("")

        elif (recipe["name"] == "buffalo/bbq chicken tacos"):

            shopping_list.append("meat - chicken")
            #shopping_list.append("")
            #shopping_list.append("")
            #shopping_list.append("")
            #shopping_list.append("")
            #shopping_list.append("")
            #shopping_list.append("")
            #shopping_list.append("")

        elif (recipe["name"] == "chicken and rice in the crockpot"):

            shopping_list.append("meat - chicken")
            #shopping_list.append("")
            #shopping_list.append("")
            #shopping_list.append("")
            #shopping_list.append("")
            #shopping_list.append("")
            #shopping_list.append("")
            #shopping_list.append("")

        elif (recipe["name"] == "chili in the crockpot"):

            shopping_list.append("meat - ground beef")
            #shopping_list.append("")
            #shopping_list.append("")
            #shopping_list.append("")
            #shopping_list.append("")
            #shopping_list.append("")
            #shopping_list.append("")
            #shopping_list.append("")

        elif (recipe["name"] == "cottage pie"):

            shopping_list.append("meat - ground beef or turkey")
            #shopping_list.append("")
            #shopping_list.append("")
            #shopping_list.append("")
            #shopping_list.append("")
            #shopping_list.append("")
            #shopping_list.append("")
            #shopping_list.append("")

        elif (recipe["name"] == "ravioli"):

            shopping_list.append("meat - ground beef or turkey")
            #shopping_list.append("")
            #shopping_list.append("")
            #shopping_list.append("")
            #shopping_list.append("")
            #shopping_list.append("")
            #shopping_list.append("")
            #shopping_list.append("")

        elif (recipe["name"] == "shrimp alfredo"):

            shopping_list.append("meat - frozen shrimp")
            #shopping_list.append("")
            #shopping_list.append("")
            #shopping_list.append("")
            #shopping_list.append("")
            #shopping_list.append("")
            #shopping_list.append("")
            #shopping_list.append("")

    #initial approach is to rempove duplicates from the list//
    #decided in favor of counting the number of recipes per ingredient

    #unique_shopping_list = list(set(shopping_list))

    #create a counter object to tally the number of unique ingredients
    shopping_list_counts = Counter(shopping_list)

    return shopping_list_counts