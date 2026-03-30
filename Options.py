from dataclasses import dataclass

from Options import DeathLink
from worlds.AutoWorld import PerGameCommonOptions


@dataclass
class HungryPumkinOptions(PerGameCommonOptions):
    death_link: DeathLink
