from typing import Dict

from .Types import LocData


LOCATION_ROWS = [
    ("Hungry Pumkin Is Very Hungry", 20052041),
    ("Hamburger Correct", 20052001),
    ("Pizza Correct", 20052002),
    ("Sandwich Correct", 20052003),
    ("Hot Dog Correct", 20052004),
    ("Fries Correct", 20052005),
    ("Eggs Correct", 20052006),
    ("Chicken Correct", 20052007),
    ("Cheese Correct", 20052008),
    ("Bread Correct", 20052009),
    ("Rice Correct", 20052010),
    ("Noodles Correct", 20052011),
    ("Salt Correct", 20052012),
    ("Pepper Correct", 20052013),
    ("Butter Correct", 20052014),
    ("Fish Correct", 20052015),
    ("Jam Correct", 20052016),
    ("Orange Juice Correct", 20052017),
    ("Ice Water Correct", 20052018),
    ("Soda Correct", 20052019),
    ("Coffee Correct", 20052020),
    ("Hamburger Incorrect", 20052021),
    ("Pizza Incorrect", 20052022),
    ("Sandwich Incorrect", 20052023),
    ("Hot Dog Incorrect", 20052024),
    ("Fries Incorrect", 20052025),
    ("Eggs Incorrect", 20052026),
    ("Chicken Incorrect", 20052027),
    ("Cheese Incorrect", 20052028),
    ("Bread Incorrect", 20052029),
    ("Rice Incorrect", 20052030),
    ("Noodles Incorrect", 20052031),
    ("Salt Incorrect", 20052032),
    ("Pepper Incorrect", 20052033),
    ("Butter Incorrect", 20052034),
    ("Fish Incorrect", 20052035),
    ("Jam Incorrect", 20052036),
    ("Orange Juice Incorrect", 20052037),
    ("Ice Water Incorrect", 20052038),
    ("Soda Incorrect", 20052039),
    ("Coffee Incorrect", 20052040),
]


location_table = {
    name: LocData(code, "Dining Room")
    for name, code in LOCATION_ROWS
}


def get_location_names() -> Dict[str, int]:
    return {name: data.ap_code for name, data in location_table.items()}


def get_total_locations(_: object) -> int:
    return len(location_table)
