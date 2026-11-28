import json


merchandise_response = (
    '{"status": "success", "event": "Python Marathon Live", '
    '"customer": "Usman", "items": ['
    '{"item_name": "Python T-shirt", "price": 1800}, '
    '{"item_name": "Code Notebook", "price": 700}, '
    '{"item_name": "Python Mug", "price": 1200}'
    ']}'
)
order_data = json.loads(merchandise_response)


def calculate_discounted_price(original_price, discount_percentage):
    discount_amount = original_price * (discount_percentage / 100)
    return original_price - discount_amount


cart_total = 0

print("Merchandise:")
for item in order_data["items"]:
    cart_total += item["price"]
    if item["price"] >= 1000:
        item_type = "PREMIUM"
    else:
        item_type = "STANDARD"

    print(f"{item['item_name']} - Rs. {item['price']} ({item_type})")

if cart_total >= 3000:
    discount_percentage = 10
else:
    discount_percentage = 0

discounted_cart_total = calculate_discounted_price(
    cart_total, discount_percentage
)

if cart_total >= 1000:
    shipping_cost = 0
elif cart_total >= 500:
    shipping_cost = 150
else:
    shipping_cost = 300

amount_due = discounted_cart_total + shipping_cost

receipt = {
    "event": order_data["event"],
    "customer": order_data["customer"],
    "merchandise_total": cart_total,
    "discount_percentage": discount_percentage,
    "shipping_cost": shipping_cost,
    "amount_due": amount_due
}

print("\nOrder receipt:")
print(json.dumps(receipt, indent=2))
