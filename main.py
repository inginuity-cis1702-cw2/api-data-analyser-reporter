from api_handler import fetch_country_data, parse_country_data

country = input("Enter a country name: ")
raw_data = fetch_country_data(country)

if raw_data:
    parsed = parse_country_data(raw_data)
    if parsed:
        print(parsed)