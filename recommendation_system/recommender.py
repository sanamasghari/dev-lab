""" Mini Recommendation System """
import json


def load_users():
    """load json file in json format and return as dictionary"""
    users_file = open("/home/sanam/Desktop/ai_daneshkar_bootcamp/python/assignment/users.json", "r").read()
    users_content = json.loads(users_file)
    return users_content


def get_or_create_user(name, data_set):
    """ check for user if does not exist, creates one with 3 favorite movie"""
    new_person = {}
    if name not in data_set:
        print("Enter maximum your 3 favorite movies: ")
        favorite_movies = []
        for i in range(3):
            movie = input(f"{i+1}. ").strip().lower().capitalize()
            if movie:
                favorite_movies.append(movie)
        new_person[name] = favorite_movies
        return new_person     
    else:
        return "username exists"
    
    
def save_users(data, data_set):
    """ Append new information into json dataset """
    data_set.update(data)
    with open("users.json", "w") as f:
        json.dump(data_set, f, indent=4)
    return "Username added successfuly!"
    
    
def find_best_match(name, data_set):
    """input the name to find the best similar person to that name"""
    comparison = {}
    for person in data_set: # iterate in every item of users dictionary
        count = 0
        if person == name:
            continue
        for movie in data_set[person]: # iterate in values of each item of dict, which is a list
            for user_movie in data_set[name]: # iterate in list of the person's movies
                if user_movie == movie:
                    count += 1
        comparison[person] = count

    # use max function to find the highest similarity
    best_match = max(comparison.values())
    # if maximum similariti is zero, it means it didn't find any person
    if best_match == 0:
        return "No Similarity"
    else:
    # if find similarity and if the number of most similarities is greater than one, sort the names alphabetically.
        condidates = [person for person, similarity in comparison.items() if similarity == best_match]
        return sorted(condidates)[0]

    
def recommend_for(name, user, data_set):
    """ input: 
            name: username of the person,
            user: username of similar person to iterate on his movies,
            data_set"""
    for movie in data_set[user]:
        if movie == data_set[name]:
            continue
        elif not movie:
            return "No Suggestion"
        else:
            return movie
    
    
def main():
    """ The main function to control other finctions"""
    
    # Read and Load data
    data_set = load_users()
    print((data_set))

    # check for new username
    username = input("Enter your name: ").strip().lower().capitalize()
    new_data = get_or_create_user(username, data_set)
    print((new_data))

    # save new data: username, list of favorite movies
    msg = save_users(new_data, data_set)
    print(msg)

    # Find the most similar person
    similar_person = find_best_match(username, data_set)
    print(similar_person)
    
    #recommend one movie 
    recommendation = recommend_for(username, similar_person, data_set)
    print(recommendation)
        
    
if __name__ == "__main__":
    main()