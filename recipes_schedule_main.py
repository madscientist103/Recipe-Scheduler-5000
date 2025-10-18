#import random
#from collections import Counter
import day_logic_handler
import recipe_book
import shopping_list
import usual_items
from datetime import datetime


#Current limitations and future improvements://
#Cannot account for "leftovers" days as many recipes will//
#provide dinner for a second night.
#Also, it would be nifty to include quantities/amounts for//
#the shopping list instead of just "number of dinners".
#Could eventually include a more advanced UI which will provide//
#the user options for customization of the schedule and/or ability//
#to update their recipe books and shopping lists. 

def main():
    
    #create a new file name for output based on the timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"recipe_schedule_{timestamp}.txt"

    #intro to user - outout to terminal and file
    print("\n\nWelcome to the Recipe Scheduler 5000! :) \n")
    print("Designed to take the stress out of deciding what to have for dinner for the week!\n")

    with open(output_file, "w") as f:
        f.write("\n\nWelcome to the Recipe Scheduler 5000! :) \n")
        f.write("\nDesigned to take the stress out of deciding what to have for dinner for the week!\n")

    #instantiate a new recipe book
    my_recipe_book = recipe_book.create_recipe_book()

    #instantiate a new shopping list
    my_shopping_list = shopping_list.create_shopping_list(my_recipe_book, output_file)

    print("\nThis week's meal schedule has been generated:\n")

    with open(output_file, "a") as f:
        f.write("\nThis week's meal schedule has been generated:\n")

    

    #check current day of the week
    today = datetime.now()


    # Get the abbreviated day name
    day_name_abbreviated = today.strftime("%a")
    #print(day_name_abbreviated)

    #check which schedule to print
    if day_name_abbreviated == "Sun":

        day_logic_handler.today_is_sunday(my_recipe_book, output_file)

    elif day_name_abbreviated == "Mon":

        day_logic_handler.today_is_monday(my_recipe_book, output_file)

    elif day_name_abbreviated == "Tue":

        day_logic_handler.today_is_tuesday(my_recipe_book, output_file)

    elif day_name_abbreviated == "Wed":

        day_logic_handler.today_is_wednesday(my_recipe_book, output_file)

    elif day_name_abbreviated == "Thu":

        day_logic_handler.today_is_thursday(my_recipe_book, output_file)

    elif day_name_abbreviated == "Fri":

        day_logic_handler.today_is_friday(my_recipe_book, output_file)

    elif day_name_abbreviated == "Sat":

        day_logic_handler.today_is_saturday(my_recipe_book, output_file)

  
    print("________\n")
    print("Shopping List and Recipe Count per Item: \n")

    with open(output_file, "a") as f:
        f.write("\n________\n")
        f.write("\nShopping List and Recipe Count per Item: \n")
    

    for item, count in sorted(my_shopping_list.items()):
        
        print(f"{item}: {count}")

        with open(output_file, "a") as file:
            file.write("\n")
            file.write((f"{item}: {count}"))

    print("\nFinished!! :)\n")
    
    with open(output_file, "a") as f:
        f.write("\n\nFinished!! :)\n")

main()