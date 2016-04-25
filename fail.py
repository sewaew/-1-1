import re

f = open("query1","r")
fail = f.readlines()
f.close()

for i in fail:
    print (i)

print ("\nВ файле query1 выбрать все строки, в которых имя сотрудника начинается на букву R.\n");


li=[]
for line in fail:
   match = re.search(r'^.....R.*', line)
   if match:
      print (match.group())
      li += [match.group()]



result = open ("result.txt","w")
for i in li:
	result.write(i+"\n")
result.close()