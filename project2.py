from pathlib import Path

filename = "costa_restaurants.txt"
menu_index = "menu_index.txt"

# create a function that convert strings in textfile to list


def greeting():
# greeting the user
    print("Hello business owner, do you want to add a new restaurant?")

# ********************amended*****
def read_line(filename: str) -> list:
# turn each line in the file to a list of string, and
# the content to list of lists
    try:
        restaurant_list = []
        with open(filename, 'r') as restaurant_info:
            lines = restaurant_info.readlines()
        for line in lines: 
            restaurant_list.append(line.split(","))          
    except FileNotFoundError:
        new_filename = input("File not found. please input a new file name")
        read_line(new_filename)
    return restaurant_list

# ********************amended*****
def option_validator(x: str)->str:
# check if the user's file is pdf 
    while not (x.lower() == "y" or x.lower() =="n"):
        x = input("Please re-enter! (y / n)")
    else:
        if x == 'y':
            return 'yes'
        else:
            return 'no'

def file_validator(x: str)->str:
    '''validate the menu pdf file user upload'''
    try:
        # check if the user's file is pdf
        while not x[-3:] == "pdf":
            x = input("Please enter a pdf file")
            # check if the file exists
            path.exists(x)
            break
    except FileNotFoundError:
        print("file doesn't exist")
    
        
    return x

def upload_file(file: str) -> list:
# upload the file
    new_file = input("Type in file name to input with either '.txt'"
                     + " or '.pdf'")
    with open(menu_index, 'w') as menu_name:
        # write new menu names to menu_index.txt
        # and because menu_index is not created yet,
        # write attribute will create a new txt file
        new_file = menu_name.write()


def add_user_input(filename)->list:
# get input from the user
    new_input = "y"
    while new_input == "y":
        try:
            with open(filename,'a+') as user_input:
                # promt user's input
                restaurant_name = input("Enter restaurant's name: ")
                assert len(restaurant_name) > 0
                address = input("Enter restaurant's address: ")
                assert len(address) > 0
                zipcode = input("Enter restaurant's zipcode: ")
                vegetarian = input("vegetarian (y/n): ")
                option_validator(vegetarian)
                vegan = input("vegan (y/n): ")
                option_validator(vegan)
                gluten_free = input("gluten-free (y/n): ")
                option_validator(gluten_free)
                menu = input("please enter menu name in .pdf: ")
                file_validator(menu)
        except AssertionError as error:
                restaurant_name = input("Please enter a name.")
                address = input("Please enter the zip code.")
                new_info = [
                    restaurant_name, address, zipcode, vegetarian,
                    vegan, gluten_free, menu]
                new_input = input("Do you want to add another one? (y/n)")
                # compare if the new info is different from the current list
                for each in restaurant_list:
                    if new_info[0].lower() != each[0].lower():
                        restaurant_list.append(new_info)
                    
    return restaurant_list
        
 
##if __name__ == "__main__":
##    restaurant_list = []
##    greeting()
print (read_line(filename))
##    add_user_input()
##    upload_file(menu)
    
 
 
