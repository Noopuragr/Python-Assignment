import re
str1=str(input("Enter the number"))
phoneReg= re.compile(r'(\d){3}-(\d){3}-(\d){6}')
mo= phoneReg.search(str1)
print(mo.group())