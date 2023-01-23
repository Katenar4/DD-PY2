from typing import Union

import doctest


class Telephone:
    def __init__(self, free_memory: Union[int, float], average_app_memory: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Телефон"

        :param free_memory: Свободный обьем памяти телефона
        :param average_app_memory: Средний объем памяти, занимаемый одним приложение

        Примеры:
        >>> telephone = Telephone(6.2, 0.5)  # инициализация экземпляра класса
        """
        if not isinstance(free_memory, (int, float)):
            raise TypeError("Свободный обьем памяти телефона должен быть типа int или float")
        if free_memory < 0:
            raise ValueError("Свободный обьем памяти телефона должен быть больше или равен нулю")
        self.free_memory = free_memory

        if not isinstance(average_app_memory, (int, float)):
            raise TypeError("Средний объем памяти, занимаемый одним приложение должен быть типа int или float")
        if average_app_memory < 0:
            raise ValueError("Средний объем памяти, занимаемый одним приложение не может быть отрицательным числом")
        self.average_app_memory = average_app_memory

    def ability_to_download(self) -> bool:
        """
        Функция, которая проверяет хватает ли памяти на загрузку хотя бы одного приложения

        :return: Возможжно ли загрузить хотя бы 1 приложение

        Примеры:
        >>> telephone = Telephone(6.2, 0.5)
        >>> telephone.ability_to_download()
        """
        ...

    def number_of_apps(self) -> None:
        """
        Функция, которая вычисляет сколько приложений можно загрузить

        :return: Количество приложений, которое можно загрузить

        Примеры:
        >>> telephone = Telephone(6.2, 0.5)
        >>> telephone.number_of_apps()
        """
        ...


class SavingsAccount:
    def __init__(self, accumulation: int):
        """
        Создание и подготовка к работе объекта "Накопительный счет"

        :param accumulation: Накопления

        Примеры:
        >>> savings_account = SavingsAccount(115000)  # инициализация экземпляра класса
        """
        if not isinstance(accumulation, int):
            raise TypeError("Накопления должны быть типа int")
        if accumulation < 0:
            raise ValueError("Накопления не могут быть отрицательным числом ")
        self.accumulation = accumulation

    def add_to_account(self, replenishment: int) -> None:
        """
        Пополнение накопительного счета

        :param replenishment: Сумма пополнения

        :return: Сумма денег на счете после пополнения

        Примеры:
        >>> savings_account = SavingsAccount(115000)
        >>> savings_account.add_to_account(20000)
        """
        if not isinstance(replenishment, int):
            raise TypeError("Сумма пополнения должна быть типа int")
        if replenishment <= 0:
            raise ValueError("Сумма пополнения должна быть положительным числом ")
        ...

    def withdrawal_from_account(self, withdrawals: int) -> None:
        """
        Снятие денег с накопительного счета

        :param withdrawals: Сумма снятия

        :raise ValueError: Если сумма снятия превышает остаток на накопительном счете

        :return: Остаток денег на счете

        Примеры:
        >>> savings_account = SavingsAccount(115000)
        >>> savings_account.withdrawal_from_account(15000)
        """
        if not isinstance(withdrawals, int):
            raise TypeError("Сумма снятия должна быть типа int")
        if withdrawals <= 0:
            raise ValueError("Сумма снятия должна быть положительным числом ")
        ...


class University:
    def __init__(self, my_points: int):
        """
        Создание и подготовка к работе объекта "Университет"

        :param my_points: Мои баллы ЕГЭ

        Примеры:
        >>> university = University(251)  # инициализация экземпляра класса
        """
        if not isinstance(my_points, int):
            raise TypeError("Баллы ЕГЭ должны быть типа int")
        if my_points < 0:
            raise ValueError("Баллы ЕГЭ не могут быть отрицательным числом ")
        self.my_points = my_points

    def ability_to_apply(self, minimum_points: int) -> bool:
        """
        Функция, которая проверяет хватает ли баллов для подачи документов в ВУЗ

        :param minimum_points: Минимальный проходной балл

        :return: Возможно ли подать документы

        Примеры:
        >>> university = University(251)
        >>> university.ability_to_apply(135)
        """
        if not isinstance(minimum_points, int):
            raise TypeError("Минимальный проходной балл должен быть типа int")
        if minimum_points <= 0:
            raise ValueError("Минимальный проходной балл должен быть положительным числом ")
        ...

    def ability_to_enter(self, lowest_points: int) -> bool:
        """
        Функция, которая проверяет выше ли наш балл, чем балл абитуриента, занимающего последнее бюджетное место

        :param lowest_points: Балл абитуриента, занимающего последнее бюджетное место

        :return: Возможно ли занять бюджетное место

        Примеры:
        >>> university = University(251)
        >>> university.ability_to_apply(248)
        """
        if not isinstance(lowest_points, int):
            raise TypeError("Балл абитуриента должен быть типа int")
        if lowest_points <= 0:
            raise ValueError("Балл абитуриента должен быть положительным числом ")
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    pass
