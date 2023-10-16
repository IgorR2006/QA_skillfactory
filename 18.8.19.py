visitors = int(input('число посетителей: ' ))

sum = 0

List_age_visitors = [int(input(f"введите возраст посетителя #{i+1}: ")) for i in range(visitors)]

for age in List_age_visitors:
    if age >= 25:
        sum += 1390
    elif 18 <= age < 25:
        sum +=990
        
if visitors > 3:
      sum1 = sum - sum*0.1
      print(f"сумма к оплате: {sum1}, с учетом скидки за регистрацию {visitors} посетителей ")
elif age < 18:
      print('Посетителям конференции менее 18 лет, вход бесплатный')    

else:
      print(f"сумма к оплате: {sum}")
    
