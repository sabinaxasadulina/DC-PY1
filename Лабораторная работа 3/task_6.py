# Дан целочисленный список, состоящий из 10 элементов. Поменять местами первый максимальный и последний элементы.
list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_index = 0
last_number = list_numbers[-1]

for current_index in range(len(list_numbers)):
    max_number = list_numbers[max_index]
    current_number = list_numbers[current_index]
    if current_number > max_number:
        max_index = current_index

list_numbers[-1] = max_number
list_numbers[max_index] = last_number

print(list_numbers)

