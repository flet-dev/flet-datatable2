from dataclasses import dataclass
from enum import Enum

import flet as ft

__all__ = ["DataColumnSize", "DataColumnSortEvent"]

class DataColumnSize(Enum):
    """
    Relative size of a column determines the share of total table
    width allocated to each individual column.

    When determining column widths, ratios between `S`, `M` and `L`
    columns are kept (i.e. Large columns are set to 1.2x width of Medium ones).
    See `DataTable2.smRatio`, `DataTable2.lmRatio`.
    Default S/M ratio is 0.67, L/M ratio is 1.2.
    """

    S = "s"
    M = "m"
    L = "l"


@dataclass
class DataColumnSortEvent(ft.ControlEvent):
    column_index: int
    ascending: bool