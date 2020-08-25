import imdb
hr=imdb.IMDb()
movie_name=input("enter the movie name : ")
movies=hr.search_movie(movie_name)
index=movies[0].getID()
movie=hr.get_movie(index)
title=movie['title']
year=movie['year']
cast=movie['cast']
list_of_cast=','.join(map(str,cast))
print('title: ',title)
print('year: ',year)  #last 3 lines of code wrote by my own by trail and error methode if you not understand it's fine
print("cast is : ")
for i in range(len(cast)):
    print(cast[i],end=",")
