# Программа для сохранения уникальных цифр из введенного списка

# Функция для получения уникальных элементов из списка
def unique_nums(input_list):
    unique_list = []
    for num in input_list:
        if input_list.count(num) == 1:
            unique_list.append(num)
    return unique_list

# Получаем введенную строку от пользователя
user_input = input("Введите цифры через запятую, точку с запятой или слэш: ")

# Разделяем введенную строку на список по разделителям
nums_list = []
if ',' in user_input:
    nums_list = user_input.split(',')
elif ';' in user_input:
    nums_list = user_input.split(';')
elif '/' in user_input:
    nums_list = user_input.split('/')

# Преобразуем элементы списка в целые числа
nums_list = [int(num) for num in nums_list]

# Получаем список уникальных элементов
unique_list = unique_nums(nums_list)

# Выводим список уникальных элементов на экран
print("Уникальные цифры из введенного списка:")
print(unique_list)