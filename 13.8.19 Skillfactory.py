count = abs(int(input("Введите количество билетов: ")))
i = 1
price = 0

while i <= count:
    age = int(input("Введите возраст посетителя ", ))
    if 0 <= age < 18:
        i += 1
    elif 18 <= age < 25:
        price += 990
        i += 1
    elif 118 >= age > 25: #самому старому человеку на планете 118 лет (на 2021 год)
        price += 1390
        i += 1
    else:
        print("Указан некорректный возраст")

if price > 0:
    if count > 3:
        price *= 0.9
    print("Сумма к оплате: ", price)
else:
    print("Должен быть хотя бы один взрослый сопровождающий")
