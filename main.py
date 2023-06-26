import products
import store
import promotions


class humberto_store:
    def __init__(self):

        self.product_list = [
            products.Product("Dumbbells 50kg", price=550, quantity=100),
            products.Product("Barbells 20kg", price=150, quantity=300),
            products.Product("Retract bench", price=50, quantity=100),
            products.Limited("Smith machine", price=1450, quantity=2, maximum=3),
            products.Non_Stocked("strappers", price=50)
        ]

        second_half_price = promotions.SecondHalfPrice("Second Half price!")
        third_one_free = promotions.ThirdFree("Third One Free!")
        thirty_percent = promotions.Percentage("30% off!", percent=30)

        self.product_list[0].set_promotion(second_half_price)
        self.product_list[1].set_promotion(third_one_free)
        self.product_list[3].set_promotion(thirty_percent)

        self.items = store.Store(self.product_list)

    def show_product_list(self):
        print("--Product List---")
        for product in self.product_list:
            print(f"Product: {product.show_product()}")
        print("------------")

    def show_product_list_for_order(self):
        print("--Available Gym Items---")
        for product in self.product_list:
            print(f"Product: {product.show_product()}")
        print("\n")

    def show_total_amount(self):
        total = self.items.get_total_quantity()
        print(f"Total items in store: {int(total)} \n")

    def show_menu(self) -> str:
        print("*********** My Gym Store - Humberto's  ********** \n")
        print("Menu: ")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Check if product exists")
        print("5. Exit\n")

    def check_if_product_exists(self):
        product_name = input("Enter the product name: ")
        exists = any(product.name.lower() == product_name.lower() for product in self.items.products)
        if exists:
            print(f"The product '{product_name}' exists in the store.\n")
        else:
            print(f"The product '{product_name}' does not exist in the store.\n")

    def make_order(self):
        order_list = []
        names = []
        for product in self.product_list:
            name = product.show_product_name()
            names.append(name)
        names
        print("Write Exit to finish the order")

        while True:
            product_name = input("Select the product name: ")
            if product_name == 'Exit':
                break

            try:
                if product_name not in names:
                    raise ValueError("We dont have that product, please try again")
            except ValueError as error:
                print(f"Error: {str(error)}")
                continue

            quantity = input(f"We do have {product_name}. Enter the quantity: ")
            try:
                quantity = int(quantity)
                if quantity <= 0:
                    raise ValueError("Invalid quantity. Please enter a positive quantity.")
            except ValueError as error:
                print(f"Error: {str(error)}")
                continue
            for product in self.product_list:
                pdict = product.product_dict()
                p_name = pdict['name']
                p_quantity = pdict['quantity']
                if product_name in p_name:
                    if p_quantity >= quantity:
                        order_list.append((p_name, quantity, p_quantity, product.buy(quantity)))
                        print("Product added to the order list!")
                    else:
                        print("Insufficient quantity available!")
            order_list

        try:
            print("**********")
            print("Your order is formed by :")
            sumatory = 0
            for p_name, quantity, p_quantity, total_per_product in order_list:
                print(f"{p_name} with the quantity of {quantity} wich totalizes ${total_per_product}")
                sumatory += total_per_product
            print(f"Total order amount is ${sumatory}")
            print("**********")
        # Add exception handling for unexpected errors
        except ValueError as error:
            print(f"Error: {str(error)}")

    def start(self):
        while True:
            self.show_menu()
            option = ''
            try:
                option = int(input('Please insert a number between 1 and 5: '))
            except TypeError:
                print('Wrong input. Please enter a number ...')
            # Check what choice was entered accordingly
            if option == 1:
                self.show_product_list()
            elif option == 2:
                self.show_total_amount()
            elif option == 3:
                self.make_order()
            elif option == 4:
                self.check_if_product_exists()
            elif option == 5:
                print('Thanks for visiting!')
                exit()
            else:
                print('Invalid option. Please enter a number between 1 and 4.')


if __name__ == "__main__":
    # initiate the class
    hs = humberto_store()
    hs.start()
