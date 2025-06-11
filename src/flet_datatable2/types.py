from enum import Enum

__all__ = ["DataColumnSize"]

class DataColumnSize(Enum):
    """
    Relative size of a column determines the share of total table
    width allocated to each individual column.

    When determining column widths, ratios between `S`, `M` and `L`
    columns are kept (i.e. Large columns are set to 1.2x width of Medium ones).

    See [`DataTable2.sm_ratio`][(p).datatable2.], [`DataTable2.lm_ratio`][(p).datatable2.].
    """

    S = "s"
    M = "m"
    L = "l"