def knapsack(items, max_weight):
    def helper(item_index, current_weight, selected_items):
        if item_index == len(items):
            return selected_items

        item = items[item_index]
        item_weight = item[1]

        if current_weight + item_weight <= max_weight:
            # Попробовать добавить текущий предмет в рюкзак
            with_item = helper(item_index + 1, current_weight + item_weight, selected_items + [item])

            # Попробовать пропустить текущий предмет
            without_item = helper(item_index + 1, current_weight, selected_items)

            # Выбрать вариант с наибольшей общей массой
            if sum(weight for _, weight in with_item) > sum(weight for _, weight in without_item):
                return with_item
            else:
                return without_item
        else:
            # Пропустить текущий предмет, так как его масса превышает грузоподъемность
            return helper(item_index + 1, current_weight, selected_items)

    return helper(0, 0, [])

# Пример словаря с вещами для похода, где ключ - название вещи, значение - масса
items = {
    'Палатка': 3,
    'Спальный мешок': 2,
    'Термос': 1,
    'Посуда': 4,
    'Кружка': 1,
    'Фонарик': 2,
    'Карта': 1,
    'Палка для похода': 2,
    'Компас': 1,
    'Плащ': 3
}

# Максимальная грузоподъемность рюкзака
max_weight = 10

# Определение вещей, влезающих в рюкзак
selected_items = knapsack(list(items.items()), max_weight)

print("Максимальная грузоподъемность рюкзака:", max_weight)
print("Выбранные предметы:")
for item, weight in selected_items:
    print(item, "- масса:", weight)
