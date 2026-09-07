import csv
from io import StringIO
from typing import Optional


def parse_csv(data: str) -> list[dict]:
    reader = csv.DictReader(StringIO(data))
    return list(reader)


def compute_revenue(rows: list[dict]) -> float:
    return sum(int(row["quantity"]) * float(row["price"]) for row in rows)


def top_item(rows: list[dict]) -> Optional[dict]:
    if not rows:
        return None
    return max(rows, key=lambda row: int(row["quantity"]) * float(row["price"]))


CSV_DATA = """date,item,quantity,price
2026-09-01,Тетрадь,3,12.5
2026-09-02,Ручка,10,4
2026-09-03,Альбом,2,30
"""

ROWS = parse_csv(CSV_DATA)
TOTAL_REVENUE = compute_revenue(ROWS)
TOP_ITEM = top_item(ROWS)


if __name__ == "__main__":
    rows_before = [row.copy() for row in ROWS]

    parsed_again = parse_csv(CSV_DATA)
    revenue_again = compute_revenue(ROWS)
    top_again = top_item(ROWS)

    print("parse_csv:", ROWS, "| детерминирована:", ROWS == parsed_again)
    print("compute_revenue:", TOTAL_REVENUE, "| детерминирована:", TOTAL_REVENUE == revenue_again)
    print("top_item:", TOP_ITEM, "| детерминирована:", TOP_ITEM == top_again)
    print("Аргументы не изменены:", ROWS == rows_before)
