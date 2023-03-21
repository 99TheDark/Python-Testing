def online_count(statuses):
    return len([person for person in statuses if statuses[person] == "online"])

all_statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
    "Jim": "offline"
}

print(online_count(all_statuses))
