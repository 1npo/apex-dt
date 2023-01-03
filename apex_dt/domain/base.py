from dataclass import dataclass
from datetime import datetime


@dataclass(frozen=True)
class ValueObject:
    """A base class for all value objects"""
    date_updated: datetime = None


@dataclass
class Entity:
    """A base class for all entities"""
    date_updated: datetime = None

