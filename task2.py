
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


valid_events = list(
    filter(
        lambda event: period(event["hour"]) != "Invalid",
        events
    )
)

formatted_events = list(
    map(
        lambda event: event["name"] + " - " + period(event["hour"]),
        valid_events
    )
)

evening_events = list(
    filter(
        lambda item: item.endswith(" - Evening"),
        formatted_events
    )
)

print("Valid events:", valid_events)
print("Formatted events:", formatted_events)
print("Evening events:", evening_events)
