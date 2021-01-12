"""Restaurant rating lister."""

#create display_restaurant_ratings(file)
    #open file

    #restaurant_ratings {}
    #loop through each line in file
        #for each line 
        #   remove trailing white space and split at colon [restaurant_info]
            # Loop through the list and add the 0 index as key and 1 index as 
            # value
    # Use sorted on our dictionary, restaurant_names
    # Loop through restaurant_names
        # Using the name pull the value from the dictionary, print as an f 
        # string

    # Close file




    
    #give_choices()
        #create dictionary()
        #while loop
            #what do you want to do
                #display()
                #input()
            #break out of function if user selects quit

import sys

def create_dictionary():
    data_to_rate = open(sys.argv[1])
    ratings = {}

    for line in data_to_rate:
        data_to_rate = line.rstrip().split(":")
        ratings[data_to_rate[0]] = data_to_rate[1]  

    return ratings


def display_ratings(ratings_dict):
    restaurant_names = sorted(ratings_dict)

    for name in restaurant_names:
        print(f'{name} is rated at {ratings_dict[name]}')

def add_restaurant(ratings_dict):
    user_restaurant = input("What restaurant would you like to rate? ")

    while True:
        user_rating = input(f'On a scale on 1 - 5, how would you rate {user_restaurant} ')

        if user_rating in ['1', '2', '3', '4', '5']:
            user_rating = int(user_rating)
            break

        else:
            print("Sorry try again!")

    ratings_dict[user_restaurant] = user_rating
    return ratings_dict

def give_choices():
    restaurant_ratings = create_dictionary()

    while True:
        print()
        print('What would you like to do?')
        print()
        print('To display a list of restaurants along with their ratings, enter "D"')
        print('To add a new restaurant and rate it, enter "A"')
        print('To quit, enter "Q"')
        choice = input(">>> ").upper()
        print()

        if choice == 'Q':
            break
        elif choice == 'D':
            display_ratings(restaurant_ratings)
        elif choice == 'A':
            add_restaurant(restaurant_ratings)

give_choices()
            



# def display_restaurant_ratings():
#     """ Display and Organize Restaurant Ratings"""

#     restaurant_data = open(sys.argv[1])

#     restaurant_ratings = {}

#     for line in restaurant_data:
        
#         restaurant_info = line.rstrip().split(":")
#         restaurant_ratings[restaurant_info[0]] = restaurant_info[1]  

#     user_restaurant = input("What restaurant would you like to rate? ")

#     while True:
#         user_rating = input(f'On a scale on 1 - 5, how would you rate {user_restaurant} ')

#         if user_rating in ['1', '2', '3', '4', '5']:
#             user_rating = int(user_rating)
#             break

#         else:
#             print("Sorry try again!")

#     restaurant_ratings[user_restaurant] = user_rating

#     restaurant_names = sorted(restaurant_ratings)

#     for name in restaurant_names:
#         print(f'{name} is rated at {restaurant_ratings[name]}')

#     restaurant_data.close()

# display_restaurant_ratings()



