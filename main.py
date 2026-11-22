wallet_balance = 1500
item_price = 2000

if wallet_balance >= item_price:
    new_balance = wallet_balance - item_price
    print(f"Purchase successful, your new balance is: {new_balance}")
else:
    print(f"Insufficient balance. you need {item_price - wallet_balance} more to make this purchase.")

minimum_age = 18
user_age = 20

if user_age >= minimum_age:
    print(f"Access granted. You are allowed to book a riding service.")
else:
    print(f"Access denied. You must be at least {minimum_age} years old to book a riding service.")

user_role = "guest"

if user_role == "admin":
    print(f"Access granted, you can view, edit or delete all the records.")
elif user_role == "editor":
    print(f"Access granted, you can view and edit the records.")
elif user_role == "viewer":
    print(f"Access granted, you can only view the records.")
else:
    print(f"Access denied, you do not have the permissions to access the records, Please login with a valid account.")

# Create a variable named cart_total and set it to 750.
# Write an if / elif / else structure to determine the shipping_cost:
# If cart_total is 1000 or more, the shipping is free (0).
# Else if (elif) cart_total is 500 or more (but less than 1000), the shipping is 150.
# Else (for anything under 500), the shipping is 300.
# Store the result in a new variable called shipping_cost.
# Print an f-string that says: "Your cart total is {cart_total} PKR. Your shipping cost is {shipping_cost} PKR."

cart_total = 750
shipping_cost = 0

if cart_total >= 1000:
    shipping_cost = 0
elif cart_total >= 500:
    shipping_cost = 150
else:
    shipping_cost = 300

print(f"Your cart total is {cart_total} PKR. Your shipping cost is {shipping_cost} PKR.")

user_names = ["Ali", "Usman", "Sara"]

for name in user_names:
    if name == "Ali":
        print(f"Hello {name}, welcome back!")
    elif name == "Usman":
        print(f"Hello {name}, how have you been?")
    elif name == "Sara":
        print(f"Hello {name}, it's great to see you!")
    else:
        print(f"Hello {name}, welcome!")

user_age = [15, 22, 17, 30, 12, 19]
for age in user_age:
    if age >= 18:
        print(f"User aged {age} is an Adult.")
    else:
        print(f"User aged {age} is a Minor.")







 







    