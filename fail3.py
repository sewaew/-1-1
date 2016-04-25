import re

f = open("query4","r")
fail = f.readlines()
f.close()

for i in fail:
    print (i)

print ("\nВ файле query4 выбрать все строки, в которых фамилия продавца - 'DUNCAN'.\n");


li=[]
for line in fail:
   match = re.search(r'^.{4}DUNCAN.*', line)
   if match:
      print (match.group())
      li += [match.group()]



result = open ("result3.txt","w")
for i in li:
	result.write(i+"\n")
result.close()