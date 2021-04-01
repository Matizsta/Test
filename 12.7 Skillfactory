per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму: "))/100
float_deposit = [i * money for i in per_cent.values()]
deposit = list(map(round, float_deposit))

print(deposit)
print("Максимальная сумма, которую вы можете заработать — ", max(deposit))
