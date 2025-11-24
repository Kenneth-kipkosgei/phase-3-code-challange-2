# debug.py

# 1. Import all necessary classes
from customer import Customer
from coffee import Coffee
from order import Order

print("--- COFFEE SHOP DOMAIN MODEL TESTING ---")

# --- Setup Data ---
# Reset the class lists for a clean run, useful for iterative testing
Order.all = []
Customer.all = []
Coffee.all = []

# A. Create Coffees (Test Coffee.name validation implicitly)
print("\n--- 1. Creating Entities ---")
try:
    espresso = Coffee("Espresso")
    latte = Coffee("Vanilla Latte")
    drip = Coffee("House Drip")
    print(f"Created Coffees: {Coffee.all}")
except Exception as e:
    print(f"Error creating Coffee: {e}")

# B. Create Customers (Test Customer.name validation implicitly)
try:
    alice = Customer("Alice")
    bob = Customer("BobTheBuilder")
    charlie = Customer("Charlie")
    print(f"Created Customers: {Customer.all}")
except Exception as e:
    print(f"Error creating Customer: {e}")


# C. Create Orders (Using Customer.create_order)
print("\n--- 2. Creating Orders ---")

# Alice's orders (Total spending: 3.50 + 5.00 + 3.50 = 12.00)
order1 = alice.create_order(espresso, 3.50) # Alice Order 1
order2 = alice.create_order(latte, 5.00)    # Alice Order 2
order3 = alice.create_order(espresso, 3.50) # Alice Order 3

# Bob's orders (Total spending: 4.50 + 4.50 + 2.00 = 11.00)
order4 = bob.create_order(latte, 4.50)      # Bob Order 1
order5 = bob.create_order(latte, 4.50)      # Bob Order 2
order6 = bob.create_order(drip, 2.00)       # Bob Order 3

# Charlie's orders (Total spending: 3.25 + 3.25 + 5.50 = 12.00)
order7 = charlie.create_order(espresso, 3.25)# Charlie Order 1
order8 = charlie.create_order(espresso, 3.25)# Charlie Order 2
order9 = charlie.create_order(latte, 5.50)   # Charlie Order 3

print(f"Total Orders Created: {len(Order.all)}")
# print(Order.all) # Uncomment to view all Order objects


# --- Test Customer Relationship/Aggregate Methods (Steps 5, 6, 7) ---
print("\n--- 3. Testing Customer Methods (Alice) ---")
print(f"Alice's Orders (orders()): {len(alice.orders())}") # Expected: 3
print(f"Alice's Coffees (coffees()): {alice.coffees()}") # Expected: [Espresso, Vanilla Latte]

print("\n--- 4. Testing Coffee Methods (Latte) ---")
print(f"Latte's Orders (orders()): {len(latte.orders())}") # Expected: 4
print(f"Latte's Customers (customers()): {latte.customers()}") # Expected: [Alice, Bob, Charlie]
print(f"Latte's Num Orders (num_orders()): {latte.num_orders()}") # Expected: 4
# Expected Average: (5.00 + 4.50 + 4.50 + 5.50) / 4 = 4.875
print(f"Latte's Average Price (average_price()): ${latte.average_price():.2f}") 


# --- Test most_aficionado Class Method (Step 7) ---
print("\n--- 5. Testing most_aficionado ---")

# Espresso spending: Alice (7.00), Charlie (6.50). Expected: Alice
aficionado_espresso = Customer.most_aficionado(espresso)
print(f"Most Aficionado for Espresso: {aficionado_espresso.name}") 

# Latte spending: Alice (5.00), Bob (9.00), Charlie (5.50). Expected: Bob
aficionado_latte = Customer.most_aficionado(latte)
print(f"Most Aficionado for Latte: {aficionado_latte.name}") 


# --- Test Validation/Exceptions (Step 9) ---
print("\n--- 6. Testing Validation (Exceptions) ---")

# A. Invalid Customer Name (too long)
try:
    Customer("ThisNameIsWayTooLong")
except Exception as e:
    print(f"Customer Error (Name Length): {e}")

# B. Invalid Price (too high)
try:
    alice.create_order(drip, 15.00)
except Exception as e:
    print(f"Order Error (Price Range): {e}")

# C. Invalid Coffee Name (too short)
try:
    Coffee("a")
except Exception as e:
    print(f"Coffee Error (Name Length): {e}")

# D. Invalid Order Object Type (e.g., passing a string instead of a Coffee object)
try:
    Order(alice, "not_a_coffee_object", 5.00)
except Exception as e:
    print(f"Order Error (Object Type): {e}")