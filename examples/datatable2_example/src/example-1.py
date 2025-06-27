import flet as ft

import flet_datatable2 as fdt


def main(page: ft.Page):
    page.add(
        fdt.DataTable2(
            empty=ft.Text("This table is empty."),
            columns=[
                fdt.DataColumn2(ft.Text("First name")),
                fdt.DataColumn2(ft.Text("Last name")),
                fdt.DataColumn2(ft.Text("Age"), numeric=True),
            ],
        ),
    )


ft.run(main)
