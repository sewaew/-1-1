import re

f = open('query1')
fail = f.read()
f.close()
print (fail);
print;
print ("В файле query1 выбрать все строки, в которых имя сотрудника начинается на букву R.");
print;


#найдены сопоставления

f1 = open('text.txt', 'w')
f1.write
f1.close()


f = open('query1')
for line in f:
   match = re.search(r'^.....R.*', line)
   if match:
      print(match.group())
      a = match.group()
      f1 = open('text.txt', 'a')
      f1.write(a + '\n')
      f1.close()
f.close()