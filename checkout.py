from datetime import datetime
from Product import Product


class CheckoutRegister():
    def __init__(self):
        self.__product_list = []
        self.__shopping_cart = []
        self.init()
        self.__total_payment = 0
        self.__amount_received = 0
        self.__amount_due = 0

    # read product file
    def init(self):
        print("Welcome to our supermarket")
        try: 
            file = open('products.txt', 'rt')
            lines = file.readlines()

            # spliting word in each line
            for line in lines:
                word = line.strip().split(",")
                # removing whitespace in single word
                bar_code, product_name, desc, price = [item.strip() for item in word]
                # create a new product object
                product = Product(bar_code, product_name, desc, float(price))
                # append product code into product list
                self.__product_list.append(product)
            file.close()
        except FileNotFoundError:
            print("File is not found")

    # print product list
    def print_product(self):
        for p in self.__product_list:
            print(p)

    #scanning item method
    def scan_item(self, bar_code):
        for each_product in self.__product_list:
            if each_product.get_bar_code() == bar_code:
                self.__shopping_cart.append(each_product)
                return f'{each_product.get_product_name()} - ${each_product.get_product_price()}'
        return "product not found"


    #accepting payment method
    def get_total_payment(self):
        for each_product in self.__shopping_cart:
            self.__total_payment += each_product.get_product_price()
        return self.__total_payment

    def accept_payment(self, amount_paid):
        self.__amount_received += amount_paid
        self.__amount_due = self.__total_payment - self.__amount_received
        return self.__amount_due


    #print receipt method
    def print_receipt(self):
        print("\n----- Final Receipt -----\n")
        for product in self.__shopping_cart:
            print(f'{product.get_product_name()} ${str(product.get_product_price())}')
        print(f'\nTotal amount: ${str(self.__total_payment)}')
        print(f'Amount received: ${str(self.__amount_received)}')
        print(f'Change given: ${str(self.__amount_received - self.__total_payment)}')
        print('Thank you for shopping!')

    #save transaction method
    def save_transaction(self):
        now = datetime.now()  #get current time
        date = now.strftime("%d/%m/%Y %H:%M:%S") # convert current time to string
        total_payment = str(self.__total_payment)
        output = (date + " " + "Total payment = $" + total_payment + "\n")

        file = open('saleTransaction.txt', 'a') #open file
        file.write(str(output)) #write on file
        file.close()
        self.reset_data() #reset data for next transaction

    #reset data
    def reset_data(self):
        self.__total_payment = 0
        self.__amount_received = 0
        self.__amount_due = 0
        self.__shopping_cart = []

