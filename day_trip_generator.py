import random
#Travel the USA
destinations = ["Alabama" , "Alaska" , "Arizona" , "Arkansas" , "California" , "Colorado" , "Connecticut" , "Delaware" , "Florida" , "Georgia" , "Hawaii" , "Idaho" , "Illinois" , "Indiana" , "Iowa" , "Kansas" , "Kentucky" , "Louisiana" , "Maine" , "Maryland" , "Massachusetts" , "Michigan" , "Minnesota" , "Mississippi" , "Missouri" , "Montana" , "Nebraska" , "Nevada" , "New Hampshire" , "New Jersey" , "New Mexico" , "New York" , "North Carolina" , "North Dakota" , "Ohio" , "Oklahoma" , "Oregon" , "Pennsylvania" , "Pennsylvania" , "Rhode Island" , "South Carolina" , "South Dakota" , "Tennessee" , "Texas" , "Utah" , "Vermont" , "Virginia" , "Washington" , "West Virginia" , "Wisconsin", "Wyoming"]
restaurants = ["Starbucks","Chick-fil-A	","Taco Bell","Wendy's","Burger King","Dunkin'"	,"Subway","Domino's	","Chipotle Mexican Grill","Sonic Drive-In","Pizza Hut","Panera Bread","KFC	",
"Popeyes Louisiana Kitchen","Arby's","Little Caesars","Panda Express","Jack in the Box","Olive Garden","Papa John's","Buffalo Wild Wings","Applebee's","Chili's Grill & Bar","Whataburger","Texas Roadhouse","IHOP","Outback Steakhouse"]
mode_of_transportations = ["bicycle" , "motorcycle" , "car" , "ferry" , "blimp" , "ship" , "bus" , "train" , "airplane"]
entertainments = ["Skydive" , "Jetski" , "Dance" , "Movie Theater" , "Rollerblade" , "Snowboard"]

def gen_rand_from_list(list_of_values):
    return(random.choice(list_of_values))

def generate_trip_items():
    destination = gen_rand_from_list(destinations)
    restaurant =  gen_rand_from_list(restaurants)
    mode_of_transportation = gen_rand_from_list(mode_of_transportations)
    entertainment = gen_rand_from_list(entertainments)
    trip = [destination , mode_of_transportation , entertainment , restaurant]
    return trip

def user_trip_select(trip_array):
    trip_items = trip_array
    user_choice = input(f"Would you like to go to {trip_items[0]} via {trip_items[1]}, and go to {trip_items[2]} and dine at {trip_items[3]}. Please enter either 'yes' or 'no': ").lower()
    while user_choice == "no":
        return user_trip_select(generate_trip_items())

    return trip_items

def display_trip():
    completed_trip = user_trip_select(generate_trip_items())
    print(f"You have chosen to go to {completed_trip[0]} via {completed_trip[1]}, and go to {completed_trip[2]} and dine at {completed_trip[0]}. That's a wonderful idea, would you like to make reservations in cash or card.")

display_trip()