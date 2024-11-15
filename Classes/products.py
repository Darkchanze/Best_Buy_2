class Product:


    def __init__(self, name, price, quantity):
        """Get name price and quantity from user and check for valid input with exceptions.
        Set active of new item to default True."""
        self.name = str(name)
        if self.name == "":
            raise ValueError("Name must not be empty")
        try:
            self.price = float(price)
        except (ValueError, TypeError):
            raise ValueError("Price must be a valid number")
        if self.price < 0:
            raise ValueError("Price must be greater than 0")
        self.set_quantity(quantity)
        self.active = True


    def get_quantity(self):
        """Getter function for quantity.
        Returns the quantity (float)."""
        return self.quantity


    def set_quantity(self, quantity):
        """Setter function for quantity with try except
        If quantity reaches 0, deactivates the product."""
        try:
            self.quantity = int(quantity)
        except (ValueError, TypeError):
            raise ValueError("Invalid quantity provided")
        if self.quantity < 0:
            raise ValueError("Quantity must not be negative")
        if self.quantity == 0:
            self.deactivate()



    def is_active(self):
        """Getter function for active.
        Returns True if the product is active, otherwise False."""
        return self.active


    def activate(self):
        """Activates the product."""
        self.active = True


    def deactivate(self):
        """Deactivates the product."""
        self.active = False


    def show(self):
        """Returns a string that presents the product"""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"


    def buy(self, quantity):
        """Get a quantity and check if its to high or negative. Decrease self.quantity by the
        bought amount and return the price of purchase."""
        if quantity > self.quantity:
            raise ValueError("Quantity is too high")
        if quantity < 0:
            raise ValueError("Quantity must not be negative")
        self.set_quantity(self.quantity - quantity)
        return self.price * quantity


    def __str__(self):
        return f"{self.name}"