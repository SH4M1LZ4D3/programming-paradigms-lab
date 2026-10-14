# Task 3 - Higher-order Function and Callback
events = [
    {"name": "Meeting", "hour": 9},
    {"name": "Study", "hour": 14},
    {"name": "Gym", "hour": 19},
    {"name": "Reading", "hour": 23},
    {"name": "Breakfast", "hour": 7},
    {"name": "Movie", "hour": 21},
    {"name": "Homework", "hour": 16},
    {"name": "Mystery", "hour": 25},
]


def period(hour):
    if hour < 0 or hour > 23:
        return "Invalid"

    if 6 <= hour <= 11:
        return "Morning"
    elif 12 <= hour <= 17:
        return "Afternoon"
    elif 18 <= hour <= 22:
        return "Evening"
    else:
        return "Night"


def group_by(items, key_func):
    groups = {}

    for item in items:
        key = key_func(item)

        if key not in groups:
            groups[key] = []

        groups[key].append(item)

    return groups


def first_letter(event):
    return event["name"][0].upper()


by_period = group_by(
    events,
    lambda event: period(event["hour"])
)

by_letter = group_by(events, first_letter)

print("Grouped by period:", by_period)
print("Grouped by first letter:", by_letter)
