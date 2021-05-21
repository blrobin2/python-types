from typing import List


def get_full_name(first_name: str, last_name: str):
    return first_name.title() + " " + last_name.title()


def get_name_with_age(name: str, age: int):
    return name + " is this old: " + str(age)


def get_items(
    item_a: str,
    item_b: int,
    item_c: float,
    item_d: bool,
    item_e: bytes
):
    return item_a, item_b, item_c, item_d, item_e


def process_items(items: List[str]):
    for item in items:
        print(item)
