# might be a better way to do this
# solution for keeping the day names correct //
# // on the printed schedule


def today_is_sunday(recipe_book, output_file):

    day_recipe = recipe_book[0]
    print("_____")
    print("Sunday:")
    print(day_recipe["name"])
    print("Complexity: ", day_recipe["complexity"])
    print("Prep Time: ", day_recipe["time"])
    
    with open(output_file, "a") as f:
        f.write("\n_____")
        f.write("\nSunday:\n")
        f.write(day_recipe["name"])
        f.write("\nComplexity: ")
        f.write(day_recipe["complexity"])
        f.write("\nPrep Time: ")
        f.write(day_recipe["time"])

    day_recipe = recipe_book[1]
    print("_____")
    print("Monday:")
    print(day_recipe["name"])
    print("Complexity: ", day_recipe["complexity"])
    print("Prep Time: ", day_recipe["time"])
    
    with open(output_file, "a") as f:
        f.write("\n_____")
        f.write("\nMonday:\n")
        f.write(day_recipe["name"])
        f.write("\nComplexity: ")
        f.write(day_recipe["complexity"])
        f.write("\nPrep Time: ")
        f.write(day_recipe["time"])

    day_recipe = recipe_book[2]
    print("_____")
    print("Tuesday:")
    print(day_recipe["name"])
    print("Complexity: ", day_recipe["complexity"])
    print("Prep Time: ", day_recipe["time"])
    
    with open(output_file, "a") as f:
        f.write("\n_____")
        f.write("\nTuesday:\n")
        f.write(day_recipe["name"])
        f.write("\nComplexity: ")
        f.write(day_recipe["complexity"])
        f.write("\nPrep Time: ")
        f.write(day_recipe["time"])

    day_recipe = recipe_book[3]
    print("_____")
    print("Wednesday:")
    print(day_recipe["name"])
    print("Complexity: ", day_recipe["complexity"])
    print("Prep Time: ", day_recipe["time"])
    
    with open(output_file, "a") as f:
        f.write("\n_____")
        f.write("\nWednesday:\n")
        f.write(day_recipe["name"])
        f.write("\nComplexity: ")
        f.write(day_recipe["complexity"])
        f.write("\nPrep Time: ")
        f.write(day_recipe["time"])

    day_recipe = recipe_book[4]
    print("_____")
    print("Thursday:")
    print(day_recipe["name"])
    print("Complexity: ", day_recipe["complexity"])
    print("Prep Time: ", day_recipe["time"])
    
    with open(output_file, "a") as f:
        f.write("\n_____")
        f.write("\nThursday:\n")
        f.write(day_recipe["name"])
        f.write("\nComplexity: ")
        f.write(day_recipe["complexity"])
        f.write("\nPrep Time: ")
        f.write(day_recipe["time"])

    day_recipe = recipe_book[5]
    print("_____")
    print("Friday:")
    print(day_recipe["name"])
    print("Complexity: ", day_recipe["complexity"])
    print("Prep Time: ", day_recipe["time"])
    
    with open(output_file, "a") as f:
        f.write("\n_____")
        f.write("\nFriday:\n")
        f.write(day_recipe["name"])
        f.write("\nComplexity: ")
        f.write(day_recipe["complexity"])
        f.write("\nPrep Time: ")
        f.write(day_recipe["time"])

    day_recipe = recipe_book[6]
    print("_____")
    print("Saturday:")
    print(day_recipe["name"])
    print("Complexity: ", day_recipe["complexity"])
    print("Prep Time: ", day_recipe["time"])
    
    with open(output_file, "a") as f:
        f.write("\n_____")
        f.write("\nSaturday:\n")
        f.write(day_recipe["name"])
        f.write("\nComplexity: ")
        f.write(day_recipe["complexity"])
        f.write("\nPrep Time: ")
        f.write(day_recipe["time"])


