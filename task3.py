def cheapest_items(shops):
    data = {}

    for idx in range(len(shops)):
        for key, value in shops[idx].items():
            if key not in data or data[key][1] > value:
                data[key] = [idx, value]

    return data


def cheapest_shop_total(shops):
    data = {}

    for idx in range(len(shops)):
        data[idx] = sum(shops[idx].values())

    return min(data, key=data.get)


# # --- Набор 1 ---
shops1 = [
    {"хлеб": 1, "молоко": 2},
    {"хлеб": 0.8, "молоко": 2.5},
    {"хлеб": 1.2, "молоко": 1.9},
]

assert cheapest_items(shops1)["хлеб"][0] == 1, "Неверный магазин для хлеба (shops1)"
assert cheapest_items(shops1)["молоко"][0] == 2, "Неверный магазин для молока (shops1)"
assert cheapest_items(shops1)["хлеб"][1] == 0.8, "Неверная цена хлеба (shops1)"
assert cheapest_items(shops1)["молоко"][1] == 1.9, "Неверная цена молока (shops1)"
assert cheapest_shop_total(shops1) == 0, "Неверный магазин по сумме (shops1)"


# --- Набор 2 ---
shops2 = [
    {"яблоко": 3, "банан": 2, "киви": 5},
    {"яблоко": 2.5, "банан": 2.2, "киви": 4.8},
    {"яблоко": 3.1, "банан": 1.9, "киви": 5.1},
]

assert cheapest_items(shops2)["яблоко"][0] == 1, "Неверный магазин для яблок (shops2)"
assert cheapest_items(shops2)["банан"][0] == 2, "Неверный магазин для бананов (shops2)"
assert cheapest_items(shops2)["киви"][0] == 1, "Неверный магазин для киви (shops2)"
assert cheapest_shop_total(shops2) == 1, "Неверный магазин по сумме (shops2)"
assert cheapest_items(shops2)["банан"][1] == 1.9, "Неверная цена банана (shops2)"


# --- Набор 3 ---
shops3 = [
    {"рис": 4.5, "гречка": 3.2},
    {"рис": 4.4, "гречка": 3.5},
    {"рис": 4.6, "гречка": 3.0},
]

assert cheapest_items(shops3)["рис"][0] == 1, "Неверный магазин для риса (shops3)"
assert cheapest_items(shops3)["гречка"][0] == 2, "Неверный магазин для гречки (shops3)"
assert cheapest_shop_total(shops3) == 2, "Неверный магазин по сумме (shops3)"
assert cheapest_items(shops3)["гречка"][1] == 3.0, "Неверная цена гречки (shops3)"
assert cheapest_items(shops3)["рис"][1] == 4.4, "Неверная цена риса (shops3)"


# --- Набор 4 ---
shops4 = [
    {"масло": 5.5, "сыр": 7.2, "йогурт": 2.1},
    {"масло": 5.4, "сыр": 7.5, "йогурт": 2.0},
    {"масло": 5.6, "сыр": 7.0, "йогурт": 2.3},
]

assert cheapest_items(shops4)["масло"][0] == 1, "Неверный магазин для масла (shops4)"
assert cheapest_items(shops4)["сыр"][0] == 2, "Неверный магазин для сыра (shops4)"
assert cheapest_items(shops4)["йогурт"][0] == 1, "Неверный магазин для йогурта (shops4)"
assert cheapest_shop_total(shops4) == 0, "Неверный магазин по сумме (shops4)"
assert cheapest_items(shops4)["сыр"][1] == 7.0, "Неверная цена сыра (shops4)"
