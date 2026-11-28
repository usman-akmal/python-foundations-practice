attendees = [
    {"name": "Usman", "age": 22},
    {"name": "Sara", "age": 16},
    {"name": "Ahmed"}
]


def calculate_ticket_price(age):
    if age < 5:
        return 0
    elif age <= 17:
        return 300
    elif age <= 59:
        return 600
    else:
        return 250


ticket_total = 0

print("Python Marathon Live - Ticket Booking")

for attendee in attendees:
    try:
        age = attendee["age"]
    except KeyError:
        print(f"{attendee['name']}: Age not provided, ticket not booked.")
        continue

    ticket_price = calculate_ticket_price(age)
    ticket_total += ticket_price

    if ticket_price == 0:
        print(f"{attendee['name']} (age {age}): Free ticket")
    else:
        print(f"{attendee['name']} (age {age}): Rs. {ticket_price}")

print(f"Total ticket cost: Rs. {ticket_total}")
