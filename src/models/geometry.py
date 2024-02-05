from pydantic.dataclasses import dataclass
from pydantic.fields import Field

class Geometry:
    type: str = "Point"
    coordinates: list = Field(default_factory=list)