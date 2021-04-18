"""Utility functions for wrangling data."""

__author__ = "730411656"


from csv import DictReader


def read_csv_rows(csv_file: str) -> list[dict[str, str]]:
    """Read a CSV file's contents into a list of rows."""
    # list of rows
    rows: list[dict[str, str]] = []
    
    # TODO 0.1) Complete the implementation of this function here.
    file_handle = open(csv_file, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        rows.append(row)
    file_handle.close()
    return rows
    
# TODO: Define the other functions here.


def column_values(table: list[dict[str, str]], column_name: str) -> list[str]:
    """Read a CSV file's content into a list of columns."""
    columns = []
    for row in table:
        for column in row:
            if column == column_name:
                columns.append(row[column])
    return columns


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a table represented as a list of rows into one as a dictionary of columns."""
    columns: dict[str, list[str]] = {}
    for column in table[0]:
        columns[column] = column_values(table, column)

    return columns    


def head(table: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first N."""
    newrows: dict[str, list[str]] = {}
    for column in table:
        rows = []
        if N >= len(table[column]):
            N = len(table[column])
        for row in range(N):
            rows.append(table[column][row])
        newrows[column] = rows 
    return newrows


def select(table: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Produces a new column based table with a subset of original columns."""
    newrows: dict[str, list[str]] = {}
    for column in columns:
        newrows[column] = table[column]
    return newrows


def count(values: list[str]) -> dict[str, int]:
    """Produces dictionary where each key is a unique value."""
    keys: dict[str, int] = {}
    for key in values:
        if key in keys:
            keys[key] += 1
        else:
            keys[key] = 1
    return keys

def masked(col: list[str], threshold: str) -> list[bool]:
    """Masks a list into a list of bools first step of filtering."""
    result: list[bool] = []
    for item in col:
            result.append(item == threshold)
    return result


def filter(col: list[bool], mask:list[bool]) -> list[str]:
    """Filters the data, a list[bool] against list[bool]."""
    result: list[bool] = []
    for i in range(len(mask)):
        if mask[i] == True and col[i] == True:
            result.append(True)
        else:
            result.append(False)
    return result
