"""
Задание 1
 Пользователь вводитсклавиатурыстроку.Проверьте
является ли введенная строка палиндромом. Палин
слева направо и справа налево. Например, кок; А роза
упала на лапу Азора; доход; А буду я у дуба.
"""
"""
palindrom = "а роза упала на лапу азора"
print(palindrom.replace(" ", "")[::-1])

if palindrom.replace(" ", "") == palindrom.replace(" ", "")[::-1]:
    print("Эта строка является палиндромом")
else:
    print("Эта строка не палиндром")
"""





"""
 Задание 2
 Пользователь вводит с клавиатуры некоторый текст,
после чего пользователь вводит список зарезервированных
слов. Необходимо найти в тексте все зарезервированные
слова и изменить их регистр на верхний. Вывести на
экран измененный текст.
"""

#V1 который не работает
"""
reserve = ("солнце", "лес", "река")
result = []
i = 0
while i <= 5:
    user_inp = input("Введите по одному слову c маленькой буквы через пробел:"
                     "\nсолнце, гора, лес, куртка, река")
    if user_inp == reserve[0] or reserve[1] or reserve[2]:
        print("Данное слово есть в списке! Теперь его первая буква в верхнем регистре")
        i += 1
        user_inp = user_inp[0].upper()
        result = result.append(user_inp)

    else:
        print("Этого слова в списке нет! Регистр не изменен")
        i += 1
        result = result.append(user_inp)
        continue
print("Цикл окончен. Итоговая строка: ", result)
"""
#V2

user_inp = input("Введите текст")
reserve = input("Введите список слов, "
                "\nв которых я поменяю регистр на верхний").split(",")
for i in reserve:
    result = user_inp.replace(i, i.upper())








"""
Задание 3
 Есть некоторый текст. Посчитайте в этом тексте ко
личество предложенийивыведитенаэкранполученный
результат
-------------------------------------------------------------
Задание 1
 Пользователь вводит с клавиатуры число в диапа
зоне от 1 до 100. Если число кратно 3 (делится на 3 без
остатка) нужно вывести слово Fizz. Если число кратно 5
нужновывестисловоBuzz.Есличислократно3и5нужно
вывести Fizz Buzz. Если число не кратно не 3 и 5 нужно
вывести само число.
Еслипользователь ввел значение не вдиапазонеот1
до 100 требуется вывести сообщение об ошибке.
 Задание 2
 Написать программу, которая по выбору пользова
теля возводит введенное им число в степень от нулевой
до седьмой включительно.
 Задание 3
 Написать программу подсчета стоимости разговора
для разныхмобильныхоператоров.Пользовательвводит
стоимость разговора и выбирает с какого на какой опе
ратор он звонит. Вывести стоимость на экран
Задание 4
 Зарплатаменеджерасоставляет200$+процентотпро
даж, продажидо500$—3%,от500до1000—5%,свыше
1000 — 8%. Пользователь вводит с клавиатуры уровень
продаж для трех менеджеров. Определить их зарплату,
определить лучшего менеджера, начислить ему премию
200$, вывести итоги на экран
---------------------------------------------------------------------------
Задание 1
 Показать на экран все простые числа в диапазоне,
указанном пользователем. Число называется простым,
если оноделитсябезостаткатольконасебяинаединицу.
Например, три — это простое число, а четыре нет.
 Задание 2
 Показатьнаэкранетаблицуумножениядлявсехчисел
от 1 до 10. Например:
 1 * 1 = 1          1 * 2 = 2   …..  1 * 10  = 10
 .........................................................................
 10 * 1 = 10    10 * 2 = 20 …. 10 * 10 = 100.
 Задание 3
 Показать на экран таблицу умножения в диапазоне,
указанном пользователем. Например, если пользователь
указал 3 и 5, таблица может выглядеть так

 3*1 = 3    3*2 = 6       3*3 = 9       ...     3 * 10 = 30
"""


print('1234567890'.find('r', 5, 10)) # возвращает индекс первого вхожденич подстроки

someStr = '123z121saf253'
print(someStr)

new_str = someStr.replace('123', '2')
print(new_str)
length1 = len([1, 2, 3])
length2 = len(someStr)
list2 = ['123', '123']
sorted1 = sorted(someStr)
print(sorted1)
print(''.join(sorted1))
msg = ' 3 4 456  456456 6 5 '
print(msg.split())
print(msg.strip())
