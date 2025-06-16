from typing import Optional

import flet as ft

__all__ = ["DataRow2"]

@ft.control("DataRow2")
class DataRow2(ft.DataRow):
    """
    Extends [`DataRow`](https://flet.dev/docs/controls/datatable#datarow).

    Adds row-level `tap` events. There are also [`on_secondary_tap`][(c).] and [`on_secondary_tap_down`][(c).],
    which are not available in `DataCell`s and can be useful in desktop settings to handle right-click actions.
    """

    decoration: Optional[ft.BoxDecoration] = None
    """
    Decoration to be applied to the row. 
    
    Overrides `divider_thickness`.
    """

    specific_row_height: Optional[ft.Number] = None
    """
    Specific row height. 
    
    Falls back to `data_row_height` if not set.
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

    on_tap: ft.OptionalEventCallable[ft.TapEvent] = None
    """
    Fires when the row is tapped.
    
    Ignored if the tapped cell has a `tap` handler.
    """

