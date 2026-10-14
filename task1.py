
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

result = {
    "Morning": [],
    "Afternoon": [],
    "Evening": [],
    "Night": []
}

for event in events:
    hour = event["hour"]

    if hour < 0 or hour > 23:
        continue

    if 6 <= hour <= 11:
        category = "Morning"
    elif 12 <= hour <= 17:
        category = "Afternoon"
    elif 18 <= hour <= 22:
        category = "Evening"
    else:
        category = "Night"

    result[category].append(event["name"])

print(result)