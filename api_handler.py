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

        # Extract required information from nested JSON fields
        name = country["name"]["common"]
        population = country["population"]
        region = country["region"]
        capital = country["capital"][0]

        # Return extracted data dictionary
        return {
            "name": name,
            "population": population,
            "region": region,
            "capital": capital
        }

    except KeyError:
        # Handle unexpected or missing fields within API response
        print("Unexpected data format received from the API.") 
        return None


