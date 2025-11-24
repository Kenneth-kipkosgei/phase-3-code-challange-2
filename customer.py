class Customer:
    all = []

    def __init__(self, name):
        self.name = name
        Customer.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise Exception("Name must be a string between 1 and 15 characters.")

    def orders(self):
        """Returns a list of all Order instances for this customer."""
        from order import Order
        return [order for order in Order.all if order.customer is self]

    def coffees(self):
        """Returns a unique list of Coffee instances that the customer has ordered."""
        return list(set([order.coffee for order in self.orders()]))

    def create_order(self, coffee, price):
        """Creates a new Order instance and associates it with this customer and the coffee."""
        from order import Order
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        """Returns the Customer instance that has spent the most money on the provided coffee."""
        from order import Order
        coffee_orders = [order for order in Order.all if order.coffee is coffee]
        
        if not coffee_orders:
            return None

        customer_spending = {}
        for order in coffee_orders:
            customer_spending[order.customer] = customer_spending.get(order.customer, 0) + order.price

        return max(customer_spending, key=customer_spending.get)

    def __repr__(self):
        return f"<Customer name='{self.name}'>"