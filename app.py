from movie_rental.models import Movie
from movie_rental.rental_system import RentalSystem
from movie_rental.rental_provider import FileRentalProvider

print('Welcome in movie rental 0.3')

rental_provider = FileRentalProvider(
    'movie_rental/resources/movie_database.db',
    'movie_rental/resources/rented_movies.db'
)

system = RentalSystem(rental_provider)

while True:
    try:
        action = input('Input your action [all, rent, return, add, remove]: ')

        if action == 'remove':
            movie_id = input('Movie to remove')
            system.remove(movie_id)
            print(f'Movie {movie_id} was removed ')

        if action == 'add':
            movie_data = input('Enter id, title, year, score')
            system.add(Movie(*movie_data.split(',')))
            print(f'You add movie')

        if action == 'return':
            back_movie_id = input('What movie You want to return')
            system.give_back(back_movie_id)
            print(f'Your returned movie {back_movie_id}')

        if action == 'all':
            li = system.get_all()

            sort_response = input('Do you want to sort results[y/n]?')

            if sort_response == 'n':
                print(li)
            elif sort_response == 'y':
                order = input('Do you want to sort descending? ')

                print(sorted(li, key=lambda m: m.get_score(), reverse=order == 'y'))

        if action == 'rent':
            movie_id = input('What movie you want yo rent?')
            system.rent(movie_id)
            print(f'You rented movie {movie_id}')
    except ValueError as error:
        print(error)