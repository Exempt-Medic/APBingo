from dataclasses import dataclass
from Options import Toggle, Option, Range, Choice, ItemSet, OptionSet, PerGameCommonOptions, StartHints
from .Items import item_data_table

class RequiredBingos(Range):
    """The number of Bingo's required to goal, min is 1, max is 22
    max per board size: 3x3 = 8, 4x4 = 10, 5x5 = 12, 6x6 = 14, 7x7 = 16, 8x8 = 18, 9x9 = 20, 10x10 = 22 """
    range_start = 1
    range_end = 22
    default = 1
    display_name = "Required Bingos"


class BoardSize(Range):
    """The size of the bingo board (3 = 3x3, 10 = 10x10)"""
    range_start = 3
    range_end = 10
    default = 5
    display_name = "Board Size"

class AutoHints(Toggle):
    """If true, automatically hint all board squares"""
    display_name = "Auto Hints"

class BingoStartHints(StartHints):
    """Start with these item's locations prefilled into the ``!hint`` command."""
    default = []

@dataclass
class BingoOptions(PerGameCommonOptions):
    required_bingos: RequiredBingos
    board_size: BoardSize
    auto_hints: AutoHints
    start_hints: BingoStartHints
