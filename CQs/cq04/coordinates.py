"""coordsinates"""

__author__ = "730653037"


def get_coords(xs: str, ys: str) -> None:
    i = 0
    while i < len(xs):
        j = 0
        while j < len(ys):
            print(f"({xs[i]}, {ys[j]})")
            """innermost part of the loop, includes the print"""
            j += 1
        i += 1
        """outer part of the loop"""
