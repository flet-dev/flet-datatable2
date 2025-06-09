from typing import List, Optional

import flet as ft

__all__ = ["DataRow2"]

@ft.control("DataRow2")
class DataRow2(ft.Control):
    """
    Extends [DataRow](https://flet.dev/docs/controls/datatable#datarow).

    Adds row-level `tap` events. There are also `on_secondary_tap` and `on_secondary_tap_down`,
    which are not available in DataCells and can be useful in Desktop settings when right-click
    interactions are needed.
    """

    cells: List[ft.DataCell]
    """
    The data for this row - a list of `DataCell` controls.

    There must be exactly as many cells as there are columns in the table.
    """

    color: ft.ControlStateValue[ft.ColorValue] = None
    """
    The color for the row.

    By default, the color is transparent unless selected. 
    Selected rows has a grey translucent color.
    
    The effective color can depend on the ControlState state, 
    if the row is selected, pressed, hovered, focused, disabled or enabled. 
    The color is painted as an overlay to the row. 
    
    To make sure that the row's InkWell is visible (when pressed, hovered and focused), 
    it is recommended to use a translucent color.
    """

    decoration: Optional[ft.BoxDecoration] = None
    """
    Decoration to be applied to the row. 
    
    Overrides `divider_thickness`.
    """

    specific_row_height: ft.OptionalNumber = None
    """
    Specific row height. 
    
    Falls back to `data_row_height` if not set.
    """

    selected: Optional[bool] = None
    """
    Whether the row is selected.

    If `on_select_changed` is non-null for any row in the table, 
    then a checkbox is shown at the start of each row. 
    If the row is selected (`True`), the checkbox will be checked 
    and the row will be highlighted.
    
    Otherwise, the checkbox, if present, will not be checked.
    """

    on_long_press: ft.OptionalControlEventCallable = None
    """
    Fires when the row is long-pressed.
    
    If a `DataCell` in the row has its `on_tap`, `on_double_tap`, `on_long_press`, 
    `on_tap_cancel` or `on_tap_down` callback defined, that callback behavior 
    overrides the gesture behavior of the row for that particular cell.
    """

    on_select_change: ft.OptionalControlEventCallable = None
    """
    Fires when the user selects or unselects a selectable row.
    
    If a callback is set, then the row is selectable. 
    The current selection state of the row is given by selected.

    If any row is selectable, then the table's heading row will 
    have a checkbox that can be checked to select all selectable 
    rows (and which is checked if all the rows are selected), and 
    each subsequent row will have a checkbox to toggle just that row.
    
    A row whose `on_select_changed` callback is null is ignored for 
    the purposes of determining the state of the "all" checkbox, 
    and its checkbox is disabled.
    
    If a `DataCell` in the row has its `DataCell.on_tap` callback defined, 
    that callback behavior overrides the gesture behavior of the row 
    for that particular cell.
    """

    on_double_tap: ft.OptionalControlEventCallable = None
    """
    Fires when the row is double-tapped.
    
    Ignored if the tapped cell has a `tap` handler.
    """

    on_secondary_tap: ft.OptionalControlEventCallable = None
    """
    Fires when the row is right-clicked (secondary tap).
    
    Ignored if the tapped cell has a `tap` handler.
    """

    on_secondary_tap_down: ft.OptionalControlEventCallable = None
    """
    Fires when the row is right-clicked (secondary tap down).
    
    Ignored if the tapped cell has a `tap` handler.
    """

    on_tap: ft.OptionalControlEventCallable = None
    """
    Fires when the row is tapped.
    
    Ignored if the tapped cell has a `tap` handler.
    """

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
