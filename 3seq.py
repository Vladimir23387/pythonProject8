# Ввод элементов 1-го списка
input_list1 = input("Введите элементы 1-го списка через запятую: ").split(",")

# Ввод элементов 2-го списка
input_list2 = input("Введите элементы 2-го списка через запятую: ").split(",")

# Преобразование в множества для удобства операций
set1 = set(input_list1)
set2 = set(input_list2)

# Удаление элементов из первого списка, которые присутствуют во втором
result_set = set1 - set2

# Вывод результата
print("Результат:", ",".join(result_set))