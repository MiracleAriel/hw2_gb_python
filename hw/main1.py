def find_duplicate_elements(input_list):
    seen = set()
    duplicates = set()

    for element in input_list:
        if element in seen:
            duplicates.add(element)
        else:
            seen.add(element)

    unique_duplicates = list(duplicates)
    return unique_duplicates

# Пример списка с повторяющимися элементами
input_list = [1, 2, 3, 4, 2, 3, 5, 1, 6, 7, 8, 9, 7, 6]

# Поиск дублирующихся элементов без дубликатов
result_list = find_duplicate_elements(input_list)
print("Исходный список:", input_list)
print("Список с дублирующимися элементами без дубликатов:", result_list)
