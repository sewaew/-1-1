import re

f = open('query1')
fail = f.read()
f.close()
print (fail);
print;
print ("В файле query1 выбрать все строки, в которых имя сотрудника начинается на букву R.");
print;


#чистим файд text.txt от предыдущих тестов
f1 = open('text.txt', 'w')
f1.write
f1.close()


f = open('query1')							#открываем файл для чтения
for line in f:								#организовавыем масси для чтения файла по строке
   match = re.search(r'^.....R.*', line)	#ищим совпадения по шаблону
   if match:								#если совпадания найдены
      print(match.group())					#печатаем совпадения
      a = match.group()						#переменной а присваем совпадшую строку
      f1 = open('text.txt', 'a')			#открываем файл для записи
      f1.write(a + '\n')					#записываем совпадения в файл
      f1.close()							#закрываем файл
f.close()