from typing import TYPE_CHECKING

from BaseClasses import Region

from .Locations import location_table
from .Types import HungryPumkinLocation

if TYPE_CHECKING:
    from . import HungryPumkinWorld


def create_regions(world: "HungryPumkinWorld") -> None:
    menu = Region("Menu", world.player, world.multiworld)
    region = Region("Dining Room", world.player, world.multiworld)

    for name, data in location_table.items():
        region.locations.append(HungryPumkinLocation(world.player, name, data.ap_code, region))

    menu.connect(region)
    world.multiworld.regions.extend([menu, region])
