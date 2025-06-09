from dataclasses import dataclass
from enum import Enum
from typing import Optional

import flet as ft

__all__ = ["DataColumn2"]


@ft.control("DataColumn2")
class DataColumn2(ft.Control):
    """
    Column configuration for a [DataTable2](datatable2.md).

    One column configuration must be provided for each column to display in the table.

    Additional to Flet [DataColumn](https://flet.dev/docs/controls/datatable/#datacolumn), adds the capability to set relative column size via size property.
    """

    label: ft.Control
    """
    The column heading.

    Typically, this will be a `Text` control. It could also be an 
    `Icon` (typically using size 18), or a `Row` with an icon and some text.
    """

    fixed_width: ft.OptionalNumber = None
    """
    Defines absolute width of the column in pixels (as opposed to relative `size` used by default).
    """

    heading_row_alignment: Optional[ft.MainAxisAlignment] = None
    """
    Defines the horizontal layout of the label and sort indicator in the heading row.
    """

    numeric: bool = False
    """
    Whether this column represents numeric data or not.

    The contents of cells of columns containing numeric data are right-aligned.
    """

    size: Optional[Size] = None
    """
    Column sizes are determined based on available width by distributing it to individual columns accounting for their relative sizes. Value is of type `Size` and defaults to `Size.S`.
    """

    on_sort: ft.OptionalEventCallable[ft.DataColumnSortEvent] = None
    """
    Fires when the user asks to sort the table using this column.

    If not set, the column will not be considered sortable.
    """

    def before_update(self):
        super().before_update()
        assert self.label.visible, "label must be visible"
