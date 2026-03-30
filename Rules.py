from typing import TYPE_CHECKING

from worlds.generic.Rules import add_item_rule, add_rule

from .Items import FOOD_ITEM_ROWS
from .Locations import location_table

if TYPE_CHECKING:
    from . import HungryPumkinWorld


VERY_HUNGRY_LOCATION = "Hungry Pumkin Is Very Hungry"
LOCAL_FOOD_NAMES = {name for name, _ in FOOD_ITEM_ROWS}


def get_required_food_name(location_name: str) -> str | None:
    if location_name.endswith(" Correct"):
        return location_name[:-len(" Correct")]
    if location_name.endswith(" Incorrect"):
        return location_name[:-len(" Incorrect")]
    return None


def set_rules(world: "HungryPumkinWorld") -> None:
    player = world.player
    first_check = world.multiworld.get_location(VERY_HUNGRY_LOCATION, player)
    add_item_rule(
        first_check,
        lambda item, player=player: item.player == player and item.name in LOCAL_FOOD_NAMES,
    )

    for location_name in location_table:
        if location_name == VERY_HUNGRY_LOCATION:
            continue

        required_food_name = get_required_food_name(location_name)
        if required_food_name not in LOCAL_FOOD_NAMES:
            continue

        add_rule(
            world.multiworld.get_location(location_name, player),
            lambda state, player=player, required_food_name=required_food_name: state.has(required_food_name, player),
        )

    world.multiworld.completion_condition[player] = lambda state: all(
        state.has(item_name, player) for item_name, _ in FOOD_ITEM_ROWS
    )
