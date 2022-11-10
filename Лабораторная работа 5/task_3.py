import random

required_len_list = 15
min_range = -10
max_range = 10

def get_unique_list_numbers() -> list[int]:
    output = []
    while len(output) < required_len_list:
        random_unit = random.randint(min_range, max_range)
        if random_unit not in output:
            output.append(random_unit)
    return output

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
