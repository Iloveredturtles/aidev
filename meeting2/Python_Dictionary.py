movie = { 
    'title': 'Jumanji : The Next Level',
    'year': 2017,
    'genre' :'Adventure',  
}
movie_2 = { 
    'title': 'Frozen II',
    'year': 2019,
    'genre' :'Family',  
}

# movie.update({'viewers': 44324578}) #Added new items
# movie["genre"] = "Adventure/Comedy" #Changing the value of the genre key
# del movie['year'] #Removing year items

# print(movie)
# movie_2.update({'viewers': 98698637})
# movie_2["genre"] ="Family/Musical"
# print(movie_2)

import random
friends_list = ['Bryan','Cia','Petter','Drake']
random_name = random.choice(friends_list)
random_number = random.randint(10,15)
print(random_name)
print(random_number)