from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Api:
    """reprents the key meta data for a API"""

    name: str
    url: str
    date: datetime = None
    meta: field(default_factory=dict) = None
