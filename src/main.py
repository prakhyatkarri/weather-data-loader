from fastapi import FastAPI
from .models.station import Station  
from .service.stations_service import Station_Service

app = FastAPI()

@app.get("/")
def get_homepage():
    return {"status": "OK"}


@app.get("/stations_test")
def get_stations_test():
    stations_value =     {
  "type": "FeatureCollection",
  "features": [
    {
      "id": "string",
      "type": "Feature",
      "properties": {
        "geometry": "string",
        "@id": "string",
        "@type": "wx:ObservationStation",
        "elevation": {
          "value": 0,
          "maxValue": 0,
          "minValue": 0,
          "unitCode": "string",
          "qualityControl": "Z"
        },
        "stationIdentifier": "string",
        "name": "string",
        "timeZone": "string",
        "forecast": "string",
        "county": "string",
        "fireWeatherZone": "string"
      }
    }
  ],
  "observationStations": [
    "string"
  ],
  "pagination": {
    "next": "string"
  }
}
    return Station(**stations_value)

@app.get("/stations")
def get_stations():
    return Station_Service(endpoint="stations").get_stations()