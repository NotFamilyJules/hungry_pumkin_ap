from typing import NamedTuple, Optional

from BaseClasses import Item, ItemClassification, Location


class HungryPumkinLocation(Location):
    game = "Hungry Pumkin"


class HungryPumkinItem(Item):
    game = "Hungry Pumkin"


class ItemData(NamedTuple):
    ap_code: Optional[int]
    classification: ItemClassification
    count: int = 1


class LocData(NamedTuple):
    ap_code: Optional[int]
    region: str
