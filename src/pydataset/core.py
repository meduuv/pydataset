def select_columns(rows, columns):
    """Return rows containing only the requested columns."""
    columns = tuple(columns)
    return [{column: row[column] for column in columns if column in row} for row in rows]


def filter_rows(rows, predicate):
    """Return rows for which predicate returns true."""
    return [row for row in rows if predicate(row)]


def summarize(rows):
    """Return row count and non-empty column counts."""
    rows = list(rows)
    keys = sorted({key for row in rows for key in row})
    return {
        "rows": len(rows),
        "columns": {key: sum(key in row and row[key] is not None for row in rows) for key in keys},
    }
