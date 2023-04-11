from csv import DictReader
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

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) < 11:
            self.__name = new_name
        else:
            print("Error length name more 10 characters")

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
        f_path = "C:/Users/gtsoktoeva001/PycharmProjects/electronics/electronics-shop-project/src/items.csv"

        try:
            with open(f_path) as csvfile:
                reader = DictReader(csvfile)
                for line in reader:
                    #print(cls,line)
                    cls(line["name"], line["price"], line["quantity"])

        except IOError as e:
            print(u'не удалось открыть файл')

    @staticmethod
    def string_to_number(string):

        if string.isdigit():
            return int(string)
        return int(float(string))

