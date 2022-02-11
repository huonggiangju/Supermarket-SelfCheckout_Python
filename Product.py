class Product:
    def __init__(self, bar_code, product_name, desc, price):
        self.__bar_code = bar_code
        self.__product_name = product_name
        self.__desc = desc
        self.__price = price

    def __str__(self):
        return f"{self.__bar_code}, {self.__product_name}, {self.__desc} - ${self.__price}"

    def get_bar_code(self):
        return self.__bar_code

    def get_product_name(self):
        return self.__product_name

    def get_product_price(self):
        return self.__price

    def get_product_desc(self):
        return self.__desc


    

