message = 'Привет мир! А тебе есть 18?'

print(message)

age = int(input('Сколько тебе лет?'))
if (age >= 25):
    print('Добро пожаловать!')
elif (age >= 18) and (age < 25):
    print('Вход только с мамой')
else:
    print('Иди взрослей!')
