#!/usr/bin/env python3

# -- Ephraim -- imports were acting weird. Moved everything into __init__.py
# Then get imports from a single point src
from src import (
    get_user_input,
    get_sun_info,
    time_until,
    save_user_log_csv,
    save_to_json,
    fetch_country_data,
    parse_country_data,
)

def try_again() -> bool:
    """
    Asks user to retry forever until they enter 'y' or 'n'
    """
    while True:
        try_again = input("Try again? (y/n): ")
        match try_again.lower():
            case 'n':
                return False
            case 'y':
                return True
            case _:
                print("Invalid input. Please enter 'y' or 'n'.")
                continue


def collect_data(user_req: dict) -> dict:
    """
    Use user's requested country and return selected facts
    """

    # -- datasets ---------------------------------------------------
    req = fetch_country_data(user_req['country'])
    parsed_data = parse_country_data(req)
    assert req is not None, "Country data not found"
    assert parsed_data is not None, "Country data not found"

    sun_related = {
        "sunrise": req[0]['latlng'],
        "sunset": req[0]['latlng'],
    }

    # -- collect data -----------------------------------------------
    collection  = {}
    for i in user_req['data_points']:
        if (latlng := sun_related.get(i, False)):
            payload = get_sun_info(latlng[0], latlng[1])
            time_diff = time_until(payload['results'][i])
            data = f"{i}: {payload['results'][i]}. Time time until {i}: {time_diff}"
            print(data)
            collection[i] = data
        else:
            collection[i] = parsed_data[i]
    return collection

def logger() -> tuple:
    """
    Wraps user input functions with logging functionality.
    Each iteration is stored in zero indexed dictionary.
    """
    i = 0
    user_log = {}
    while True:
        user_input = get_user_input()
        requested  = collect_data(user_input)
        user_log[i] = requested
        print(f"\nLogged:{user_log[i]}\n")
        retry = try_again()
        if retry:
            i += 1
            continue

        save = input("Save data? (y/n): ")
        if save.lower() == 'y':
            return (user_input, user_log)
        return (None, None)


def main() -> None:

    inputs, outputs = logger()
    if inputs is None and outputs is None:
        print("No data to save.")
        return

    save_location = int(input("Enter save location (1 for JSON, 2 for CSV): "))
    match save_location:
        case 1:
            save_to_json(inputs, outputs)
        case 2:
            save_user_log_csv(outputs) #-- Dan Foy-- Fixed save issue --
        case _:
            print("Invalid save location.")
    print(f"\nInputs:{inputs}\nOutputs:{outputs}")
    # save_user_log_csv(outputs) #-- Dan Foy-- Fixed save issue --


if __name__ == "__main__":
    main()
