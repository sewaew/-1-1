import re

f = open("query3","r")
fail = f.readlines()
f.close()

for i in fail:
    print (i)

print ("\nВ файле query3 выбрать все строки, в которых в названии есть слово 'TENNIS', а цена установлена в 1990 г.\n");


li=[]
for line in fail:
   match = re.search(r'^.*TENNIS.*90', line)
   if match:
      print (match.group())
      li += [match.group()]



result = open ("result2.txt","w")
for i in li:
	result.write(i+"\n")
result.close()