def today_is_monday(recipe_book, output_file):

    day_recipe = recipe_book[0]
    print("_____")
    print("Monday:")
    print(day_recipe["name"])          
    print("Complexity: ", day_recipe["complexity"])               
    print("Prep Time: ", day_recipe["time"])

    with open(output_file, "a") as f:
        f.write("\n_____")
        f.write("\nMonday:\n")
        f.write(day_recipe["name"])
        f.write("\nComplexity: ")
        f.write(day_recipe["complexity"])
        f.write("\nPrep Time: ")
        f.write(day_recipe["time"])

    day_recipe = recipe_book[1]
    print("_____")
    print("Tuesday:")
    print(day_recipe["name"])
    print("Complexity: ", day_recipe["complexity"])
    print("Prep Time: ", day_recipe["time"])
    
    with open(output_file, "a") as f:
        f.write("\n_____")
        f.write("\nTuesday:\n")
        f.write(day_recipe["name"])
        f.write("\nComplexity: ")
        f.write(day_recipe["complexity"])
        f.write("\nPrep Time: ")
        f.write(day_recipe["time"])

    day_recipe = recipe_book[2]
    print("_____")
    print("Wednesday:")
    print(day_recipe["name"])
    print("Complexity: ", day_recipe["complexity"])
    print("Prep Time: ", day_recipe["time"])
    
    with open(output_file, "a") as f:
        f.write("\n_____")
        f.write("\nWednesday:\n")
        f.write(day_recipe["name"])
        f.write("\nComplexity: ")
        f.write(day_recipe["complexity"])
        f.write("\nPrep Time: ")
        f.write(day_recipe["time"])

    day_recipe = recipe_book[3]
    print("_____")
    print("Thursday:")
    print(day_recipe["name"])
    print("Complexity: ", day_recipe["complexity"])
    print("Prep Time: ", day_recipe["time"])
    
    with open(output_file, "a") as f:
        f.write("\n_____")
        f.write("\nThursday:\n")
        f.write(day_recipe["name"])
        f.write("\nComplexity: ")
        f.write(day_recipe["complexity"])
        f.write("\nPrep Time: ")
        f.write(day_recipe["time"])

    day_recipe = recipe_book[4]
    print("_____")
    print("Friday:")
    print(day_recipe["name"])
    print("Complexity: ", day_recipe["complexity"])
    print("Prep Time: ", day_recipe["time"])
    
    with open(output_file, "a") as f:
        f.write("\n_____")
        f.write("\nFriday:\n")
        f.write(day_recipe["name"])
        f.write("\nComplexity: ")
        f.write(day_recipe["complexity"])
        f.write("\nPrep Time: ")
        f.write(day_recipe["time"])

    day_recipe = recipe_book[5]
    print("_____")
    print("Saturday:")
    print(day_recipe["name"])
    print("Complexity: ", day_recipe["complexity"])
    print("Prep Time: ", day_recipe["time"])
    
    with open(output_file, "a") as f:
        f.write("\n_____")
        f.write("\nSaturday:\n")
        f.write(day_recipe["name"])
        f.write("\nComplexity: ")
        f.write(day_recipe["complexity"])
        f.write("\nPrep Time: ")
        f.write(day_recipe["time"])

    day_recipe = recipe_book[6]
    print("_____")
    print("Sunday:")
    print(day_recipe["name"])
    print("Complexity: ", day_recipe["complexity"])
    print("Prep Time: ", day_recipe["time"])
    print("\n")
    
    with open(output_file, "a") as f:
        f.write("\n_____")
        f.write("\nSunday:\n")
        f.write(day_recipe["name"])
        f.write("\nComplexity: ")
        f.write(day_recipe["complexity"])
        f.write("\nPrep Time: ")
        f.write(day_recipe["time"])
        f.write("\n")

