from .api_handler import fetch_country_data, parse_country_data
from .country_input import get_user_input
from .processing import get_today, get_utc_time, time_until
from .sunrise import get_sun_info


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
            ... # TODO: implement csv

        return (user_input, user_log)


def main() -> None:

    inputs, outputs = logger()
    print(f"\nInputs:{inputs}\nOutputs:{outputs}")




if __name__ == "__main__":
    main()
