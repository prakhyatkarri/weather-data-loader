import requests
from ..models.station import Station
import json

class Station_Service():
    endpoint:str
    base_url: str | None = "http://api.weather.gov/"

    def __init__(self, endpoint) -> None:
        self.endpoint = endpoint

    def get_stations(self):
        response = requests.get(url = self.base_url + self.endpoint, timeout=60).json()
        return Station(**response)
        