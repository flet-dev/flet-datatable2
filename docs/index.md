# flet-datatable2

An enhanced DataTable for Flet apps.
It extends Flet’s built-in DataTable with additional functionality such as sticky headers, fixed top rows, and fixed left columns, while retaining all core features of the original.

It is based on [DataTable2](https://pub.dev/packages/data_table_2) Flutter package.

## Platform Support

This package supports the following platforms:

| Platform | Supported |
|----------|:---------:|
| Windows  |     ✅     |
| macOS    |     ✅     |
| Linux    |     ✅     |
| iOS      |     ✅     |
| Android  |     ✅     |
| Web      |     ✅     |

## Installation

Add dependency to `pyproject.toml` of your Flet app:

```
dependencies = [
  "flet-datatable2 @ git+https://github.com/flet-dev/flet_datatable2.git",
  "flet>=0.27.4",
]
```

Build your app:
```
flet build macos -v
```

## Examples

[Live example](https://flet-controls-gallery.fly.dev/layout/datatable2)

### DataTable2 with `empty` property and no data rows

```
import flet as ft
from flet_datatable2 import DataColumn2, DataTable2

def main(page: ft.Page):
    page.add(
        DataTable2(
            columns=[
                DataColumn2(ft.Text("First name")),
                DataColumn2(ft.Text("Last name")),
                DataColumn2(ft.Text("Age"), numeric=True),
            ],
            empty=ft.Text("This table is empty."),
        ),
    )


ft.app(main)
```

### DataTable2 with fixed heading row and sorting

<img src="assets/datatable2-example.gif">

See source code for this example [here](https://github.com/flet-dev/flet_datatable2/tree/main/examples/flet_datatable2_example/src).


