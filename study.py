message = 'Привет мир! А тебе есть 18?'

print(message)

age = int(input('Сколько тебе лет?'))
if (age >= 25):
    print('Добро пожаловать!')
elif (age >= 18) and (age < 25):
    print('Вход только с мамой')
else:
    print('Иди взрослей!')


def hello():
    print('Урок № 3')


hello()

x = int(input('Введите 1 число:'))
y = int(input('Введите 2 число:'))


def sum(a, b):
    return a+b


z = (sum(x, y))
print(z)


def f(a):
    return 4*a-3


print(f(5))
