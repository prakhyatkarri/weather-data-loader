from pydantic.dataclasses import dataclass
from pydantic.fields import Field
from ..models.feature import Feature
from typing import List



@dataclass
class Station():
    """
    Station
    """
    type: str = "FeatureCollection"
    features: List[Feature] = Field(default_factory=list)
    observationStations: list = Field(default_factory=list) 
    pagination: dict = Field(default_factory=dict) 
