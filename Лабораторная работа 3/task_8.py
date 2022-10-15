money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
month = 0  # количество месяцев, которое можно прожить

while money_capital - spend > 0: # пока у нас есть деньги на оплату расходов
    if month == 0: # если это 0 месяц то не будем прибавлять коэффициент роста цен
        money_capital = (money_capital - spend) + salary # расчет подушки безопасности к концу месяца
        month += 1 # месяц успешно прожит
    else:
        spend = spend + spend * increase # коэффициент роста цен
        money_capital = (money_capital - spend) + salary
        month += 1

print(month)
