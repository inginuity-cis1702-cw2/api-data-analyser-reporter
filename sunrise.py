#!/usr/bin/env python3
from typing import Any
import urllib.request
import json
# from datetime import date

def isfloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def get_geo_pos(code: str, country: str) -> Any:
    """
    Request latitude and longitude based on given postal code and country:
        >>> get_geo_position("LS1", "GB")
    returns:
        >>> (48.2077, 16.3705) # (latitude, longitude)
    """
    # -- sanity checks --------------------------------------------------------
    assert isinstance(country, str), ValueError("Error: country must be type: str")
    assert isinstance(code, str), ValueError("Error: code must be type: str")

    # -- request --------------------------------------------------------------
    API_KEY = "zip_live_C07XaIk50pN0hTsI8Nnxr8Wm9ZWstQlFScRLwYdN"
    url = f"https://api.zipcodestack.com/v1/search?apikey={API_KEY}&codes={str(code)}&country={country}"
    try:
        with urllib.request.urlopen(url) as f:
            request = f.read() # json byte string
            payload = json.loads(request) # convert to python accessible cict
            print(payload)
            assert isfloat(payload["latitude"]) and isfloat(payload["longitude"]),(
                f"Error: Request failed.\nPayload: {payload}"
            )
            return payload
    except ValueError:
        print("Error: Invalid URL")
        return {}


def get_sun_info(latitude: float, longitude: float, date: str = "") -> Any:
    """
    Request sunrise, sunset and other related times, all in UTC.

    date must follow: YYYY-MM-DD
    If no date supplied, defaults to today.
    """

    # -- sanity checks --------------------------------------------------------
    assert isinstance(latitude, float) and isinstance(longitude, float), (
        "Error: latitude and logitude must be of type: float"
    )

    # -- request --------------------------------------------------------------
    url = f"https://api.sunrise-sunset.org/json?lat={latitude}&lng={longitude}&date={date}"
    try:
        with urllib.request.urlopen(url) as f:
            request = f.read() # json byte string
            payload = json.loads(request) # convert to python accessible cict
            assert payload["status"] == "OK", KeyError(f"Error: Request failed.\nPayload: {payload}")
            return payload
    except ValueError:
        print("Error: Invalid URL")
        return {}


def main():
    print(get_geo_pos("LS1", "GB"))
    print(get_sun_info(51.5074, -0.1278))

if __name__ == "__main__":
    main()
