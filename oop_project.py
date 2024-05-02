import random
from datetime import datetime
from products import Products, Drinks, \
    Fruits, Vegetables, Snacks, MeatProducts, MilkProducts, HouseholdItems, \
    PersonalHygieneItems


class InvalidNumber(Exception):
    """Custom exception for invalid input numbers."""
    pass


class Menu:
    """Class representing the grocery store menu."""

    def __init__(self):
        """Initialize the menu and cart."""
        self.categories = {
            1: {'name': 'Drinks', 'class': Drinks},
            2: {'name': 'Fruits', 'class': Fruits},
            3: {'name': 'Vegetables', 'class': Vegetables},
            4: {'name': 'Snacks', 'class': Snacks},
            5: {'name': 'Meat products', 'class': MeatProducts},
            6: {'name': 'Milk products', 'class': MilkProducts},
            7: {'name': 'Household items', 'class': HouseholdItems},
            8: {'name': 'Personal hygiene items', 'class': PersonalHygieneItems}
        }
        self.cart = Cart()

    def print_categories(self):
        """Print the available product categories."""
        print('\n'.join([f"{idx}. {category_info['name']}"
                         for idx, category_info in self.categories.items()]))
        print('99. Cart', '0. Quit', sep='\n')

    def run(self):
        """Run the menu loop."""
        while True:
            try:
                self.print_categories()
                choice = int(input('Enter the number of the type of product you want or 0 to quit: '))
                if choice == 0:
                    if len(self.cart.shopping_cart) == 0:
                        print('Your cart is empty.')
                        ext = int(input('Are you leaving us?(1:yes, 2: no): '))
                        if ext == 1:
                            print('Thank you for visiting our grocery store!')
                            break
                        elif ext == 2:
                            continue
                        else:
                            raise InvalidNumber
                    else:
                        print(self.cart.menu_title(),
                              self.cart.shopping_cart, '-' * 50,
                              f'Total: ${self.cart.calculator()}', sep='\n')
                        payment = int(input(
                            'Are you sure you want to complete your purchase and proceed to payment?(1:Yes 2: No): '))
                        if payment == 1:
                            total = self.cart.calculator()
                            now = datetime.now()
                            formatted_date_time = now.strftime("%d-%m-%Y %H:%M:%S")
                            if payment == 1:
                                print('Your check:', self.cart.menu_title(),
                                      self.cart.shopping_cart, '-' * 50,
                                      f'Processing payment for ${total}',
                                      f'Total: ${total}', '...', 'Payment is successful',
                                      f'Your cashier is {random.choice(cashiers)}',
                                      formatted_date_time,
                                      'Thank you for visiting our grocery store!', sep='\n')
                            break
                        elif payment == 2:
                            continue
                        else:
                            raise InvalidNumber
                elif choice == 99:
                    if len(self.cart.shopping_cart) == 0:
                        print('Your cart is empty.')
                    else:
                        print('Your current check:')
                        print(self.cart.menu_title(), self.cart.shopping_cart, '-' * 50,
                              f'Total: ${self.cart.calculator()}',
                              '-' * 50,
                              '0. Back', sep='\n')
                    editor = int(input('Enter number of product that you want edit/delete or 0 to go back: '))
                    if editor == 0:
                        continue
                    elif editor in range(1, len(self.cart.shopping_cart) + 1):
                        edit_or_delete = int(input('Do you want to delete or edit(1:to delete, 2:to edit): '))
                        if edit_or_delete == 1:
                            self.cart.remove_from_cart(editor)
                        elif edit_or_delete == 2:
                            quan = int(input('Enter the number to change the quantity: '))
                            self.cart.edit_quantity(editor, quan)
                        else:
                            raise InvalidNumber
                    elif len(self.cart.shopping_cart) == 0:
                        print('-' * 30, 'Your cart is empty.', '-' * 30, sep='\n')
                elif choice in self.categories:
                    category = self.categories[choice]['class'].dd
                    print(
                        f'You selected {self.categories[choice]["name"]} category',
                        '-' * 30,
                        f"{'ID':<5}{'PRODUCT':^7}{'PRICE':>13}",
                        '-' * 30, sep='\n')
                    for idx, (product_number, product) in enumerate(category.items(), start=1):
                        print(f"{idx:<5}{product.name:<14} ${product.price:<5.2f}")
                    print('-' * 30, '0. Back', sep='\n')
                else:
                    raise InvalidNumber
                product_choice = int(input(
                    'Enter the number of the product you want or 0 to go back: '))
                if product_choice == 0:
                    continue
                elif product_choice in self.categories[choice]['class'].dd:
                    quantity = int(input('Enter the quantity or kilogram you want: '))
                    product1 = self.categories[choice]['class'].dd[product_choice]
                    self.cart.shopping_cart = (product1, quantity)
                else:
                    raise InvalidNumber
            except ValueError or KeyError:
                print('Invalid input! Please enter a valid number.')
            except InvalidNumber as e:
                print('Invalid input! Please enter a valid number.', e)


class Cart:
    """Class representing the shopping cart."""

    def __init__(self):
        self._products = []
        self._menu_title = []

    @property
    def shopping_cart(self):
        """Return a formatted string of the current shopping cart."""
        cart_items = [
            *[f"{idx:<5} {product['Name']:<16}$"
              f"{product['Price']:<8}{product['Quantity'][0]} {product['Quantity'][1]}"
              for idx, product in enumerate(self._products, start=1)],
        ]

        return "\n".join(cart_items)

    @shopping_cart.setter
    def shopping_cart(self, product_quantity_tuple):
        """Add a product to the shopping cart."""
        product, quantity = product_quantity_tuple
        if isinstance(product, Products) and isinstance(quantity, int):
            self._products.append({
                'Name': product.name,
                'Price': product.price,
                'Quantity': [quantity, 'kg/l/piece(s)']})
            print(f'{product.name} added to cart')
        else:
            print('Invalid product. Please provide a valid product object.')

    def menu_title(self):
        menu_title = ['-' * 50,
                      f"{'ID':<6}{'PRODUCT':<16}{'PRICE':<9}{'QUANTITY':<12}",
                      '-' * 50]
        return "\n".join(menu_title)

    def remove_from_cart(self, num):
        """Remove a product from the shopping cart by index."""
        product_name = self._products[num - 1].get('Name')
        self._products.pop(num - 1)
        print(f"You deleted {product_name} from cart")

    def edit_quantity(self, num, num2):
        """Edit the quantity of a product in the shopping cart."""
        product = self._products[num - 1]
        product['Quantity'] = [num2, 'kg/l/piece(s)']
        print(f'You edited quantity of {product.get("Name")}')

    def calculator(self):
        """Calculate the total cost of items in the shopping cart."""
        total = 0
        for i in range(len(self._products)):
            total += self._products[i]['Price'] * self._products[i]['Quantity'][0]
        return round(total, 3)


def hello_message(name):
    """Print a welcome message."""
    print(f'Hello {name}, welcome to our grocery store!')
    print('Here is types of product:')


cashiers = ['Kosbayev Adilet', 'Talgatov Yerassyl']

if __name__ == "__main__":
    Name = input('Enter your full name: ')
    hello_message(Name)
    menu = Menu()
    menu.run()
