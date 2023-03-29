travel_log = {
    "France": {
        "total_visits": 12,
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "year_visited": 2022,
    },
    "Germany": {
        "total_visits": 12,
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "year_visited": 2021,
    },
}


# print(travel_log["France"])

# nesting dictionay in a list:

travel_list = [
    {
        "country": "France",
        "total_visits": 12,
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "year_visited": 2022,
    },
    {
        "country": "Germany",
        "total_visits": 12,
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "year_visited": 2021,
    },
]

print(travel_list)
