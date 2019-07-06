# models.py movie id, title, year


class Movie:
    def __init__(self, id: str, title: str, year: int, score: float):
        self._id = id
        self._title = title
        self._year = year
        self._score = score

    def __repr__(self):
        return f'\nMovie {self._title}\n'

    def __str__(self):
        return f'{self._id}|{self._title}|{self._year}|{self._score}'

    def get_title(self) -> str:
        return self._title

    def get_year(self) -> int:
        return self._year

    def get_id(self) -> str:
        return self._id

    def get_score(self) -> float:
        return float(self._score)





