# Coffee Shop Domain Model

A Python implementation of a coffee shop domain model with Customer, Coffee, and Order classes.

## About

This project demonstrates object-oriented programming principles in Python by modeling a coffee shop's core business entities. It implements proper class relationships, data validation, and aggregate methods to manage customers, coffee types, and orders efficiently.

## Classes

- **Customer**: Manages customer data and orders
- **Coffee**: Represents coffee types and pricing
- **Order**: Links customers to coffees with prices

## Usage

```python
from customer import Customer
from coffee import Coffee

# Create entities
customer = Customer("Alice")
coffee = Coffee("Espresso")

# Create order
order = customer.create_order(coffee, 3.50)

# Get customer's orders and coffees
print(customer.orders())
print(customer.coffees())

# Get coffee statistics
print(coffee.num_orders())
print(coffee.average_price())
```

## Testing

Run `python debug.py` to test all functionality.

## Author

Kenneth Kipkosgei