"""Restaurant rating lister."""

def rest_rating(filename):
    file = open(filename)
    ratings = {}
    for line in file: # iterate over each line in the input file
        new_line = line.split(':') # this is a list
        new_line[1] = int(new_line[1]) # turn the number stored as a string into an integer
        #The Tavern:3 -> ['The Tavern', '3']
        #print(new_line)
        ratings[new_line[0]] = new_line[1] # take the data from the new_line list and add it to the dictionary

    user_rest_name = input("Please enter a restaurant name: ")
    user_rest_score = input("Please enter a restaurant score: ")
    ratings[user_rest_name] = user_rest_score #added user inputs to the ratings dictionary

    ratings = dict(sorted(ratings.items())) #made sorted list in to a dict 
    for key, value in ratings.items():      #this printed the key, values in an organized way vs in a dict.
        print(f"{key} is rated at {value}.")


rest_rating('scores.txt')
