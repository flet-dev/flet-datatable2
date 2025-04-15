from typing import List, Optional

import flet as ft


@ft.control("DataRow2")
class DataRow2(ft.Control):
    """
    Extension of [DataRow](https://flet.dev/docs/controls/datatable#datarow).

    Adds row level `tap` events. There are also `onSecondaryTap` and `onSecondaryTapDown` which are not available in DataCells and which can be useful in Desktop settings when a reaction to the right click is required.

    Attributes:
        cells: See DataRow [cells](https://flet.dev/docs/controls/datatable#cells).
        color: See DataRow [color](https://flet.dev/docs/controls/datatable#color).
        decoration: **NEW!** Decoration to be applied to the given row. When applied, `divider_thickness` won't take effect.
        on_double_tap: **NEW!** Row double tap handler. Won't be called if tapped cell has `tap` event handler.
        on_long_press: See DataRow [on_long_press](https://flet.dev/docs/controls/datatable#on_long_press).
        on_secondary_tap: **NEW!** Row right click handler. Won't be called if tapped cell has `tap` event.
        on_secondary_tap_down: **NEW!** Row right mouse down handler. Won't be called if tapped cell has `tap` event handler.
        on_select_changed: See DataRow [on_select_changed](https://flet.dev/docs/controls/datatable#on_select_changed).
        on_tap: **NEW!** Row tap handler. Won't be called if tapped cell has `tap` event handler.
        selected: See DataRow [selected](https://flet.dev/docs/controls/datatable#selected).
        specific_row_height: **NEW!** Specific row height. If not provided, `data_row_height` will be applied.

    """

    cells: List[ft.DataCell]
    color: ft.ControlStateValue[ft.ColorValue] = None
    decoration: Optional[ft.BoxDecoration] = None
    specific_row_height: ft.OptionalNumber = None
    selected: Optional[bool] = None
    on_long_press: ft.OptionalControlEventCallable = None
    on_select_changed: ft.OptionalControlEventCallable = None
    on_double_tap: ft.OptionalControlEventCallable = None
    on_secondary_tap: ft.OptionalControlEventCallable = None
    on_secondary_tap_down: ft.OptionalControlEventCallable = None
    on_tap: ft.OptionalControlEventCallable = None

    def __contains__(self, item):
        return item in self.cells

    def before_update(self):
        super().before_update()
        assert any(
            cell.visible for cell in self.cells
        ), "cells must contain at minimum one visible DataCell"
        # assert all(
        #     isinstance(cell, DataCell) for cell in self.cells
        # ), "cells must contain only DataCell instances"
