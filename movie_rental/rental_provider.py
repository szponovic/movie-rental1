import abc
from typing import List
from movie_rental.models import Movie


class AbstractRentalProvider(abc.ABC):

    @abc.abstractmethod
    def get_all(self) -> List[Movie]:
        pass

    @abc.abstractmethod
    def exists(self, movie_id: str) -> bool:
        raise NotImplemented

    @abc.abstractmethod
    def is_rented(self, movie_id: str) -> bool:
        raise NotImplemented

    @abc.abstractmethod
    def add_rent(self, movie_id: str):
        raise NotImplemented

    @abc.abstractmethod
    def remove_rent(self, movie_id: str):
        raise NotImplemented

    @abc.abstractmethod
    def add_movie(self, movie: Movie):
        raise NotImplemented

    @abc.abstractmethod
    def remove_movie(self, movie_id) -> str:
        raise NotImplemented

class FileRentalProvider(AbstractRentalProvider):
    def __init__(self, movie_db: str, rented_movie_db: str):
        self._movie_db = movie_db
        self._rented_movie_db = rented_movie_db

    def get_all(self) -> List[Movie]:
        movie_list = []

        with open(self._movie_db) as handler:
            for line in handler:
                movie_list.append(Movie(*line.split('|')))

        return movie_list

    def exists(self, movie_id: str) -> bool:
        return any((movie.get_id() == movie_id for movie in self.get_all()))

    def is_rented(self, movie_id: str) -> bool:
        with open(self._rented_movie_db) as handler:
            return any(movie_id == m_id.strip() for m_id in handler.readlines())

    def add_rent(self, movie_id: str):
        with open(self._rented_movie_db, 'a') as write_handler:
            write_handler.write(movie_id + '\n')

    def remove_rent(self, movie_id: str):
        with open(self._rented_movie_db) as handler:
            lines = handler.readlines()
            if movie_id not in [id.strip() for id in lines]:
                raise ValueError(f'Movie {movie_id} is not rented')

        with open(self._rented_movie_db, 'w') as read_handler:
            for line in lines:
                if line.strip() != movie_id:
                    read_handler.write(line)

    def add_movie(self, movie: Movie):
        with open(self._movie_db, 'a') as handler:
            handler.write(str(movie) + '\n')

    def remove_movie(self, movie_id):
        with open(self._movie_db, 'r') as read_handler:
            movie_lines = read_handler.readlines()

        with open(self._movie_db, 'w') as write_handler:
            for line in movie_lines:
                if line.split('|')[0] != movie_id:
                    write_handler.write(line)