def today_is_tuesday(recipe_book, output_file):

    day_recipe = recipe_book[0]
    print("_____")
    print("Tuesday:")
    print(day_recipe["name"])          
    print("Complexity: ", day_recipe["complexity"])               
    print("Prep Time: ", day_recipe["time"])

    with open(output_file, "a") as f:
        f.write("\n_____")
        f.write("\nTuesday:\n")
        f.write(day_recipe["name"])
        f.write("\nComplexity: ")
        f.write(day_recipe["complexity"])
        f.write("\nPrep Time: ")
        f.write(day_recipe["time"])

    day_recipe = recipe_book[1]
    print("_____")
    print("Wednesday:")
    print(day_recipe["name"])
    print("Complexity: ", day_recipe["complexity"])
    print("Prep Time: ", day_recipe["time"])
    
    with open(output_file, "a") as f:
        f.write("\n_____")
        f.write("\nWednesday:\n")
        f.write(day_recipe["name"])
        f.write("\nComplexity: ")
        f.write(day_recipe["complexity"])
        f.write("\nPrep Time: ")
        f.write(day_recipe["time"])

    day_recipe = recipe_book[2]
    print("_____")
    print("Thursday:")
    print(day_recipe["name"])
    print("Complexity: ", day_recipe["complexity"])
    print("Prep Time: ", day_recipe["time"])
    
    with open(output_file, "a") as f:
        f.write("\n_____")
        f.write("\nThursday:\n")
        f.write(day_recipe["name"])
        f.write("\nComplexity: ")
        f.write(day_recipe["complexity"])
        f.write("\nPrep Time: ")
        f.write(day_recipe["time"])

    day_recipe = recipe_book[3]
    print("_____")
    print("Friday:")
    print(day_recipe["name"])
    print("Complexity: ", day_recipe["complexity"])
    print("Prep Time: ", day_recipe["time"])
    
    with open(output_file, "a") as f:
        f.write("\n_____")
        f.write("\nFriday:\n")
        f.write(day_recipe["name"])
        f.write("\nComplexity: ")
        f.write(day_recipe["complexity"])
        f.write("\nPrep Time: ")
        f.write(day_recipe["time"])

    day_recipe = recipe_book[4]
    print("_____")
    print("Saturday:")
    print(day_recipe["name"])
    print("Complexity: ", day_recipe["complexity"])
    print("Prep Time: ", day_recipe["time"])
    
    with open(output_file, "a") as f:
        f.write("\n_____")
        f.write("\nSaturday:\n")
        f.write(day_recipe["name"])
        f.write("\nComplexity: ")
        f.write(day_recipe["complexity"])
        f.write("\nPrep Time: ")
        f.write(day_recipe["time"])

    day_recipe = recipe_book[5]
    print("_____")
    print("Sunday:")
    print(day_recipe["name"])
    print("Complexity: ", day_recipe["complexity"])
    print("Prep Time: ", day_recipe["time"])
    
    with open(output_file, "a") as f:
        f.write("\n_____")
        f.write("\nSunday:\n")
        f.write(day_recipe["name"])
        f.write("\nComplexity: ")
        f.write(day_recipe["complexity"])
        f.write("\nPrep Time: ")
        f.write(day_recipe["time"])

    day_recipe = recipe_book[6]
    print("_____")
    print("Monday:")
    print(day_recipe["name"])
    print("Complexity: ", day_recipe["complexity"])
    print("Prep Time: ", day_recipe["time"])
    print("\n")
    
    with open(output_file, "a") as f:
        f.write("\n_____")
        f.write("\nMonday:\n")
        f.write(day_recipe["name"])
        f.write("\nComplexity: ")
        f.write(day_recipe["complexity"])
        f.write("\nPrep Time: ")
        f.write(day_recipe["time"])
        f.write("\n")

