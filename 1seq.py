num = int(input("Введите количество элементов: "))
lst = []

for i in range(num):
    elem = int(input(f"Введите {i+1} элемент: "))
    lst.append(elem)

sorted_lst = sorted(lst)
print(f"Вывод: {sorted_lst}")