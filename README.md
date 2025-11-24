# Coffee Shop Domain Model

A Python implementation of a coffee shop domain model with Customer, Coffee, and Order classes.

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