import json

INPUT_FILE = "input.csv"

def csv_to_list_dict(file, delimiter=',', new_line='\n') -> list[dict]:
    output = []
    count = 0
    with open(file, encoding='utf-8') as file:
        for line in file:
            count += 1
            if count == 1:
                keys = line.split(delimiter)
                continue
            data = line.split(delimiter)
            collection = {keys[i]: data[i] for i in range(len(keys))}
            output.append(collection)
    return output

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
