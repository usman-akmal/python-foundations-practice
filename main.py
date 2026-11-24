# wallet_balance = 1500
# item_price = 2000

# if wallet_balance >= item_price:
#     new_balance = wallet_balance - item_price
#     print(f"Purchase successful, your new balance is: {new_balance}")
# else:
#     print(f"Insufficient balance. you need {item_price - wallet_balance} more to make this purchase.")

# minimum_age = 18
# user_age = 20

# if user_age >= minimum_age:
#     print(f"Access granted. You are allowed to book a riding service.")
# else:
#     print(f"Access denied. You must be at least {minimum_age} years old to book a riding service.")

# user_role = "guest"

# if user_role == "admin":
#     print(f"Access granted, you can view, edit or delete all the records.")
# elif user_role == "editor":
#     print(f"Access granted, you can view and edit the records.")
# elif user_role == "viewer":
#     print(f"Access granted, you can only view the records.")
# else:
#     print(f"Access denied, you do not have the permissions to access the records, Please login with a valid account.")

# # Create a variable named cart_total and set it to 750.
# # Write an if / elif / else structure to determine the shipping_cost:
# # If cart_total is 1000 or more, the shipping is free (0).
# # Else if (elif) cart_total is 500 or more (but less than 1000), the shipping is 150.
# # Else (for anything under 500), the shipping is 300.
# # Store the result in a new variable called shipping_cost.
# # Print an f-string that says: "Your cart total is {cart_total} PKR. Your shipping cost is {shipping_cost} PKR."

# cart_total = 750
# shipping_cost = 0

# if cart_total >= 1000:
#     shipping_cost = 0
# elif cart_total >= 500:
#     shipping_cost = 150
# else:
#     shipping_cost = 300

# print(f"Your cart total is {cart_total} PKR. Your shipping cost is {shipping_cost} PKR.")

# user_names = ["Ali", "Usman", "Sara"]

# for name in user_names:
#     if name == "Ali":
#         print(f"Hello {name}, welcome back!")
#     elif name == "Usman":
#         print(f"Hello {name}, how have you been?")
#     elif name == "Sara":
#         print(f"Hello {name}, it's great to see you!")
#     else:
#         print(f"Hello {name}, welcome!")

# user_age = [15, 22, 17, 30, 12, 19]
# for age in user_age:
#     if age >= 18:
#         print(f"User aged {age} is an Adult.")
#     else:
#         print(f"User aged {age} is a Minor.")


# product = {
#     "name" : "Mechanical Keyboard",
#     "price": 3500,
#     "inStock": True 
# }

# print(f"Product Name: {product['name']}.")
# print(f"Product Price: {product['price']} PKR.")
# print(f"Product availability: {'In Stock' if product['inStock'] else 'Out of Stock'}.")

# # Create a dictionary named user_profile.
# # Give it exactly these four keys and values:
# # "username" with the value "ali_dev"
# # "role" with the value "editor"
# # "login_count" with the value 5
# # "is_active" with the value True
# # Write an f-string that prints: "User ali_dev is an editor and has logged in 5 times." (Hint: Use the dictionary keys to pull the data dynamically, don't just type the words!)
# # Finally, simulate the user logging in again by updating the "login_count" to 6, and print the new count.

# user_profile = {
#     "user_name" : "ali_dev",
#     "role": "editor",
#     "login_count": 5,
#     "is_active": True
# }

# print(f"User {user_profile['user_name']} is an {user_profile['role']} and has logged in {user_profile['login_count']} times.")

# user_profile["login_count"] += 1
# print(f"User {user_profile['user_name']} is a {user_profile['role']} and has logged in {user_profile['login_count']} times.")

# employees = [
#     {"name": "Usman", "age": 22, "designation": "AI-Ingineer"},
#     {"name": "Sarah", "age": 20, "designation": "Software Engineer"}
# ]

# for emp in employees:
#     print(f"Employee Name: {emp['name']}, is {emp['age']} years old and works as a {emp['designation']} at Folio 3.")

# Create a list named cart_items containing exactly 3 dictionaries.
# Each dictionary must have two keys: "item_name" (a string) and "price" (a number).
# Make sure at least one item is over 1000 PKR, and at least one is under 1000 PKR.
# Write a for loop to iterate through cart_items. Let's call our temporary variable item.
# Inside the loop, write an if/else statement checking the price:
# If the price is 1000 or more, print an f-string: "{item_name} is a PREMIUM item."
# Else, print an f-string: "{item_name} is a STANDARD item."
# (Hint: Remember to use the item dictionary to pull out the item_name and price dynamically!)

# cart_items = [
#     {"item_name": "Chicken Tikka", "price": 1200},
#     {"item_name": "Beef Burger", "price": 800},
#     {"item_name": "Coffee Mug", "price": 500}
# ]
# for item in cart_items:
#     if item['price'] >= 1000:
#         print(f"{item['item_name']} is a premium item.")
#     else:
#         print(f"{item['item_name']} is a standard item.")

def calculate_discounted_price(original_price, discount_percentage):
    discounted_amount = original_price * (discount_percentage / 100)
    actual_amount = original_price - discounted_amount
    return actual_amount

final_price_1 = calculate_discounted_price(2000, 20)

print(f"The amount that you are supposed to pay after {20}% discount is : {final_price_1} PKR.")

# Define a function named check_voting_eligibility.
# It should take one parameter: age.
# Inside the function, write an if/else statement:
# If age is 18 or older, return the string "Eligible to vote".
# Else, return the string "Not eligible to vote".
# Below the function, create a list of ages: [16, 18, 21, 15, 30].
# Write a for loop to go through the list of ages.
# Inside the loop, call your function, passing in the current age. Store the returned result in a variable called status.
# Print an f-string: "Age {age}: {status}"

def check_voting_eligibility(age):
    if age >= 18:
        return "You are eligible to vote."
    else:
        return "You are not eligible to vote."

ages = [16, 18, 21, 15, 30]

for age in ages:
    status = check_voting_eligibility(age)
    print(f"You are {age} years old, so you are {status}")

# Define a function named check_driving_eligibility.
# The function should take one parameter: age.
# Inside the function, write an if/else statement:
# If age is 18 or older, return "Eligible to drive".
# Otherwise, return "Not eligible to drive".
# Below the function, create a list of ages: [14, 19, 17, 25, 16].
# Write a for loop to go through the list.
# Inside the loop:
# Call your function, passing the current age.
# Store the returned result in a variable called status.
# Print an f-string in this format:
# python
# Age {age}: {status}

def check_driving_eligibility(age):
    if age >= 18:
        return "Eligible to drive"
    else:
        return "Not eligible to drive"

ages = [14, 19, 17, 25, 16]

for age in ages:
    status = check_driving_eligibility(age)
    print(f"Age {age}: {status}")

    








 







    