d = []
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = float(input('Введите сумму:'))
d.append(round(float(per_cent['ТКБ']*money/100),2))
d.append(round(float(per_cent['СКБ']*money/100),2))
d.append(round(float(per_cent['ВТБ']*money/100),2))
d.append(round(float(per_cent['СБЕР']*money/100),2))

print(d)

print('Максимальная сумма, которую Вы можете получить - ', max(d))
