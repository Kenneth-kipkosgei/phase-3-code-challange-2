class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self._customer = None
        self._coffee = None
        self._price = None

        self.customer = customer
        self.coffee = coffee
        self.price = price

        Order.all.append(self)

    @property
    def customer(self):
        """Getter for the Customer instance."""
        return self._customer

    @customer.setter
    def customer(self, customer_instance):
        from customer import Customer
        if isinstance(customer_instance, Customer):
            self._customer = customer_instance
        else:
            raise Exception("Customer must be a Customer instance.")

    @property
    def coffee(self):
        """Getter for the Coffee instance."""
        return self._coffee

    @coffee.setter
    def coffee(self, coffee_instance):
        from coffee import Coffee
        if isinstance(coffee_instance, Coffee):
            self._coffee = coffee_instance
        else:
            raise Exception("Coffee must be a Coffee instance.")

    @property
    def price(self):
        """Getter for the price."""
        return self._price

    @price.setter
    def price(self, price_value):
        """Setter for price. Must be a float/int between 1.0 and 10.0."""
        if isinstance(price_value, (float, int)) and 1.0 <= price_value <= 10.0:
            self._price = float(price_value)
        else:
            raise Exception("Price must be a float or integer between 1.0 and 10.0.")

    def __repr__(self):
        """Helper for clean representation in a debugger."""
        return f"<Order customer='{self.customer.name}' coffee='{self.coffee.name}' price={self.price}>"