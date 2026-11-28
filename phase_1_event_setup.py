import json


event_response = (
    '{"status": "success", "event": {"name": "Python Marathon Live"}}'
)
event_data = json.loads(event_response)

user_profile = {
    "name": "Usman",
    "role": "viewer",
    "login_count": 5,
    "is_active": True
}

print(f"Event: {event_data['event']['name']}")

if event_data["status"] == "success":
    print("Event information loaded successfully.")
else:
    print("Event information could not be loaded.")

if user_profile["is_active"]:
    user_profile["login_count"] += 1
    print(
        f"Welcome, {user_profile['name']}! "
        f"You have logged in {user_profile['login_count']} times."
    )
else:
    print("Your account is inactive.")

if user_profile["role"] == "admin":
    print("Role access: You can manage the event.")
elif user_profile["role"] == "editor":
    print("Role access: You can update event information.")
elif user_profile["role"] == "viewer":
    print("Role access: You can view event information.")
else:
    print("Role access denied.")