def today_is_wednesday(recipe_book, output_file):

    day_recipe = recipe_book[0]
    print("_____")
    print("Wednesday:")
    print(day_recipe["name"])          
    print("Complexity: ", day_recipe["complexity"])               
    print("Prep Time: ", day_recipe["time"])

    with open(output_file, "a") as f:
        f.write("\n_____")
        f.write("\nWednesday:\n")
        f.write(day_recipe["name"])
        f.write("\nComplexity: ")
        f.write(day_recipe["complexity"])
        f.write("\nPrep Time: ")
        f.write(day_recipe["time"])

    day_recipe = recipe_book[1]
    print("_____")
    print("Thursday:")
    print(day_recipe["name"])
    print("Complexity: ", day_recipe["complexity"])
    print("Prep Time: ", day_recipe["time"])
    
    with open(output_file, "a") as f:
        f.write("\n_____")
        f.write("\nThursday:\n")
        f.write(day_recipe["name"])
        f.write("\nComplexity: ")
        f.write(day_recipe["complexity"])
        f.write("\nPrep Time: ")
        f.write(day_recipe["time"])

    day_recipe = recipe_book[2]
    print("_____")
    print("Friday:")
    print(day_recipe["name"])
    print("Complexity: ", day_recipe["complexity"])
    print("Prep Time: ", day_recipe["time"])
    
    with open(output_file, "a") as f:
        f.write("\n_____")
        f.write("\nFriday:\n")
        f.write(day_recipe["name"])
        f.write("\nComplexity: ")
        f.write(day_recipe["complexity"])
        f.write("\nPrep Time: ")
        f.write(day_recipe["time"])

    day_recipe = recipe_book[3]
    print("_____")
    print("Saturday:")
    print(day_recipe["name"])
    print("Complexity: ", day_recipe["complexity"])
    print("Prep Time: ", day_recipe["time"])
    
    with open(output_file, "a") as f:
        f.write("\n_____")
        f.write("\nSaturday:\n")
        f.write(day_recipe["name"])
        f.write("\nComplexity: ")
        f.write(day_recipe["complexity"])
        f.write("\nPrep Time: ")
        f.write(day_recipe["time"])

    day_recipe = recipe_book[4]
    print("_____")
    print("Sunday:")
    print(day_recipe["name"])
    print("Complexity: ", day_recipe["complexity"])
    print("Prep Time: ", day_recipe["time"])
    
    with open(output_file, "a") as f:
        f.write("\n_____")
        f.write("\nSunday:\n")
        f.write(day_recipe["name"])
        f.write("\nComplexity: ")
        f.write(day_recipe["complexity"])
        f.write("\nPrep Time: ")
        f.write(day_recipe["time"])

    day_recipe = recipe_book[5]
    print("_____")
    print("Monday:")
    print(day_recipe["name"])
    print("Complexity: ", day_recipe["complexity"])
    print("Prep Time: ", day_recipe["time"])
    
    with open(output_file, "a") as f:
        f.write("\n_____")
        f.write("\nMonday:\n")
        f.write(day_recipe["name"])
        f.write("\nComplexity: ")
        f.write(day_recipe["complexity"])
        f.write("\nPrep Time: ")
        f.write(day_recipe["time"])

    day_recipe = recipe_book[6]
    print("_____")
    print("Tuesday:")
    print(day_recipe["name"])
    print("Complexity: ", day_recipe["complexity"])
    print("Prep Time: ", day_recipe["time"])
    print("\n")
    
    with open(output_file, "a") as f:
        f.write("\n_____")
        f.write("\nTuesday:\n")
        f.write(day_recipe["name"])
        f.write("\nComplexity: ")
        f.write(day_recipe["complexity"])
        f.write("\nPrep Time: ")
        f.write(day_recipe["time"])
        f.write("\n")

def today_is_thursday(recipe_book, output_file):

    day_recipe = recipe_book[0]
    print("_____")
    print("Thursday:")
    print(day_recipe["name"])          
    print("Complexity: ", day_recipe["complexity"])               
    print("Prep Time: ", day_recipe["time"])

    with open(output_file, "a") as f:
        f.write("\n_____")
        f.write("\nThursday:\n")
        f.write(day_recipe["name"])
        f.write("\nComplexity: ")
        f.write(day_recipe["complexity"])
        f.write("\nPrep Time: ")
        f.write(day_recipe["time"])

    day_recipe = recipe_book[1]
    print("_____")
    print("Friday:")
    print(day_recipe["name"])
    print("Complexity: ", day_recipe["complexity"])
    print("Prep Time: ", day_recipe["time"])
    
    with open(output_file, "a") as f:
        f.write("\n_____")
        f.write("\nFriday:\n")
        f.write(day_recipe["name"])
        f.write("\nComplexity: ")
        f.write(day_recipe["complexity"])
        f.write("\nPrep Time: ")
        f.write(day_recipe["time"])

    day_recipe = recipe_book[2]
    print("_____")
    print("Saturday:")
    print(day_recipe["name"])
    print("Complexity: ", day_recipe["complexity"])
    print("Prep Time: ", day_recipe["time"])
    
    with open(output_file, "a") as f:
        f.write("\n_____")
        f.write("\nSaturday:\n")
        f.write(day_recipe["name"])
        f.write("\nComplexity: ")
        f.write(day_recipe["complexity"])
        f.write("\nPrep Time: ")
        f.write(day_recipe["time"])

    day_recipe = recipe_book[3]
    print("_____")
    print("Sunday:")
    print(day_recipe["name"])
    print("Complexity: ", day_recipe["complexity"])
    print("Prep Time: ", day_recipe["time"])
    
    with open(output_file, "a") as f:
        f.write("\n_____")
        f.write("\nSunday:\n")
        f.write(day_recipe["name"])
        f.write("\nComplexity: ")
        f.write(day_recipe["complexity"])
        f.write("\nPrep Time: ")
        f.write(day_recipe["time"])

    day_recipe = recipe_book[4]
    print("_____")
    print("Monday:")
    print(day_recipe["name"])
    print("Complexity: ", day_recipe["complexity"])
    print("Prep Time: ", day_recipe["time"])
    
    with open(output_file, "a") as f:
        f.write("\n_____")
        f.write("\nMonday:\n")
        f.write(day_recipe["name"])
        f.write("\nComplexity: ")
        f.write(day_recipe["complexity"])
        f.write("\nPrep Time: ")
        f.write(day_recipe["time"])

    day_recipe = recipe_book[5]
    print("_____")
    print("Tuesday:")
    print(day_recipe["name"])
    print("Complexity: ", day_recipe["complexity"])
    print("Prep Time: ", day_recipe["time"])
    
    with open(output_file, "a") as f:
        f.write("\n_____")
        f.write("\nTuesday:\n")
        f.write(day_recipe["name"])
        f.write("\nComplexity: ")
        f.write(day_recipe["complexity"])
        f.write("\nPrep Time: ")
        f.write(day_recipe["time"])

    day_recipe = recipe_book[6]
    print("_____")
    print("Wednesday:")
    print(day_recipe["name"])
    print("Complexity: ", day_recipe["complexity"])
    print("Prep Time: ", day_recipe["time"])
    print("\n")
    
    with open(output_file, "a") as f:
        f.write("\n_____")
        f.write("\nWednesday:\n")
        f.write(day_recipe["name"])
        f.write("\nComplexity: ")
        f.write(day_recipe["complexity"])
        f.write("\nPrep Time: ")
        f.write(day_recipe["time"])
        f.write("\n")

