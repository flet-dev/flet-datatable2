from dataclasses import field
from typing import List, Optional, Union

import flet as ft

from .datacolumn2 import DataColumn2
from .datarow2 import DataRow2

__all__ = ["DataTable2"]

@ft.control("DataTable2")
class DataTable2(ft.DataTable):
    """
    Extends [DataTable](https://flet.dev/docs/controls/datatable).

    Provides sticky header row, scrollable data rows,
    and additional layout flexibility with [`DataColumn2`][(p).datacolumn2.]
    and [`DataRow2`][(p).datarow2.].
    """

    columns: list[Union[DataColumn2, ft.DataColumn]]
    """
    A list of table columns.
    """

    rows: list[Union[ft.DataRow, DataRow2]] = field(default_factory=list)
    """
    A list of table rows.
    """

    empty: Optional[ft.Control] = None
    """
    Placeholder control shown when there are no data rows.
    """

    bottom_margin: ft.OptionalNumber = None
    """
    Adds space after the last row if set.
    """

    lm_ratio: ft.Number = 1.2
    """
    Ratio of Large column width to Medium.
    """

    sm_ratio: ft.Number = 0.67
    """
    Ratio of Small column width to Medium.
    """

    fixed_left_columns: int = 0
    """
    Number of sticky columns on the left. Includes checkbox column, if present.
    """

    fixed_top_rows: int = 1
    """
    Number of sticky rows from the top. Includes heading row by default.
    """

    fixed_columns_color: Optional[ft.ColorValue] = None
    """
    Background color for sticky left columns.
    """

    fixed_corner_color: Optional[ft.ColorValue] = None
    """
    Background color of the fixed top-left corner cell.
    """

    sort_arrow_icon_color: Optional[ft.ColorValue] = None
    """
    When set always overrides/preceeds default arrow icon color.
    """

    min_width: ft.OptionalNumber = None
    """
    Minimum table width before horizontal scrolling kicks in.
    """

    show_heading_checkbox: bool = True
    """
    Controls visibility of the heading checkbox.
    """

    heading_checkbox_theme: Optional[ft.CheckboxTheme] = None
    """
    Overrides theme of the heading checkbox.
    """

    data_row_checkbox_theme: Optional[ft.CheckboxTheme] = None
    """
    Overrides theme of checkboxes in each data row.
    """

    sort_arrow_icon: ft.IconValue = ft.Icons.ARROW_UPWARD
    """
    Icon shown when sorting is applied.
    """

    sort_arrow_animation_duration: ft.DurationValue = field(
        default_factory=lambda: ft.Duration(milliseconds=150)
    )
    """
    Duration of sort arrow animation in milliseconds.
    """

    visible_horizontal_scroll_bar: Optional[bool] = None
    """
    Determines visibility of the horizontal scrollbar.
    """

    visible_vertical_scroll_bar: Optional[bool] = None
    """
    Determines visibility of the vertical scrollbar.
    """

    checkbox_alignment: ft.Alignment = field(
        default_factory=lambda: ft.Alignment.center()
    )
    """
    Alignment of the checkbox.
    """

    data_row_height: ft.OptionalNumber = None
    """
    Height of each data row. 
    
    Note:
        `DataTable2` doesn't support 
        `DataTable.data_row_min_height` and `DataTable.data_row_max_height`.
    """

    heading_row_color: ft.ControlStateValue[ft.ColorValue] = None
    """
    The background [color](https://flet.dev/docs/reference/colors) for the heading row.

    The effective background color can be made to depend on the 
    [`ControlState`](https://flet.dev/docs/reference/types/controlstate) state,
    i.e. if the row is pressed, hovered, focused when sorted. The color is 
    painted as an overlay to the row. 
    
    To make sure that the row's InkWell is visible (when pressed, hovered and focused), 
    it is recommended to use a translucent color.
    """

    def before_update(self):
        super().before_update()
        assert all(
            isinstance(column, DataColumn2) for column in self.columns
        ), "columns must contain only DataColumn2 instances"
        assert all(
            isinstance(row, DataRow2) for row in self.rows
        ), "rows must contain only DataRow2 instances"
        visible_columns = list(filter(lambda column: column.visible, self.columns))
        visible_rows = list(filter(lambda row: row.visible, self.rows))
        assert (
            len(visible_columns) > 0
        ), "columns must contain at minimum one visible DataColumn"

        assert all(
            len(list(filter(lambda c: c.visible, row.cells))) == len(visible_columns)
            for row in visible_rows
        ), f"each visible DataRow must contain exactly as many visible DataCells as there are visible DataColumns ({len(visible_columns)})"
        assert (
            self.divider_thickness is None or self.divider_thickness >= 0
        ), "divider_thickness must be greater than or equal to 0"
        assert self.sort_column_index is None or (
            0 <= self.sort_column_index < len(visible_columns)
        ), f"sort_column_index must be greater than or equal to 0 and less than the number of columns ({len(visible_columns)})"
