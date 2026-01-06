from api_handler import fetch_country_data, parse_country_data
from country_input import get_user_input
from processing import get_today, get_utc_time, time_until
from sunrise import get_sun_info

import csv
from datetime import datetime


def try_again():
    while True:
        response = input("Try again? (y/n): ").lower()
        
        #Tries to match the user input to see if the user would want to try again
        match response.lower():
            case 'n':
                return False
            case 'y':
                return True
            case _:
                print("Invalid input. Please enter 'y' or 'n'.")

def save_user_log_csv(user_log: dict, filename="user_log.csv"):
    #Open the CSV file in write mode
    with open(filename, mode="w", newline="", encoding="utf=8") as file:
        writer = csv.writer(file)
        
        #Write the header row in the CSV file
        writer.writerow([
            "log_index",
            "requested_data",
            "value",
            "timestamp"
        ])
        
        #Iterate over all of the logged user requests
        for index, results in user_log.items():
            for key, value in results.items():
                writer.writerow([
                    index,
                    key,
                    value,
                    datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
                ])
                
def collect_data(user_req: dict):
    #Fetch raw country data from the API
    req = fetch_country_data(user_req['country'])
    #Parse the raw data into a readable format
    parsed_data = parse_country_data(req)
    
    #Validate the responses provided
    assert req is not None, "Country data not found"
    assert parsed_data is not None, "Country data not found"
    
    #Mapping the sunrise and sunset to the latitude and longitude reported from
    sun_related = {
        "sunrise": req[0]['latlng'],
        "sunset": req[0]['latlng'],
    }
    
    collection = {}
    
    for item in user_req['data_points']:
        if (latlng := sun_related.get(item, False)):
            payload = get_sun_info(latlng[0], latlng[1])
            time_diff = time_until(payload['results'][item])
            
            #Formatting the output for user readablity
            data = (f"{item}: {payload['results']}. "
                    f"Time until {item}: {time_diff}"
            )
            
            print(data)
            collection[item] = data
        else:
            collection[item] = parsed_data[item]
            
    return collection

def logger():
    i = 0
    user_log = {}
    
    while True:
        user_input = get_user_input()
        requested = collect_data(user_input)
        user_log[i] = requested
        
        print(f"\nLogged:{user_log[i]}\n")
        
        retry = try_again()
        if retry:
            i += 1
            continue
        
        #Asking whether or not to save data
        save = input("Save data? (y/n): ")
        if save.lower() == 'y':
            save_user_log_csv(user_log)
            
        return (user_input, user_log)
    
    #Exiting the loop and returning the results
    return (user_input, user_log)


if __name__ == "__main__":
    #Run the application only when executed directly

    logger()

