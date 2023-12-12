# itertools - библиотека для работы с комбинаторикой
import itertools

# product() - функция, получающая все возможные перестановки элементов длины repeat из букв, которые в неё переданы
list_string = itertools.product('БОРИС', repeat=6)

count = 0
for str in list_string:
    # join() - функция соединяющая массив строк в одну строку при помощи разделителя, который указан до точки
    line = ''.join(str)
    # count() - строковая функция, которая определяет кол-во вхождений букв или слов в строку
    if line.count('Б') == 1 and line.count('Р') == 1 and line.count('С') < 2:
        count += 1
print(count)
