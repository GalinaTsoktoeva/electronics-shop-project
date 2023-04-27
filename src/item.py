from csv import DictReader
from exception_item import InstantiateCSVError
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)
        super().__init__()

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.name}"

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        raise Exception

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) < 11:
            self.__name = new_name
        else:
            raise Exception("Длина наименования товара превышает 10 символов")

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        """
        Считывает файл и создает экземпляры класса Item
        """
        f_path = "../src/items.csv"

        try:
            with open(f_path) as csvfile:
                reader = DictReader(csvfile)

                if len(reader.fieldnames) < 3:
                    raise InstantiateCSVError

                for line in reader:
                    cls(line["name"], line["price"], line["quantity"])

        except FileNotFoundError as e:
            print(f'Отсутствует файл item.csv')

    @staticmethod
    def string_to_number(string):
        """
        Переводит строку в целочисленное значение
        """
        if string.isdigit():
            return int(string)
        return int(float(string))

