from typing import List, Callable
from movie_rental.models import Movie
from movie_rental.rental_provider import AbstractRentalProvider


class RentalSystem:
    def __init__(self, rental_provider: AbstractRentalProvider):
        self._rental_provider = rental_provider

    def get_all(self) -> List[Movie]:
        return self._rental_provider.get_all()

    def get_sorted(self, callback: Callable):
        sorted(self.get_all(), key=lambda m: m.get_score())



    def rent(self, movie_id: str):
        if not self._rental_provider.exists(movie_id):
            raise ValueError(f'Movie {movie_id} does not exist')

        if self._rental_provider.is_rented(movie_id):
            raise ValueError(f'Movie {movie_id} is already rented')

        self._rental_provider.add_rent(movie_id)

    def give_back(self, movie_id: str):
        if not self._rental_provider.exists(movie_id):
            raise ValueError(f'Movie {movie_id} does not exist')

        if not self._rental_provider.is_rented(movie_id):
            raise ValueError(f'Movie {movie_id} is not rented')

        self._rental_provider.remove_rent(movie_id)

    def add(self, movie: Movie):
        if self._rental_provider.exists(movie.get_id()):
            raise ValueError(f'Movie {movie.get_id()} alread exist')

        self._rental_provider.add_movie(movie)

    def remove(self, movie_id: str):
        if not self._rental_provider.exists(movie_id):
            raise ValueError(f'Movie {movie_id} does not exist')

        if self._rental_provider.is_rented(movie_id):
            raise ValueError(f'Movie {movie_id} is rented')

        self._rental_provider.remove_movie(movie_id)