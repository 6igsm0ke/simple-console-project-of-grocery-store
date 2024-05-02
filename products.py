class Products:
    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} ${self.price} {self.quantity} kg/l/piece(s)"


class Drinks(Products):
    dd = {
        1: Products("Water", 1.5),
        2: Products("Juice", 2.0)}


class Fruits(Products):
    dd = {
        1: Products("Apple", 1.2),
        2: Products("Banana", 0.8),
        3: Products("Orange", 1.0)}


class HouseholdItems(Products):
    dd = {
        1: Products("Dish soap", 3.5),
        2: Products("Sponge", 1.0),
        3: Products("Trash bags", 5.0)}


class MeatProducts(Products):
    dd = {
        1: Products("Chicken breast", 6.0),
        2: Products("Beef steak", 8.0),
        3: Products("Pork chops", 7.5)}


class MilkProducts(Products):
    dd = {
        1: Products("Milk", 2.5),
        2: Products("Cheese", 3.0),
        3: Products("Yogurt", 1.8)}


class Snacks(Products):
    dd = {
        1: Products("Potato Chips", 2.5),
        2: Products("Chocolate Bar", 1.8),
        3: Products("Trail Mix", 3.0)}


class Vegetables(Products):
    dd = {
        1: Products("Carrot", 1.0),
        2: Products("Tomato", 1.5),
        3: Products("Broccoli", 2.0)}


class PersonalHygieneItems(Products):
    dd = {
        1: Products("Toothpaste", 2.0),
        2: Products("Shampoo", 4.5),
        3: Products("Soap", 1.5)}