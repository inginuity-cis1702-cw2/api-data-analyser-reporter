def get_user_input():
    # Ask for country
    while True:
        country = input("Enter a country name: ").strip()
        if country != "":
            break
        print("Country cannot be empty.")

    # Ask for data points
    print("Enter data points (press Enter on empty input to finish):")
    data_points = []

    while True:
        data = input("> ").strip()
        if data == "":
            break
        data_points.append(data)

    return {
        "country": country,
        "data_points": data_points
    }
