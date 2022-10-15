salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение
for current_month in range(months):
    if current_month == 0: # если это 0 месяц то не будем прибавлять коэффициент роста цен
        extra_money = spend - salary # сколько дополнительных денег нам нужно в этом месяце
        need_money += extra_money # суммируем в общую сумму
    else:
        spend = spend + spend * increase
        extra_money = spend - salary
        need_money += extra_money

print(round(need_money))
