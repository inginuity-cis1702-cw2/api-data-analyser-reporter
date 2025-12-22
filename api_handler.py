import urllib.request
import json

def fetch_country_data(country_name):
    try:
        url = f"https://restcountries.com/v3.1/name/{country_name}"
        with urllib.request.urlopen(url) as response:
            data = response.read()
            return json.loads(data)
    except Exception as e:
        print(f"An error occurred: {e}")
        return None



