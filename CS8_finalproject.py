# Zejie Gao (8913006) and Han Wu(8018996), CS 8 (M21)

movies = {'im':{'title':'Iron Man','year':'2008','director':'Jon Favreau','imdb':'https://www.imdb.com/title/tt0371746/?ref_=fn_al_tt_1'}}

movie_menu = {
    '1': 'List movies',
    '2': 'Add a movie',
    '3': 'Update a movie',
    '4': 'Delete a movie',
    'Q': 'Quit the system'
}

def print_menu(menu):
    '''the function is build for the purpose of create the menu that can make the command.'''
    print('**************************')
    print('What would you like to do?')
    for i in menu:
        print('{} - {}'.format(i, menu[i]))
    print('**************************')

    
def print_movie(movie):
    '''the function is build for the purpose of give information of movie.'''
    print('title: {}'.format(movie["title"]))
    print('year: {}'.format(movie["year"]))
    print('director: {}'.format(movie["director"]))
    print('imdb: {}'.format(movie["imdb"]))
    

def create_id(text):
    '''the function is build for the purpose of create the id. movie id is the initials of title using lowercase.'''
    text = text.lower()
    words = text.split()
    result_id = ""
    for i in range(len(words)):
        result_id = result_id + words[i][0]
    return result_id



def list_movies():
    '''the function is build for print the number of movies in the collection and print all the movies' information in the collection'''
    print("You select option 1 to list movies.")
    print("-----------------------------------")
    if len(movies) == 0:
        print("There is no movies in this collection")
        return
    else:
        if len(movies) == 1:
            print("There is " + str(len(movies)) + " movie in this collection.")
        else:
            print("There are " + str(len(movies)) + " movie in this collection.")
        for key in movies.keys():
            print(key)
            print_movie(movies[key])
        print("------------------------------------------------------")


def add_a_movie():
    '''the function is build for the purpose of add a movie.'''
    while True:
        print("You selected option 2 to Add a movie.")
        print("You'll need to add the following info:\n- title\n- year\n- director\n- imdb")
        print('::: Press Enter to continue')
        print('or type M to return to the menu.')
        opt = input("::: ")

        if opt == 'M' or opt == 'm':
            return False
        else:
            title = input("Title: ")
            print('Movie key: {}'.format(create_id(title)))
            if create_id(title) in movies:
                print("WARNING: A movie with such key already exists\n{} - {}".format(create_id(title), title))
                
            else:
                print('Adding a new movie:')
                year = input("Year: ")
                director = input("Director: ")
                imdb = input("IMDB: ")
                new_movies = {'title': title, 'year': year, 'director': director, 'imdb': imdb}
                movieID = create_id(title)
                movies[movieID] = new_movies
                print_movie(new_movies)
            return True

def update_movie():
    '''the function is build for the purpose of update a movie.It will first ask the user to input the ID of an movie, which exists in the current collection. '''
    while True:
        print('Enter the ID of a movie that you want to update')
        print('or type M to return to the menu.')
        movie_id = input("::: ")
        if movie_id == 'M' or movie_id == 'm':
            return False
        else:
            ok = 0
            for key in movies.keys():
                if key == movie_id:
                    ok = 1
                    break
            if(ok == 1):
                ok = 0
                print("Updating '{}'".format(movie_id))
                print_movie(movies[movie_id])
                print('Which field would you like to update?')
                movie_field = {
                '0': 'title',
                '1': 'year',
                '2': 'director',
                '3': 'imdb'
                }
                for i in movie_field:
                    print('{} - {}'.format(i, movie_field[i]))
                while True:
                    print('Enter an option for the field')
                    print('or type M to return to the menu.')
                    opt = input("::: ")
                    if opt == 'M' or opt == 'm':
                        return False
                    else:
                        print('You selected option {} to update {}'.format(opt, movie_field[opt]))
                        print('Enter your updated value of {}:'.format(movie_field[opt]))
                        new_data = input("::: ")
                        print('Successfully updated, new infos:')
                        print('----------------------------------------------------')
                        if opt == '0':
                            movies[movie_id]['title'] = new_data
                            new_movie_id = create_id(new_data)
                            movie2 = movies[movie_id]
                            movies[new_movie_id] = movie2
                            movies.pop(movie_id)
                        for movie in movies.values():
                            if opt == '1':
                                movie.update({'year': new_data})
                            elif opt == '2':
                                movie.update({'director': new_data})
                            elif opt == '3':
                                movie.update({'imdb': new_data})
                            print_movie(movie)
            else:
                print("WARNING: No such a movie to update")
        return True
                
            

def delete_movie():
    '''the function is build for the purpose of delete a movie.It will first ask the user to input the ID of an movie which exists in the current collection. '''
    while True:
        print('Enter the ID of a movie that you want to delete')
        print('or type M to return to the menu.')
        movie_id = input("::: ")
        if movie_id == 'M' or movie_id == 'm':
            return False
        else:
            if movie_id in movies:
                print("Deleting movie with ID'{}'".format(movie_id))
                print('----------------------------------------------------')
                print_movie(movies[movie_id])
                print('::: Are you sure? Type Y or N')
                opt = input("::: ")
                if opt == 'Y' or opt == 'y':
                    print('Deleted')
                    del movies[movie_id]
                if opt == 'N' or opt == 'n':
                    print("Looks like you aren't 100% sure.")
                    print('Cancelling the deletion.')
            else:
                    print("WARNING: No such a movie to delete")
            return True
            


if __name__ == "__main__":
    '''We can use this code to give instructions'''
    opt = None

    while True:
        print_menu(movie_menu)
        print("::: Enter an option")
        opt = input("::: ")

        if opt == 'q' or opt == 'Q':
            print("Goodbye")
            break
        else:
            if opt == '1':
                list_movies()
            if opt == '2':
                add_a_movie()
            if opt == '3':
                update_movie()
            if opt == '4':
                delete_movie()
            else:
                continue
    print("See you next time!")

  
