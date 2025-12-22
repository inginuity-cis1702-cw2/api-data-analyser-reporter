# Import urllib to handle HTTP requests using the Python standard library
import urllib.request

# Import json to parse JSON data returned by the API
import json


def fetch_country_data(country_name):
    """
    Fetches raw country data from the REST Countries API based on the user's input.
    """
    try:
        # Construct API URL using provided country name
        url = f"https://restcountries.com/v3.1/name/{country_name}"

        # Open connection to API and read response data
        with urllib.request.urlopen(url) as response:
            data = response.read()

            # Convert JSON response into Python data structure
            return json.loads(data)

    except Exception as e:
        # Handle network errors, invalid URLs, or API failures
        print(f"An error occurred while fetching data: {e}")
        return None


def parse_country_data(data):
    """
    Extracts relevant fields from the raw API data and structures them for use
    elsewhere in the application.
    """
    try:
        # Access first country result from API response
        country = data[0]
        # Extract and return required information from nested JSON fields in dictionary
        return {
            "name": country["name"]["common"],
            "population": country["population"],
            "region": country["region"],
            "capital": country["capital"][0],
            "area": country["area"]
        }
    except (KeyError, IndexError, TypeError):
        # Handle unexpected or missing fields within API response (now including Index & Type)
        print("Error parsing country data.")
        return None

# Handle Invalid User Input, Specifically required by brief
if __name__ == "__main__":
    country_name = input("Enter a country name: ")
    data = fetch_country_data(country_name)
    if data is None:
        print("No data found. Please try again.")
    else:
        parsed_data = parse_country_data(data)
        if parsed_data is None:
            print("Failed to parse country data.")
        else:
            print(parsed_data)





