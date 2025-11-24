class Coffee:
    all = []

    def __init__(self, name):
        self.name = name
        Coffee.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
        else:
            raise Exception("Name must be a string with at least 3 characters.")

    def orders(self):
        """Returns a list of all Order instances for that coffee."""
        from order import Order
        return [order for order in Order.all if order.coffee is self]

    def customers(self):
        """Returns a unique list of Customer instances who have ordered that coffee."""
        return list(set([order.customer for order in self.orders()]))

    def num_orders(self):
        """Returns the total number of times a coffee has been ordered."""
        return len(self.orders())

    def average_price(self):
        """Returns the average price for a coffee based on its orders."""
        coffee_orders = self.orders()
        
        if not coffee_orders:
            return 0.0
        
        total_price = sum(order.price for order in coffee_orders)
        return total_price / len(coffee_orders)

    def __repr__(self):
        return f"<Coffee name='{self.name}'>"