def today_is_friday(recipe_book, output_file):

    day_recipe = recipe_book[0]
    print("_____")
    print("Friday:")
    print(day_recipe["name"])          
    print("Complexity: ", day_recipe["complexity"])               
    print("Prep Time: ", day_recipe["time"])

    with open(output_file, "a") as f:
        f.write("\n_____")
        f.write("\nFriday:\n")
        f.write(day_recipe["name"])
        f.write("\nComplexity: ")
        f.write(day_recipe["complexity"])
        f.write("\nPrep Time: ")
        f.write(day_recipe["time"])

    day_recipe = recipe_book[1]
    print("_____")
    print("Saturday:")
    print(day_recipe["name"])
    print("Complexity: ", day_recipe["complexity"])
    print("Prep Time: ", day_recipe["time"])
    
    with open(output_file, "a") as f:
        f.write("\n_____")
        f.write("\nSaturday:\n")
        f.write(day_recipe["name"])
        f.write("\nComplexity: ")
        f.write(day_recipe["complexity"])
        f.write("\nPrep Time: ")
        f.write(day_recipe["time"])

    day_recipe = recipe_book[2]
    print("_____")
    print("Sunday:")
    print(day_recipe["name"])
    print("Complexity: ", day_recipe["complexity"])
    print("Prep Time: ", day_recipe["time"])
    
    with open(output_file, "a") as f:
        f.write("\n_____")
        f.write("\nSunday:\n")
        f.write(day_recipe["name"])
        f.write("\nComplexity: ")
        f.write(day_recipe["complexity"])
        f.write("\nPrep Time: ")
        f.write(day_recipe["time"])

    day_recipe = recipe_book[3]
    print("_____")
    print("Monday:")
    print(day_recipe["name"])
    print("Complexity: ", day_recipe["complexity"])
    print("Prep Time: ", day_recipe["time"])
    
    with open(output_file, "a") as f:
        f.write("\n_____")
        f.write("\nMonday:\n")
        f.write(day_recipe["name"])
        f.write("\nComplexity: ")
        f.write(day_recipe["complexity"])
        f.write("\nPrep Time: ")
        f.write(day_recipe["time"])

    day_recipe = recipe_book[4]
    print("_____")
    print("Tuesday:")
    print(day_recipe["name"])
    print("Complexity: ", day_recipe["complexity"])
    print("Prep Time: ", day_recipe["time"])
    
    with open(output_file, "a") as f:
        f.write("\n_____")
        f.write("\nTuesday:\n")
        f.write(day_recipe["name"])
        f.write("\nComplexity: ")
        f.write(day_recipe["complexity"])
        f.write("\nPrep Time: ")
        f.write(day_recipe["time"])

    day_recipe = recipe_book[5]
    print("_____")
    print("Wednesday:")
    print(day_recipe["name"])
    print("Complexity: ", day_recipe["complexity"])
    print("Prep Time: ", day_recipe["time"])
    
    with open(output_file, "a") as f:
        f.write("\n_____")
        f.write("\nWednesday:\n")
        f.write(day_recipe["name"])
        f.write("\nComplexity: ")
        f.write(day_recipe["complexity"])
        f.write("\nPrep Time: ")
        f.write(day_recipe["time"])

    day_recipe = recipe_book[6]
    print("_____")
    print("Thursday:")
    print(day_recipe["name"])
    print("Complexity: ", day_recipe["complexity"])
    print("Prep Time: ", day_recipe["time"])
    print("\n")
    
    with open(output_file, "a") as f:
        f.write("\n_____")
        f.write("\nThursday:\n")
        f.write(day_recipe["name"])
        f.write("\nComplexity: ")
        f.write(day_recipe["complexity"])
        f.write("\nPrep Time: ")
        f.write(day_recipe["time"])
        f.write("\n")

