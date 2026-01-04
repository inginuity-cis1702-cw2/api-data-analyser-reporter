from api_handler import fetch_country_data, parse_country_data
from country_input import get_user_input

def main():
    # Step 1: Get country and data points from CLI
    user_input = get_user_input()
    country = user_input["country"]
    data_points = user_input["data_points"]

    # Step 2: Fetch raw data from the API
    raw_data = fetch_country_data(country)
    if not raw_data:
        print("No data found for this country.")
        return

    # Step 3: Parse the data
    parsed = parse_country_data(raw_data)
    if not parsed:
        print("Failed to parse country data.")
        return

    # Step 4: Filter parsed data to only include user-selected points
    selected_data = {}
    for key in data_points:
        if key in parsed:
            selected_data[key] = parsed[key]
        else:
            print(f"Warning: '{key}' is not available for this country.")

    # Step 5: Display the filtered data
    print("\nSelected data:")
    print(selected_data)

if __name__ == "__main__":
    main()
