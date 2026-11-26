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

# def calculate_discounted_price(original_price, discount_percentage):
#     discounted_amount = original_price * (discount_percentage / 100)
#     actual_amount = original_price - discounted_amount
#     return actual_amount

# final_price_1 = calculate_discounted_price(2000, 20)

# print(f"The amount that you are supposed to pay after {20}% discount is : {final_price_1} PKR.")

# Define a function named check_voting_eligibility.
# It should take one parameter: age.
# Inside the function, write an if/else statement:
# If age is 18 or older, return the string "Eligible to vote".
# Else, return the string "Not eligible to vote".
# Below the function, create a list of ages: [16, 18, 21, 15, 30].
# Write a for loop to go through the list of ages.
# Inside the loop, call your function, passing in the current age. Store the returned result in a variable called status.
# Print an f-string: "Age {age}: {status}"

# def check_voting_eligibility(age):
#     if age >= 18:
#         return "You are eligible to vote."
#     else:
#         return "You are not eligible to vote."

# ages = [16, 18, 21, 15, 30]

# for age in ages:
#     status = check_voting_eligibility(age)
#     print(f"You are {age} years old, so you are {status}")

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

# def check_driving_eligibility(age):
#     if age >= 18:
#         return "Eligible to drive"
#     else:
#         return "Not eligible to drive"

# ages = [14, 19, 17, 25, 16]

# for age in ages:
#     status = check_driving_eligibility(age)
#     print(f"Age {age}: {status}")

# Define a function named calculate_ticket_price.
# The function should take one parameter: age.
# Inside the function, use if/elif/else statements:
# If the age is below 5, return "Free Entry".
# If the age is between 5 and 17 (inclusive), return "Ticket Price: Rs. 300".
# If the age is between 18 and 59 (inclusive), return "Ticket Price: Rs. 600".
# Otherwise (age 60 or above), return "Ticket Price: Rs. 250".
# Below the function, create a list of ages:
# python
# ages = [3, 10, 18, 25, 62, 45, 7, 70]
# Write a for loop to iterate through the list.
# Inside the loop:
# Call your function using the current age.
# Store the returned result in a variable named status.
# Print the result using an f-string in this format:
# python
# Age {age}: {status}

# def calculate_ticket_price(age):
#     if age < 5:
#         return "Free Entry"
#     elif 5 <= age <= 17:
#         return "Ticket Price: Rs. 300"
#     elif 18 <= age <= 59:
#         return "Ticket Price: Rs. 600"
#     else:
#         return "Ticket Price: Rs. 250"

# ages = [3, 10, 18, 25, 62, 45, 7, 70]

# for age in ages:
#     status = calculate_ticket_price(age)
#     print(f"Age: {age}: {status}")

# userdata = {"name" : "Sarah", "age" : "21"}

# try:
#     user_role = userdata["role"]
#     print(f"User role : {user_role}")
# except KeyError:
#     print(f"User role is not defined in the dictionary or the database so we cannot retrieve the user_role")

# print("The application is still running despite the error.")

# Define a function named get_user_age that takes one parameter: user_data (a dictionary).
# Inside the function, write a try block:
# Try to access user_data["age"].
# If it works, return the age.
# Write an except KeyError block:
# If the key is missing, return the string "Age not provided".
# Below the function, create a list of two dictionaries:
# The first dictionary should have "name": "Sara" and "age": 25.
# The second dictionary should ONLY have "name": "Ahmed" (no age!).
# Write a for loop to iterate through the list.
# Inside the loop, call your get_user_age function, passing in the current dictionary. Store the result in a variable called age_status.
# Print an f-string: "User: {name}, Age Status: {age_status}" (Hint: You will need to pull the name out of the dictionary too!)

# def get_user_age(user_data):
#     try:
#         user_age = user_data["age"]
#         if(user_age):
#             return f"Age: {user_age}"
#     except KeyError:
#          return "The age is not provided."

# user_data = [
#     {"name" : "Sarah", "age": "21"},
#     {"name" : "Ahmed"}
    
# ]

# for employee in user_data:
#     age_status = get_user_age(employee)
#     print(f"User: {employee["name"]}, Age Status: {age_status}")

# import json

# python_user = {
#     "name" : "Usman",
#     "role": "admin",
#     "is_active": True
# }

# # I am converting this python dictionary into a json text
# json_string = json.dumps(python_user)
# print(json_string)

# # now i am converting this json text back to the python dictionary
# received_json = '{"name" : "Sarah", "age" : "25"}'
# python_dict = json.loads(received_json)
# print(python_dict["name"],python_dict["age"])

# Write a Python script that does the following:
# import json at the very top of your file.
# Create a variable named api_response that contains this exact JSON string:
# '{"status": "success", "data": {"user_id": 101, "credits": 50}}'
# (Notice it's a single string wrapped in single quotes, containing double quotes inside).
# Use json.loads() to convert api_response into a Python dictionary. Store it in a variable called parsed_data.
# Write an f-string that prints: "Status: {status}, User ID: {user_id}, Credits: {credits}" by extracting the values from parsed_data.
# (Hint: You will need to use nested dictionary keys like parsed_data['data']['user_id']).
# Finally, create a new Python dictionary named new_user with keys "name" and "is_verified" (set to True).
# Use json.dumps() to convert new_user into a JSON string and print it.

import json

api_response = '{"status": "success", "data": {"user_id": 101, "credits": 50}}'

parsed_data = json.loads(api_response)
print(f"Status: {parsed_data['status']}, User ID: {parsed_data['data']['user_id']}, Credits: {parsed_data['data']['credits']}")

new_user = {"name" : "Sarah","is_active": True}
json_string = json.dumps(new_user)
print(json_string)






    







    








 







    