def today_is_saturday(recipe_book, output_file):

    day_recipe = recipe_book[0]
    print("_____")
    print("Saturday:")
    print(day_recipe["name"])          
    print("Complexity: ", day_recipe["complexity"])               
    print("Prep Time: ", day_recipe["time"])

    with open(output_file, "a") as f:
        f.write("\n_____")
        f.write("\nSaturday:\n")
        f.write(day_recipe["name"])
        f.write("\nComplexity: ")
        f.write(day_recipe["complexity"])
        f.write("\nPrep Time: ")
        f.write(day_recipe["time"])

    day_recipe = recipe_book[1]
    print("_____")
    print("Sunday:")
    print(day_recipe["name"])
    print("Complexity: ", day_recipe["complexity"])
    print("Prep Time: ", day_recipe["time"])
    
    with open(output_file, "a") as f:
        f.write("\n_____")
        f.write("\nSunday:\n")
        f.write(day_recipe["name"])
        f.write("\nComplexity: ")
        f.write(day_recipe["complexity"])
        f.write("\nPrep Time: ")
        f.write(day_recipe["time"])

    day_recipe = recipe_book[2]
    print("_____")
    print("Monday:")
    print(day_recipe["name"])
    print("Complexity: ", day_recipe["complexity"])
    print("Prep Time: ", day_recipe["time"])
    
    with open(output_file, "a") as f:
        f.write("\n_____")
        f.write("\nMonday:\n")
        f.write(day_recipe["name"])
        f.write("\nComplexity: ")
        f.write(day_recipe["complexity"])
        f.write("\nPrep Time: ")
        f.write(day_recipe["time"])

    day_recipe = recipe_book[3]
    print("_____")
    print("Tuesday:")
    print(day_recipe["name"])
    print("Complexity: ", day_recipe["complexity"])
    print("Prep Time: ", day_recipe["time"])
    
    with open(output_file, "a") as f:
        f.write("\n_____")
        f.write("\nTuesday:\n")
        f.write(day_recipe["name"])
        f.write("\nComplexity: ")
        f.write(day_recipe["complexity"])
        f.write("\nPrep Time: ")
        f.write(day_recipe["time"])

    day_recipe = recipe_book[4]
    print("_____")
    print("Wednesday:")
    print(day_recipe["name"])
    print("Complexity: ", day_recipe["complexity"])
    print("Prep Time: ", day_recipe["time"])
    
    with open(output_file, "a") as f:
        f.write("\n_____")
        f.write("\nWednesday:\n")
        f.write(day_recipe["name"])
        f.write("\nComplexity: ")
        f.write(day_recipe["complexity"])
        f.write("\nPrep Time: ")
        f.write(day_recipe["time"])

    day_recipe = recipe_book[5]
    print("_____")
    print("Thursday:")
    print(day_recipe["name"])
    print("Complexity: ", day_recipe["complexity"])
    print("Prep Time: ", day_recipe["time"])
    
    with open(output_file, "a") as f:
        f.write("\n_____")
        f.write("\nThursday:\n")
        f.write(day_recipe["name"])
        f.write("\nComplexity: ")
        f.write(day_recipe["complexity"])
        f.write("\nPrep Time: ")
        f.write(day_recipe["time"])

    day_recipe = recipe_book[6]
    print("_____")
    print("Friday:")
    print(day_recipe["name"])
    print("Complexity: ", day_recipe["complexity"])
    print("Prep Time: ", day_recipe["time"])
    print("\n")
    
    with open(output_file, "a") as f:
        f.write("\n_____")
        f.write("\nFriday:\n")
        f.write(day_recipe["name"])
        f.write("\nComplexity: ")
        f.write(day_recipe["complexity"])
        f.write("\nPrep Time: ")
        f.write(day_recipe["time"])
        f.write("\n")
