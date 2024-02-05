from pydantic.dataclasses import dataclass
from pydantic.fields import Field
from ..models.geometry import Geometry
from ..models.property import Property

@dataclass
class Feature:
    id: str
    type: str = "Feature"
    geometry: dict = Field(default_factory=Geometry)
    properties: dict = Field(default_factory=Property)