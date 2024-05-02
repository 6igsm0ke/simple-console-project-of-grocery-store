class Products:
    """A class representing generic products."""
    def __init__(self, name, price, quantity=1):
        """Initialize a product with a name, price, and optional quantity."""
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        """Return a string representation of the product."""
        return f"{self.name} ${self.price} {self.quantity} kg/l/piece(s)"


class Drinks(Products):
    """A class representing various drinks."""
    dd = {
        1: Products("Water", 1.5),
        2: Products("Juice", 2.0),
        3: Products("Mojito", 2.5),
        4: Products("Coffee", 2.0),
        5: Products("Sweet Tea", 1.0)}

class Fruits(Products):
    """A class representing different fruits."""
    dd = {
        1: Products("Apple", 1.2),
        2: Products("Banana", 0.8),
        3: Products("Orange", 1.0),
        4: Products("Cherry", 0.5),
        5: Products("Lime", 1.5)}


class HouseholdItems(Products):
    """A class representing household items."""
    dd = {
        1: Products("Dish soap", 3.5),
        2: Products("Sponge", 1.0),
        3: Products("Trash bags", 5.0),
        4: Products("Toilet paper", 2.5),
        5: Products("Wipes", 2.0)}


class MeatProducts(Products):
    """A class representing various meat products."""
    dd = {
        1: Products("Chicken breast", 6.0),
        2: Products("Beef steak", 8.0),
        3: Products("Horsemeat", 9.0),
        4: Products("Sausage", 3.0),
        5: Products("Lamb meat", 6,5)}


class MilkProducts(Products):
    """A class representing different milk products."""
    dd = {
        1: Products("Milk", 2.5),
        2: Products("Cheese", 3.0),
        3: Products("Yogurt", 1.8),
        4: Products("Butter", 3.5),
        5: Products("Ice Cream", 1.0)}


class Snacks(Products):
    """A class representing snack items."""
    dd = {
        1: Products("Potato Chips", 2.5),
        2: Products("Chocolate Bar", 1.8),
        3: Products("Trail Mix", 3.0),
        4: Products("Popcorn", 2.0),
        5: Products("Cookie", 2.5)}


class Vegetables(Products):
    """A class representing various vegetables."""
    dd = {
        1: Products("Carrot", 1.0),
        2: Products("Tomato", 1.5),
        3: Products("Broccoli", 2.0),
        4: Products("Potatoes", 1.0),
        5: Products("Onion", 0.5)}


class PersonalHygieneItems(Products):
    """A class representing personal hygiene items."""
    dd = {
        1: Products("Toothpaste", 2.0),
        2: Products("Shampoo", 4.5),
        3: Products("Soap", 1.5),
        4: Products("Washcloth", 3.5),
        5: Products("Towels", 4.0)}
