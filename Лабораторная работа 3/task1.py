class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self) -> str:
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name=name, author=author)
        if not isinstance(pages, int):
            raise TypeError
        if not pages > 0:
            raise ValueError
        self.pages = pages

    def __str__(self) -> str:
        return f"Книга {self._name}. Автор {self._author}. Количество страниц: {self.pages}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name=name, author=author)
        if not isinstance(duration, float):
            raise TypeError
        if not duration > 0:
            raise ValueError
        self.duration = duration

    def __str__(self) -> str:
        return f"Книга {self._name}. Автор {self._author}. Продолжительность: {self.duration}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self.duration!r})"
