from dataclasses import field
from typing import List, Optional

import flet as ft

from .datacolumn2 import DataColumn2
from .datarow2 import DataRow2

__all__ = ["DataTable2"]

@ft.control("DataTable2")
class DataTable2(ft.ConstrainedControl):
    """
    Extends [DataTable](https://flet.dev/docs/controls/datatable).

    Provides sticky header row, scrollable data rows,
    and additional layout flexibility with [`DataColumn2`][(p).datacolumn2.]
    and [`DataRow2`][(p).datarow2.].
    """

    columns: List[DataColumn2]
    """
    A list of [`DataColumn2`][(p).datacolumn2.] controls describing table columns.
    """

    rows: Optional[List[DataRow2]] = None
    """
    A list of [`DataRow2`][(p).datarow2.] controls defining table rows.
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

    min_width: ft.OptionalNumber = None
    """
    Minimum table width before horizontal scrolling kicks in.
    """

    sort_ascending: bool = False
    """
    Whether the column mentioned in [`sort_column_index`][..], 
    if any, is sorted in ascending order.

    If `True`, the order is ascending (meaning the rows with the smallest 
    values for the current sort column are first in the table).
    
    If `False`, the order is descending (meaning the rows with the smallest 
    values for the current sort column are last in the table).
    """

    show_checkbox_column: bool = False
    """
    Whether the control should display checkboxes for selectable rows.
    
    If `True`, a [`Checkbox`](https://flet.dev/docs/controls/checkbox) 
    will be placed at the beginning of each row that is selectable. 
    However, if `DataRow.on_select_changed` is not set for any row, checkboxes will not 
    be placed, even if this value is `True`.
    
    If `False`, all rows will not display a `Checkbox`.
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

    sort_column_index: Optional[int] = None
    """
    The current primary sort key's column.

    If specified, indicates that the indicated column is the column by which the data is sorted. 
    The number must correspond to the index of the relevant column in `columns`.
    
    Setting this will cause the relevant column to have a sort indicator displayed.
    
    When this is `None`, it implies that the table's sort order does not correspond to any of the columns.
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

    show_bottom_border: bool = False
    """
    Whether a border at the bottom of the table is displayed.

    By default, a border is not shown at the bottom to 
    allow for a border around the table defined by decoration.
    """

    is_horizontal_scroll_bar_visible: Optional[bool] = None
    """
    Determines visibility of the horizontal scrollbar.
    """

    is_vertical_scroll_bar_visible: Optional[bool] = None
    """
    Determines visibility of the vertical scrollbar.
    """

    border: Optional[ft.Border] = None
    """
    The border around the table.
    """

    border_radius: Optional[ft.BorderRadiusValue] = None
    """
    The border radius of the table.
    """

    horizontal_lines: Optional[ft.BorderSide] = None
    """
    Set the [color](https://flet.dev/docs/reference/colors) and width of horizontal lines between rows.
    """

    vertical_lines: Optional[ft.BorderSide] = None
    """
    Set the [color](https://flet.dev/docs/reference/colors) and width of vertical lines between columns.
    """

    checkbox_horizontal_margin: ft.OptionalNumber = None
    """
    Horizontal margin around the checkbox, if it is displayed.
    """

    checkbox_alignment: ft.Alignment = field(
        default_factory=lambda: ft.Alignment.center()
    )
    """
    Alignment of the checkbox.
    """

    column_spacing: ft.OptionalNumber = None
    """
    The horizontal margin between the contents of each data column.
    """

    data_row_color: ft.ControlStateValue[ft.ColorValue] = None
    """
    The background [color](https://flet.dev/docs/reference/colors) for the data rows.

    The effective background color can be made to depend on the 
    [`ControlState`](https://flet.dev/docs/reference/types/controlstate) state,
    i.e. if the row is selected, pressed, hovered, focused, disabled or enabled. 
    The color is painted as an overlay to the row. 
    
    To make sure that the row's InkWell is visible (when pressed, hovered and focused), 
    it is recommended to use a translucent background color.
    """

    data_row_height: ft.OptionalNumber = None
    """
    Height of each data row. Unlike `DataTable`, min/max height is not supported.
    """

    data_text_style: Optional[ft.TextStyle] = None
    """
    The text style for data rows.
    """

    bgcolor: Optional[ft.ColorValue] = None
    """
    The background [color](https://flet.dev/docs/reference/colors) for the table.
    """

    gradient: Optional[ft.Gradient] = None
    """
    The background gradient for the table.
    """

    divider_thickness: ft.OptionalNumber = None
    """
    The width of the divider that appears between rows. 
    
    Note:
        Must be greater than or equal to zero.
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

    heading_row_height: ft.OptionalNumber = None
    """
    The height of the heading row.
    """

    heading_text_style: Optional[ft.TextStyle] = None
    """
    The text style for the heading row.
    """

    heading_row_decoration: Optional[ft.BoxDecoration] = None
    """
    Decoration for the heading row. Overrides color if applied.
    """

    horizontal_margin: ft.OptionalNumber = None
    """
    The horizontal margin between the edges of the table and the content 
    in the first and last cells of each row.

    When a checkbox is displayed, it is also the margin between the 
    checkbox the content in the first data column.
    """

    clip_behavior: ft.ClipBehavior = ft.ClipBehavior.NONE
    """
    The content will be clipped (or not) according to this option. 
    """

    on_select_all: ft.OptionalControlEventCallable = None
    """
    Invoked when the user selects or unselects every row, 
    using the checkbox in the heading row.

    If this is `None`, then the [`DataRow.on_select_change`]() 
    callback of every row in the table is invoked appropriately instead.
    
    To control whether a particular row is selectable or not, 
    see [`DataRow2.on_select_change`][datarow2.md]. 
    This callback is only relevant if any row is selectable.
    """

    def __contains__(self, item):
        return item in self.columns or item in self.rows

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
        # assert (
        #     self.data_row_min_height is None
        #     or self.data_row_max_height is None
        #     or (self.data_row_min_height <= self.data_row_max_height)
        # ), "data_row_min_height must be less than or equal to data_row_max_height"
        assert (
            self.divider_thickness is None or self.divider_thickness >= 0
        ), "divider_thickness must be greater than or equal to 0"
        assert self.sort_column_index is None or (
            0 <= self.sort_column_index < len(visible_columns)
        ), f"sort_column_index must be greater than or equal to 0 and less than the number of columns ({len(visible_columns)})"
