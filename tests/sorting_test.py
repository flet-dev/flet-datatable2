import flet as ft
from data import desserts

import flet_datatable2 as ftd


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def select_row(e: ft.ControlEvent):
        print("on_select_row")
        e.control.selected = not e.control.selected
        e.control.update()

    def sort_column(e: ft.DataColumnSortEvent):
        print(f"Sorting column {e.column_index}, ascending={e.ascending}")

    def all_selected(e: ft.ControlEvent):
        print("All selected")

    def get_data_columns():
        data_columns = [
            ftd.DataColumn2(
                ft.Text("Name"),
                size=ftd.DataColumnSize.L,
                on_sort=sort_column,
                heading_row_alignment=ft.MainAxisAlignment.START,
            ),
            ftd.DataColumn2(
                ft.Text("Calories"),
                on_sort=sort_column,
                numeric=True,
                heading_row_alignment=ft.MainAxisAlignment.END,
            ),
            ftd.DataColumn2(
                ft.Text("Fat"),
                on_sort=sort_column,
                numeric=True,
            ),
            ftd.DataColumn2(
                ft.Text("Carbs"),
                on_sort=sort_column,
                numeric=True,
            ),
            ftd.DataColumn2(
                ft.Text("Protein"),
                on_sort=sort_column,
                numeric=True,
            ),
            ftd.DataColumn2(
                ft.Text("Sodium"),
                on_sort=sort_column,
                numeric=True,
            ),
            ftd.DataColumn2(
                ft.Text("Calcium"),
                on_sort=sort_column,
                numeric=True,
            ),
            ftd.DataColumn2(
                ft.Text("Iron"),
                on_sort=sort_column,
                numeric=True,
            ),
        ]
        return data_columns

    def get_data_rows(desserts):
        data_rows = []
        for dessert in desserts:
            data_rows.append(
                ftd.DataRow2(
                    specific_row_height=50,
                    on_select_changed=select_row,
                    cells=[
                        ft.DataCell(content=ft.Text(dessert.name)),
                        ft.DataCell(content=ft.Text(dessert.calories)),
                        ft.DataCell(content=ft.Text(dessert.fat)),
                        ft.DataCell(content=ft.Text(dessert.carbs)),
                        ft.DataCell(content=ft.Text(dessert.protein)),
                        ft.DataCell(content=ft.Text(dessert.sodium)),
                        ft.DataCell(content=ft.Text(dessert.calcium)),
                        ft.DataCell(content=ft.Text(dessert.iron)),
                    ],
                )
            )
        return data_rows

    page.add(
        dt := ftd.DataTable2(
            show_checkbox_column=True,
            expand=True,
            column_spacing=0,
            heading_row_color=ft.Colors.SECONDARY_CONTAINER,
            horizontal_margin=12,
            sort_ascending=True,
            bottom_margin=10,
            min_width=600,
            on_select_all=all_selected,
            columns=get_data_columns(),
            rows=get_data_rows(desserts),
        ),
    )


ft.run(main)
