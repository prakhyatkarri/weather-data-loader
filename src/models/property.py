from pydantic.dataclasses import dataclass
from pydantic.fields import Field

@dataclass
class Property:
    id: str
    type: str
    stationIdentifier: str
    name: str
    timeZone: str
    forecast: str
    county: str
    fireWeatherZone: str
    tempkey: str = "TempValue"
    # elevation: dict = Field(default_factory=dict)
    