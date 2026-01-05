from .api_handler import fetch_country_data, parse_country_data
from .country_input import get_user_input
from .processing import get_today, get_utc_time, time_until_target
from .sunrise import get_sun_info


# -- possibly redunant ----------------------------------------------
# country = input("Enter a country name: ")
# raw_data = fetch_country_data(country)
#
# if raw_data:
#     parsed = parse_country_data(raw_data)
#     if parsed:
#         print(parsed)
#     else:
#         print(f"Warning: '{key}' is not available for this country.")
#
#     # Step 5: Display the filtered data
#     print("\nSelected data:")
#     print(selected_data)
#
# if __name__ == "__main__":
#     main()
#
# -------------------------------------------------------------------

# raw_data = fetch_country_data(country)
#

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

def logger() -> dict:
    """
    Wraps user input function with logging functionality.
    Each iteration is stored in zero indexed dictionary.
    """
    i = 0
    user_log = {}
    while True:
        user_input = get_user_input()
        user_log[i] = user_input
        retry = try_again()
        if retry:
            i += 1
            continue
        return user_log



def main() -> None:
    # log = logger()
    # print(log)
    print(fetch_country_data("japan")) ## caa2
    ## timezone 'timezones': ['UTC+09:00'],
    # 'latlng': [35.68, 139.75]
    
    
    

if __name__ == "__main__":
    main()
