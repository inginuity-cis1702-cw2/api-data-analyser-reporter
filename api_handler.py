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

"Example function to parse and extract specific information from the fetched data"

def parse_country_data(data): 
    try:
        country = data[0] 
        name = country['name']['common']
        population = country['population']
        region = country['region']
        capital = country['capital'][0]

        return {
            'name': name,
            'population': population,
            'region': region,
            'capital': capital
        }    
    
    except (IndexError, KeyError) as e:
        print(f"Error parsing country data: {e}")
        return None

