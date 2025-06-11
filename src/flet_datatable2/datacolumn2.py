from typing import Optional

import flet as ft
from .types import DataColumnSize

__all__ = ["DataColumn2"]


@ft.control("DataColumn2")
class DataColumn2(ft.DataColumn):
    """
    Extends Flet [`DataColumn`](https://flet.dev/docs/controls/datatable/#datacolumn),
    adding the ability to set relative column size and fixed column width.

    Meant to be used as an item of [`DataTable2.columns`][(p).datatable2.].
    """

    fixed_width: ft.OptionalNumber = None
    """
    Defines absolute width of the column in pixels (as opposed to relative [`size`][..] used by default).
    """

    size: Optional[DataColumnSize] = DataColumnSize.S
    """
    Column sizes are determined based on available width by distributing 
    it to individual columns accounting for their relative sizes. 
    """
