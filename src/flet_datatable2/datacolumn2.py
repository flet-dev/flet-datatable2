import json
from enum import Enum
from typing import Any, Optional

import flet as ft


class Size(Enum):
    """Relative size of a column determines the share of total table width allocated to each individual column.

    When determining column widths, ratios between `S`, `M` and `L` columns are kept (i.e. Large columns are set to 1.2x width of Medium ones).
    See `DataTable2.smRatio`, `DataTable2.lmRatio`. Default S/M ratio is 0.67, L/M ratio is 1.2.
    """

    S = "s"
    M = "m"
    L = "l"


class DataColumnSortEvent(ft.ControlEvent):
    def __init__(self, e: ft.ControlEvent):
        super().__init__(e.target, e.name, e.data, e.control, e.page)
        d = json.loads(e.data)
        self.column_index: int = d.get("i")
        self.ascending: bool = d.get("a")


@ft.control("DataColumn2")
class DataColumn2(ft.Control):
    """Column configuration for a [DataTable2](datatable2.md).

    One column configuration must be provided for each column to display in the table.

    Additional to Flet [DataColumn](https://flet.dev/docs/controls/datatable/#datacolumn), adds the capability to set relative column size via size property.

    Attributes:
        label: See DataColumn [label](https://flet.dev/docs/controls/datatable#label).
        fixed_width: **NEW!** Defines absolute width of the column in pixels (as opposed to relative `size` used by default).
        heading_row_alignment: See DataColumn [heading_row_alignment](https://flet.dev/docs/controls/datatable#heading_row_alignment).
        numeric: See DataColumn [numeric](https://flet.dev/docs/controls/datatable#numeric).
        on_sort:  See DataColumn [on_sort](https://flet.dev/docs/controls/datatable#on_sort).
        size: **NEW!** Column sizes are determined based on available width by distributing it to individual columns accounting for their relative sizes. Value is of type `Size` and defaults to `Size.S`.
    """

    label: ft.Control
    fixed_width: ft.OptionalNumber = None
    heading_row_alignment: Optional[ft.MainAxisAlignment] = None
    numeric: bool = False
    size: Optional[Size] = None

    on_sort: ft.OptionalEventCallable[ft.DataColumnSortEvent] = None

    def before_update(self):
        super().before_update()
        assert self.label.visible, "label must be visible"
