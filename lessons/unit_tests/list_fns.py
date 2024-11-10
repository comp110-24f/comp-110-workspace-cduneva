def get_first(list1: list[str]) -> str:
    return list1[0]


def remove_first(list1: list[str]) -> None:
    list1.pop(0)


def get_and_remove_first(list1: list[str]) -> str:
    first_element: str = list1[0]
    list1.pop(0)
    return first_element
