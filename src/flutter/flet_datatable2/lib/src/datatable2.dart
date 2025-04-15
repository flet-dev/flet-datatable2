import 'package:collection/collection.dart';
import 'package:data_table_2/data_table_2.dart';
import 'package:flet/flet.dart' as ft;
import 'package:flet/flet.dart';
import 'package:flutter/material.dart';

class DataTable2Control extends StatefulWidget {
  final Control control;

  const DataTable2Control({
    super.key,
    required this.control,
  });

  @override
  State<DataTable2Control> createState() => _DataTable2ControlState();
}

class _DataTable2ControlState extends State<DataTable2Control> {
  //final ScrollController _horizontalController = ScrollController();
  //final ScrollController _controller = ScrollController();

  // @override
  // void dispose() {
  //   _horizontalController.dispose();
  //   _controller.dispose();
  //   super.dispose();
  // }

  @override
  Widget build(BuildContext context) {
    debugPrint("DataTable2Control build: ${widget.control.id}");

    ColumnSize? parseSize(String? size, [ColumnSize? defValue]) {
      if (size == null) {
        return defValue;
      }
      return ColumnSize.values.firstWhereOrNull(
              (e) => e.name.toLowerCase() == size.toLowerCase()) ??
          defValue;
    }

    var bgColor = widget.control.getString("bgcolor");
    var border = widget.control.getBorder("border", Theme.of(context));
    var borderRadius = widget.control.getBorderRadius("border_radius");
    var gradient = widget.control.getGradient("gradient", Theme.of(context));
    var horizontalLines =
        widget.control.getBorderSide("horizontal_lines", Theme.of(context));
    var verticalLines =
        widget.control.getBorderSide("vertical_lines", Theme.of(context));
    var defaultDecoration =
        Theme.of(context).dataTableTheme.decoration ?? const BoxDecoration();

    BoxDecoration? decoration;
    if (bgColor != null ||
        border != null ||
        borderRadius != null ||
        gradient != null) {
      decoration = (defaultDecoration as BoxDecoration).copyWith(
          color: parseColor(bgColor, Theme.of(context)),
          border: border,
          borderRadius: borderRadius,
          gradient: gradient);
    }

    TableBorder? tableBorder;
    if (horizontalLines != null || verticalLines != null) {
      tableBorder = TableBorder(
          horizontalInside: horizontalLines ?? BorderSide.none,
          verticalInside: verticalLines ?? BorderSide.none);
    }

    var datatable2 = DataTable2(
      bottomMargin: widget.control.getDouble("bottom_margin"),
      minWidth: widget.control.getDouble("minWidth"),
      //horizontalScrollController: _horizontalController,
      //scrollController: _controller,
      decoration: decoration,
      border: tableBorder,
      empty: widget.control.buildWidget("empty"),
      isHorizontalScrollBarVisible:
          widget.control.getBool("is_horizontal_scroll_bar_visible"),
      isVerticalScrollBarVisible:
          widget.control.getBool("is_vertical_scroll_bar_visible"),
      fixedLeftColumns: widget.control.getInt("fixed_left_columns") ?? 0,
      fixedTopRows: widget.control.getInt("fixed_top_rows") ?? 1,
      fixedColumnsColor:
          widget.control.getColor("fixed_columns_color", context),
      fixedCornerColor: widget.control.getColor("fixed_corner_color", context),
      smRatio: widget.control.getDouble("sm_ratio") ?? 0.67,
      lmRatio: widget.control.getDouble("lm_ratio") ?? 1.2,
      clipBehavior: widget.control.getClipBehavior("clip_behavior", Clip.none)!,
      sortArrowIcon:
          widget.control.getIcon("sort_arrow_icon") ?? Icons.arrow_upward,
      sortArrowAnimationDuration:
          widget.control.getDuration("sort_arrow_animation_duration") ??
              Duration(microseconds: 150),
      checkboxHorizontalMargin:
          widget.control.getDouble("checkbox_horizontal_margin"),
      checkboxAlignment:
          widget.control.getAlignment("checkboxAlignment", Alignment.center)!,
      headingCheckboxTheme: widget.control
          .getCheckboxTheme("heading_checkbox_theme", Theme.of(context)),
      datarowCheckboxTheme: widget.control
          .getCheckboxTheme("data_row_checkbox_theme", Theme.of(context)),
      showHeadingCheckBox:
          widget.control.getBool("show_heading_checkbox", true)!,
      columnSpacing: widget.control.getDouble("column_spacing"),
      dataRowColor: widget.control
          .getWidgetStateColor("data_row_color", Theme.of(context)),
      dataRowHeight: widget.control.getDouble("data_row_height"),
      //dataRowMinHeight: widget.control.attrDouble("dataRowMinHeight"),
      //dataRowMaxHeight: widget.control.attrDouble("dataRowMaxHeight"),
      dataTextStyle:
          widget.control.getTextStyle("data_text_style", Theme.of(context)),
      headingRowColor: widget.control
          .getWidgetStateColor("heading_row_color", Theme.of(context)),
      headingRowHeight: widget.control.getDouble("heading_row_height"),
      headingTextStyle:
          widget.control.getTextStyle("heading_text_style", Theme.of(context)),
      headingRowDecoration:
          widget.control.getBoxDecoration("heading_row_decoration", context),
      dividerThickness: widget.control.getDouble("divider_thickness"),
      horizontalMargin: widget.control.getDouble("horizontal_margin"),
      showBottomBorder: widget.control.getBool("show_bottom_border", false)!,
      showCheckboxColumn:
          widget.control.getBool("show_checkbox_column", false)!,
      sortAscending: widget.control.getBool("sort_ascending", false)!,
      sortColumnIndex: widget.control.getInt("sort_column_index"),
      onSelectAll: widget.control.getBool("on_select_all", false)!
          ? (selected) {
              widget.control.triggerEvent("select_all", selected);
            }
          : null,
      columns: widget.control.children("columns").map((column) {
        column.notifyParent = true;
        return DataColumn2(
            //size: ColumnSize.S,
            size: parseSize(column.getString("size"), ColumnSize.S)!,
            fixedWidth: column.getDouble("fixed_width"),
            numeric: column.getBool("numeric", false)!,
            tooltip: column.getString("tooltip"),
            headingRowAlignment:
                column.getMainAxisAlignment("heading_row_alignment"),
            //mouseCursor: WidgetStateMouseCursor.clickable,
            onSort: column.getBool("on_sort", false)!
                ? (columnIndex, ascending) {
                    column.triggerEvent(
                        "sort", {"i": columnIndex, "a": ascending});
                  }
                : null,
            label: column.buildWidget("label")!);
      }).toList(),
      rows: widget.control.children("rows").map((row) {
        row.notifyParent = true;
        return DataRow2(
          key: ValueKey(row.id),
          selected: row.getBool("selected", false)!,
          color: row.getWidgetStateColor("color", Theme.of(context)),
          specificRowHeight: row.getDouble("specific_row_height"),
          decoration: row.getBoxDecoration("decoration", context),
          onSelectChanged: row.getBool("on_select_changed", false)!
              ? (selected) {
                  row.triggerEvent("select_changed", selected);
                }
              : null,
          onLongPress: row.getBool("on_long_press", false)!
              ? () {
                  row.triggerEvent("long_press");
                }
              : null,
          onDoubleTap: row.getBool("on_double_tap", false)!
              ? () {
                  row.triggerEvent("double_tap");
                }
              : null,
          onTap: row.getBool("on_tap", false)!
              ? () {
                  row.triggerEvent("tap");
                }
              : null,
          onSecondaryTap: row.getBool("on_secondary_tap", false)!
              ? () {
                  row.triggerEvent("secondary_tap");
                }
              : null,
          onSecondaryTapDown: row.getBool("on_secondary_tap_sown", false)!
              ? (details) {
                  row.triggerEvent("secondary_tap_down");
                }
              : null,
          cells: row.children("cells").map((cell) {
            cell.notifyParent = true;
            return DataCell(
              cell.buildWidget("content")!,
              placeholder: cell.getBool("placeholder", false)!,
              showEditIcon: cell.getBool("show_edit_icon", false)!,
              onDoubleTap: cell.getBool("on_double_tap", false)!
                  ? () {
                      cell.triggerEvent("double_tap");
                    }
                  : null,
              onLongPress: cell.getBool("on_long_press", false)!
                  ? () {
                      cell.triggerEvent("long_press");
                    }
                  : null,
              onTap: cell.getBool("on_tap", false)!
                  ? () {
                      cell.triggerEvent("tap");
                    }
                  : null,
              onTapCancel: cell.getBool("on_tap_cancel", false)!
                  ? () {
                      cell.triggerEvent("tap_cancel");
                    }
                  : null,
              onTapDown: cell.getBool("on_tap_down", false)!
                  ? (details) {
                      cell.triggerEvent("tap_down", {
                        "kind": details.kind?.name,
                        "lx": details.localPosition.dx,
                        "ly": details.localPosition.dy,
                        "gx": details.globalPosition.dx,
                        "gy": details.globalPosition.dy,
                      });
                    }
                  : null,
            );
          }).toList(),
        );
      }).toList(),
    );

    return ConstrainedControl(control: widget.control, child: datatable2);
  }
}
