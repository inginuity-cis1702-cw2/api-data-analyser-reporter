from api_handler import fetch_country_data, parse_country_data

country = input("Enter a country name: ")
raw_data = fetch_country_data(country)

if raw_data:
    parsed = parse_country_data(raw_data)
    if parsed:
        print(parsed)
        else:
            print(f"Warning: '{key}' is not available for this country.")

    # Step 5: Display the filtered data
    print("\nSelected data:")
    print(selected_data)

if __name__ == "__main__":
    main()

