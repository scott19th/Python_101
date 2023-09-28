# Python Coding Challenge - Cities World Tour

cities = [
    {"city": "Paris", "country": "France"},
    {"city": "Berlin", "country": "Germany"},
    {"city": "Geneva", "country": "Switzerland"},
    {"city": "Nice", "country": "France"},
    {"city": "Rome", "country": "Italy"},
    {"city": "Dubai", "country": "UAE"},
    {"city": "Bangkok", "country": "Thailand"},
    {"city": "Phuket", "country": "Thailand"},
    {"city": "Tokyo", "country": "Japan"},
    {"city": "Osaka", "country": "Japan"},
]


def country_counter(tourdata):
    countries = set()
    for country in tourdata:
        countries.add(country["country"])
    print(countries)


def city_counter(tourdata):
    country_counts = {}

    for entry in cities:
        country = entry["country"]
        if country in country_counts:
            country_counts[country] += 1
        else:
            country_counts[country] = 1

# using .items() displays the dictionary as a list of key value tuple pairs
    for country, count in country_counts.items():
        print(f"I've visited {count} city(ies) in {country}.")
    print(country_counts)


country_counter(cities)
city_counter(cities)
