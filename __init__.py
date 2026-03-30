from typing import Dict

from BaseClasses import Item, MultiWorld, Tutorial
from worlds.AutoWorld import CollectionState, WebWorld, World

from .Items import create_item, create_itempool, item_table
from .Locations import get_location_names, get_total_locations
from .Options import HungryPumkinOptions
from .Regions import create_regions
from .Rules import set_rules


class HungryPumkinWeb(WebWorld):
    theme = "Party"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Hungry Pumkin for Archipelago.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Codex"],
    )]


class HungryPumkinWorld(World):
    """
    Feed Hungry Pumkin the correct foods. Every correct and incorrect answer is a check.
    """

    game = "Hungry Pumkin"
    item_name_to_id = {name: data.ap_code for name, data in item_table.items()}
    location_name_to_id = get_location_names()
    options_dataclass = HungryPumkinOptions
    options = HungryPumkinOptions
    web = HungryPumkinWeb()

    def __init__(self, multiworld: "MultiWorld", player: int):
        super().__init__(multiworld, player)

    def create_regions(self) -> None:
        create_regions(self)

    def create_items(self) -> None:
        self.multiworld.itempool += create_itempool(self)

    def set_rules(self) -> None:
        set_rules(self)

    def create_item(self, name: str) -> Item:
        return create_item(self, name)

    def fill_slot_data(self) -> Dict[str, object]:
        return {
            "options": {
                "death_link": bool(self.options.death_link.value),
            },
            "Seed": self.multiworld.seed_name,
            "Slot": self.multiworld.player_name[self.player],
            "TotalLocations": get_total_locations(self),
        }

    def collect(self, state: "CollectionState", item: "Item") -> bool:
        return super().collect(state, item)

    def remove(self, state: "CollectionState", item: "Item") -> bool:
        return super().remove(state, item)
