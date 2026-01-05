def get_user_input():
    # Ask for country
    while True:
        country = input("Enter a country name: ").strip()
        if country != "":
            break
        print("Country cannot be empty.")

    # Ask for data points
    print(
        "Enter data points (press Enter on empty input to finish):\
        \n(Enter 'help' for all data points)\n"
    ) # Notify users with options via 'help'-- Ephraim
    data_points = []

    while True:
        data = input("> ").strip()
        if data == "":
            break

        # Added options so users know valid inputs -- Ephraim
        if data.lower() == "help":
            print("\noptions:\n"
                "name","population","region","capital",
                "area(km^2)","sunrise","sunset", "timezone","\n"
            )

        # Added split in case users list items on one line -- Ephraim
        # Changed append to += as split returns list -- Ephraim
        data_points += data.split(" ")

    return {
        "country": country,
        "data_points": data_points
    }
