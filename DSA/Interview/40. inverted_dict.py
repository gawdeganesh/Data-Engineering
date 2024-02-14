"""
Given a dictionary mapping items to their prices, create a new dictionary where keys are prices, and values are lists of items with that price.
"""


def inverted_dict(input_dict: dict[str:int]) -> dict[int:list]:
    inv_dict = {}

    for k, v in input_dict.items():
        if v not in inv_dict:
            inv_dict[v] = []

        inv_dict[v].append(k)

    return inv_dict


print(
    inverted_dict(
        {
            "apple": 2,
            "avocado": 1,
            "sauce": 2,
            "banana": 1,
            "berries": 3,
        }
    )
)
