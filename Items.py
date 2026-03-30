from typing import TYPE_CHECKING, List

from BaseClasses import Item, ItemClassification

from .Locations import get_total_locations
from .Types import HungryPumkinItem, ItemData

if TYPE_CHECKING:
    from . import HungryPumkinWorld


FOOD_ITEM_ROWS = [
    ("Hamburger", 20051001),
    ("Pizza", 20051002),
    ("Sandwich", 20051003),
    ("Hot Dog", 20051004),
    ("Fries", 20051005),
    ("Eggs", 20051006),
    ("Chicken", 20051007),
    ("Cheese", 20051008),
    ("Bread", 20051009),
    ("Rice", 20051010),
    ("Noodles", 20051011),
    ("Salt", 20051012),
    ("Pepper", 20051013),
    ("Butter", 20051014),
    ("Fish", 20051015),
    ("Jam", 20051016),
    ("Orange Juice", 20051017),
    ("Ice Water", 20051018),
    ("Soda", 20051019),
    ("Coffee", 20051020),
]

SPECIAL_ITEM_ROWS = [
    ("Progressive Butter", 20051021, ItemClassification.filler),
    ("Car Hit Trap", 20051022, ItemClassification.trap),
    ("Explode Trap", 20051023, ItemClassification.trap),
    ("Butter Only Trap", 20051024, ItemClassification.trap),
    ("Speed Upgrade", 20051025, ItemClassification.useful),
]
SPECIAL_ITEM_NAMES = [name for name, _, _ in SPECIAL_ITEM_ROWS]

item_table = {
    name: ItemData(code, ItemClassification.progression, 1)
    for name, code in FOOD_ITEM_ROWS
}
item_table.update({
    name: ItemData(code, classification, 1)
    for name, code, classification in SPECIAL_ITEM_ROWS
})


def create_item(world: "HungryPumkinWorld", name: str) -> Item:
    data = item_table[name]
    return HungryPumkinItem(name, data.classification, data.ap_code, world.player)


def create_itempool(world: "HungryPumkinWorld") -> List[Item]:
    itempool: List[Item] = [
        create_item(world, name)
        for name, _ in FOOD_ITEM_ROWS
    ]

    remaining_slots = get_total_locations(world) - len(itempool)
    for _ in range(max(0, remaining_slots)):
        itempool.append(create_item(world, world.random.choice(SPECIAL_ITEM_NAMES)))

    return itempool
