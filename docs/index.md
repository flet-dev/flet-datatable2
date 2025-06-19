# flet-datatable2

[![pypi](https://img.shields.io/pypi/v/flet-datatable2.svg)](https://pypi.python.org/pypi/flet-datatable2)
[![downloads](https://static.pepy.tech/badge/flet-datatable2/month)](https://pepy.tech/project/flet-datatable2)
[![license](https://img.shields.io/github/license/flet-dev/flet-datatable2.svg)](https://github.com/flet-dev/flet-datatable2/blob/main/LICENSE)

An enhanced DataTable for Flet apps that builds on the built-in component by adding sticky headers,
fixed top rows, and fixed left columns while preserving all core features.

It is based on [data_table_2](https://pub.dev/packages/data_table_2) Flutter package.

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

## Usage

### Installation

To install the `flet-datatable2` package and add it to your project dependencies:

=== "uv"
    ```bash
    uv add flet-datatable2
    ```

=== "pip"
    ```bash
    pip install flet-datatable2  # (1)!
    ```

=== "poetry"
    ```bash
    poetry add flet-datatable2
    ```

1. After this, you will have to manually add this package to your `requirements.txt` or `pyproject.toml`.

## Examples

[Live demo](https://flet-controls-gallery.fly.dev/layout/datatable2)

### Example 1

```python
--8<-- "examples/datatable2_example/src/example-1.py"
```

### Example 2

![DataTable2 example 2](assets/example-2.gif)

```
```python
--8<-- "examples/datatable2_example/src/example-2.py"
```
