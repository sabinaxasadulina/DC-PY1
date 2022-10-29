dict_letters = {

}
def dictionary(str_):
    str_ = ''.join(str_.split())
    str_ = str_.lower()
    for i in str_:
        if i.isalpha():
            if i in dict_letters:
                dict_letters[i] += 1
            else:
                dict_letters[i] = 1
    return dict_letters

def get_count_char(dict_):
    total_count = sum(dict_.values())
    for i in dict_:
        dict_[i] = round(dict_[i] / total_count * 100, 2)
    return dict_

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(dictionary(main_str))
print(get_count_char(dict_letters))

