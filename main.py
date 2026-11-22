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






 







    