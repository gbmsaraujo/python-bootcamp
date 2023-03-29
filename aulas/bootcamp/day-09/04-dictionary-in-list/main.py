def add_new_country(country_visited, total_visits, cities_visited):
    new_country  = {
        "country": country_visited,
        "total_visits": total_visits,
        "cities_visited": cities_visited
    }
    travel_list.append(new_country)


travel_list = [
    {
        "country": "France",
        "total_visits": 12,
        "cities_visited": ["Paris", "Lille", "Dijon"],
    },
    {
        "country": "Germany",
        "total_visits": 12,
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    },
]


add_new_country("Russia", 2,  ["Moscow", "Saint Petersburg"])

print(travel_list)
