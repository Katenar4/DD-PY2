if __name__ == "__main__":
    class Fitness:
        def __init__(self, name: str, address: str, months: int, monthly_cost: int):
            """
            Инициализация базового класса

            :param name: Имя клиента
            :param address: Адрес фитнесс-клуба,в котором приобретен абонемент
            :param months: Длительность абонемента
            :param monthly_cost: Стоимость абонемента на месяц
            """
            self.name = name
            self._address = address  # Адрес фитнесс-клуба не может меняться
            self.months = months
            self.monthly_cost = monthly_cost

        @property
        def address(self) -> str:
            return self._address

        def __str__(self) -> str:
            return f"Клиент: {self.name}. Адресс: Фитнес-дом.{self._address}. Длительность: {self.months}"

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(name={self.name!r}, address={self._address!r}, months={self.months}, " \
                   f"monthly_cost={self.monthly_cost} "

        def price(self) -> int:
            """
            Расчет стоимости абонемента на месяц

            :return: Стоимость абонемента
            """

            return self.months * self.monthly_cost


    class Premium(Fitness):
        def __init__(self, name: str, address: str, months: int, monthly_cost: int, regular_customer: bool):
            """
            Инициализация дочернего класса

            :param regular_customer: Является ли клиент постоянным
            """
            super().__init__(name, address, months, monthly_cost)
            if regular_customer is not True:
                raise ValueError("Клиент не является постоянным")
            self.regular_customer = regular_customer

        def __str__(self) -> str:
            return f"Клиент: {self.name}. Адресс: Фитнес-дом.{self._address}. Длительность: {self.months}. " \
                       f"Постоянный клиент "

        def __repr__(self):
            return f"{self.__class__.__name__}(name={self.name!r}, address={self._address!r}, months={self.months}, " \
                   f"monthly_cost={self.monthly_cost}, regular_customer={self.regular_customer} "

        def premium_price(self, discount: int) -> float:
            """
            Расчет стоимости абонемента на месяц с учетом скидки постоянного клиента

            :param discount: Размер скидки, преедоставляемой постоянным клиентам

            :return: Пересчитанная стоимость абонемента
            """

            return super().price() * (100 - discount) / 100
pass

