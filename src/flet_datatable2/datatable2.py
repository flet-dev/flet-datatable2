from dataclasses import field
from typing import List, Optional

import flet as ft

from flet_datatable2.datacolumn2 import DataColumn2
from flet_datatable2.datarow2 import DataRow2


@ft.control("DataTable2")
class DataTable2(ft.ConstrainedControl):
    """
    In-place replacement of standard Flet [DataTable](https://flet.dev/docs/controls/datatable).

    Has the header row always fixed and core of the table (with data rows) scrollable and stretching to max width/height of it's container.
    By using [DataColumn2](datacolumn2.md) instead of [DataColumn](https://flet.dev/docs/controls/datatable#datacolumn) it is possible to control relative column sizes (setting them to S, M and L).
    [DataRow2](datarow2.md) provides row-level tap event handlers.

    Attributes:
        bgcolor: See DataTable [bgcolor](https://flet.dev/docs/controls/datatable#bgcolor).
        border: See DataTable [border](https://flet.dev/docs/controls/datatable#border).
        border_radius: See DataTable [border_radius](https://flet.dev/docs/controls/datatable#border_radius).
        bottom_margin: **NEW!** If set, the table will have empty space added after the the last row.
        checkbox_alignment: **NEW!** Alignment of the checkbox if it is displayed. Defaults to `alignment.center`.
        checkbox_horizontal_margin: See DataTable [checkbox_horizontal_margin](https://flet.dev/docs/controls/datatable#checkbox_horizontal_margin).
        clip_behavior: See DataTable [clip_behavior](https://flet.dev/docs/controls/datatable#clip_behavior).
        column_spacing: See DataTable [column_spacing](https://flet.dev/docs/controls/datatable#column_spacing).
        columns: A list of [DataColumn2](datacolumn2.md) controls describing table columns.
        data_row_checkbox_theme: **NEW!**  Overrides theme of the checkboxes that are displayed in the checkbox column in each data row (if checkboxes are enabled).
        data_row_color: See DataTable [data_row_color](https://flet.dev/docs/controls/datatable#data_row_color).
        data_row_height: **NEW!** The height of each row (excluding the row that contains column headings). Note that, unlike in Flet [DataTable](https://flet.dev/docs/controls/datatable), there's no capability to define min/max height of a row. This is an implementation tradeoff making it possible to have performant sticky columns.
        data_text_style: See DataTable [data_text_style](https://flet.dev/docs/controls/datatable#data_text_style).
        divider_thickness: See DataTable [divider_thickness](https://flet.dev/docs/controls/datatable#divider_thickness).
        empty: **NEW!** Placeholder control which is displayed whenever the data rows are empty. The widget will be displayed below heading row.
        fixed_columns_color: **NEW!** Backgound color of the sticky columns fixed via `fixed_left_columns`.
        fixed_corner_color: **NEW!** Backgound color of the top left corner which is fixed when both `fixed_top_rows` and `fixed_left_columns` are greater than 0.
        fixed_left_columns: **NEW!** The number of sticky columns fixed at the left side of the table. Check box column (if enabled) is also counted. Defaults to 0.
        fixed_top_rows: **NEW!** The number of sticky rows fixed at the top of the table. The heading row is counted/included. By defult the value is 1 which means header row is fixed. Set to 0 in order to unstick the header, set to >1 in order to fix data rows (i.e. in order to fix both header and the first data row use value of 2).
        gradient: See DataTable [gradient](https://flet.dev/docs/controls/datatable#gradient).
        heading_checkbox_theme: **NEW!** Overrides theme of the checkbox that is displayed in the top left corner of the heading (if checkboxes are enabled).
        heading_row_color: See DataTable [heading_row_color](https://flet.dev/docs/controls/datatable#heading_row_color).
        heading_row_decoration: **NEW!** Decoration to be applied to the heading row. When both `heading_row_color` and 'heading_row_decoration' are provided:`heading_row_decoration` takes precedence if there're 0 or 1 fixed rows; `headeing_row_color` is applied to fixed top starting from the second row; when there're both fixed top rows and fixed left columns with `fixed_corner_color` provided, this decoration overrides top left corner cell color.
        heading_row_height: See DataTable [heading_row_height](https://flet.dev/docs/controls/datatable#heading_row_height).
        heading_text_style: See DataTable [heading_text_style](https://flet.dev/docs/controls/datatable#heading_text_style).
        horizontal_lines: See DataTable [horizontal_lines](https://flet.dev/docs/controls/datatable#horizontal_lines).
        horizontal_margin: See DataTable [horizontal_margin](https://flet.dev/docs/controls/datatable#horizontal_margin).
        is_horizontal_scroll_bar_visible: **NEW!** Determines whether the horizontal scroll bar is visible.
        is_vertical_scroll_bar_visible: **NEW!** Determines whether the vertical scroll bar is visible.
        lm_ratio: **NEW!** Determines ratio of `Large` column's width to `Medium` column's width. I.e. `2.0` means that `Large` column is twice wider than `Medium` column. Defaults to `1.2`.
        min_width: **NEW!** If set, the table will stop shrinking below the threshold and provide horizontal scrolling. Useful for the cases with narrow screens (e.g. portrait phone orientation) and lots of columns.
        on_select_all: See DataTable [on_select_all](https://flet.dev/docs/controls/datatable#on_select_all).
        rows: A list of [DataRow2](datarow2.md) controls defining table rows.
        show_bottom_border: See DataTable [show_bottom_border](https://flet.dev/docs/controls/datatable#show_bottom_border).
        show_checkbox_column: See DataTable [show_checkbox_column](https://flet.dev/docs/controls/datatable#show_checkbox_column).
        show_heading_checkbox: **NEW!** Whether to display heading checkbox or not, if the checkbox column is present. Defaults to True.
        sm_ratio: **NEW!** Determines ratio of `Small` column's width to `Medium` column's width. I.e. `0.5` means that `Small` column is twice narrower than `Medium` column. Defaults to `0.67`.
        sort_arrow_animation_duration: **NEW!** When changing sort direction an arrow icon in the header is rotated clockwise. The value defines the duration of the rotation animation. Defaults to 150 milliseconds.
        sort_arrow_icon: **NEW!** Icon to be displayed when sorting is applied to a column. Defaults to `Icons.ARROW_UPWARD`.
        sort_ascending: See DataTable [sort_ascending](https://flet.dev/docs/controls/datatable#sort_ascending).
        sort_column_index: See DataTable [sort_column_index](https://flet.dev/docs/controls/datatable#sort_column_index).
        vertical_lines: See DataTable [vertical_lines](https://flet.dev/docs/controls/datatable#vertical_lines).



    """

    columns: List[DataColumn2]
    rows: Optional[List[DataRow2]] = None
    empty: Optional[ft.Control] = None
    bottom_margin: ft.OptionalNumber = None
    lm_ratio: ft.Number = 1.2
    sm_ratio: ft.Number = 0.67
    fixed_left_columns: int = 0
    fixed_top_rows: int = 1
    fixed_columns_color: Optional[ft.ColorValue] = None
    fixed_corner_color: Optional[ft.ColorValue] = None
    min_width: ft.OptionalNumber = None
    sort_ascending: bool = False
    show_checkbox_column: bool = False
    show_heading_checkbox: bool = True
    heading_checkbox_theme: Optional[ft.CheckboxTheme] = None
    data_row_checkbox_theme: Optional[ft.CheckboxTheme] = None
    sort_column_index: Optional[int] = None
    sort_arrow_icon: ft.IconValue = ft.Icons.ARROW_UPWARD
    sort_arrow_animation_duration: ft.DurationValue = field(
        default_factory=lambda: ft.Duration(milliseconds=150)
    )
    show_bottom_border: bool = False
    is_horizontal_scroll_bar_visible: Optional[bool] = None
    is_vertical_scroll_bar_visible: Optional[bool] = None
    border: Optional[ft.Border] = None
    border_radius: Optional[ft.BorderRadiusValue] = None
    horizontal_lines: Optional[ft.BorderSide] = None
    vertical_lines: Optional[ft.BorderSide] = None
    checkbox_horizontal_margin: ft.OptionalNumber = None
    checkbox_alignment: ft.Alignment = field(
        default_factory=lambda: ft.alignment.center
    )
    column_spacing: ft.OptionalNumber = None
    data_row_color: ft.ControlStateValue[ft.ColorValue] = None
    data_row_height: ft.OptionalNumber = None
    # data_row_min_height: OptionalNumber = None,
    # data_row_max_height: OptionalNumber = None,
    data_text_style: Optional[ft.TextStyle] = None
    bgcolor: Optional[ft.ColorValue] = None
    gradient: Optional[ft.Gradient] = None
    divider_thickness: ft.OptionalNumber = None
    heading_row_color: ft.ControlStateValue[ft.ColorValue] = None
    heading_row_height: ft.OptionalNumber = None
    heading_text_style: Optional[ft.TextStyle] = None
    heading_row_decoration: Optional[ft.BoxDecoration] = None
    horizontal_margin: ft.OptionalNumber = None
    clip_behavior: ft.ClipBehavior = field(default_factory=lambda: ft.ClipBehavior.NONE)
    on_select_all: ft.OptionalControlEventCallable = None

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
