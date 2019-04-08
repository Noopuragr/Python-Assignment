import sys
import random
import string
#Max number in list
def max_num_in_list(Lists):
	max=Lists[0]
	for a in Lists:
		if a > max:
			max = a
	return max
Lists1=[10,20,30,40,50,11,15,19]
maxNum=max_num_in_list(Lists1)

#Second largest number in list
def second_largest_num(Lists):
	Lists.sort()
	n=len(Lists)
	num=Lists[n-2]
	return num
second_max_num=second_largest_num(Lists1)

#Even odd number in separate list
def even_odd(lists):
	l1=[]
	l2=[]
	for n in lists:
		if n%2==0:
			l1.append(n)
		else:
			l2.append(n)
	return l1,l2
num1,num2=even_odd(Lists1)

#Check whether two list are same or not
def Checklists():
	l1=[10,20,30]
	l2=[10,20,30]
	if l1==l2:
		return True
Checklists()

#Union of list
l1=[10,20,30]
l2=[11,21,30,31]
def Union(l1,l2):
	lists=list(set(l1).union(l2))
	return sorted(lists)
UnionList=Union(l1,l2)

#Intersection of list
def Intersection(l1,l2):
	result = list(set(l1) & set(l2))
	return result
Intrsctn=Intersection(l1,l2)

#Union and Intersection without repeatition
def UnionIntersectn(l1,l2):
	union = list(set().union(l1,l2))
	result = list(set(l1) & set(l2))
	return union, result
value1,value2=UnionIntersectn(l1,l2)

#List of tuples with first elements as number and second element as square of number
def Tuples(l_range,u_range):
	a=[(x,x*x) for x in range(l_range,u_range+1)]
	return a
l_range=1
u_range=5
list_of_tuples=Tuples(l_range,u_range)

#To remove duplicates fromitems of list
def Duplicate(lists):
	result = list(set(lists))
	return result
List2=[10,10,20,30,20]
dup=Duplicate(List2)

#To read the list of words and return the length of longest one
def LongWrod(str1):
	l1=list(str1.split())
	max=len(l1[0])
	temp=l1[0]
	for ch in l1:
		if len(ch)> max:
			temp=ch
	return temp
string = "Hello! This is manipal"
Length=LongWrod(string)

#To add a key value pair to dictionary
def add_kv(key,value):
	data={}
	data.update({key:value})
	return data
key=1
value='a'
update_dict=add_kv(key,value)
#To concatenate two dictionaries into one
def Concate(d1,d2):
	d1.update(d2)
	return d1
d1 = {1: 'a',2:'b',3:'c'}
d2 = {4:'d',5:'e',3:'c'}
concatenate=Concate(d1,d2)

#To check if given key exists in dictionary or not
def CheckKey(d):
	for i in d.keys():
		if i==1:
			return True
checkey=CheckKey(d1)

#Dictionary that contain values between 1 to n in the form of (x,x*x)
def genDict():
	d={}
	#n=int(input("Enter the range"))
	for x in range(1,6):
		d[x]= x*x
	return(d)
dict1=genDict()

#To sum all the items in the dictionary
def SumItems(d):
	sum_values=sum(d.values())
	return sum_values
dict3={'a':123,'b':234,'c':345}
sum_dict=SumItems(dict3)

#To multiply all the items in the dictionary
def MulItems(d):
	m=1
	for i in d:
		m=m*d[i]
	return m
mul_dict=MulItems(dict3)

#To remove the given key from dictionary
def delKey(d):
	if 'b' in d:
		del d['b']
	return d
new_dict={'a':123,'b':234,'c':345}
delkey=delKey(new_dict)

#function is_empty(my_dict) that takes a dictionary my_dict and sreturns True if my_dict is empty and False otherwise
def is_empty(my_dict):
	n=len(my_dict)
	if n==0:
		return True
dict_1={}
empty=is_empty(dict_1)

#make_dict(key_value_list) that takes a list of tuples key_value_list where each tuple is of the form (key, value) and returns a dictionary
def make_dict(d):
	l=dict(d)
	return l
key_value_list = [('A',1), ('B',2), ('C',3)]
a=make_dict(key_value_list)

#encrypt(phrase,cipher_dict) 
cipher_dict = {'e': 'u', 'b': 's', 'k': 'x', 'u': 'q', 'y': 'c', 'm': 'w', 'o': 'y', 'g': 'f', 'a': 'm', 'x': 'j', 'l': 'n', 's': 'o', 'r': 'g', 'i': 'i', 'j': 'z', 'c': 'k', 'f': 'p', ' ': 'b', 'q': 'r', 'z': 'e', 'p': 'v', 'v': 'l', 'h': 'h', 'd': 'd', 'n': 'a', 't': ' ', 'w': 't'}
phrase = 'dog'
def encrypt(phrase,cipher_dict):
	phrase1=''
	for i in range(0,len(phrase)):
		if phrase[i] in cipher_dict.keys():
			l = phrase[i]
			rep = cipher_dict[l]
			phrase1+=rep
	return phrase1
b=encrypt(phrase,cipher_dict)

#make_cipher_dict(alphabet) 
def make_cipher_dict(char1):
	a=list(char1)
	b=list(char1)
	random.shuffle(b)
	d1={}
	for i in range(0,len(char1)):
		d={a[i]:b[i]}
		d1.update(d)
#s	print("The shuffled word is",d1)
	return len(a)

#	return len(a)
char1='abcdef'
dict_char=make_cipher_dict(char1)

#to generate grade using dictionary
def genGrades():
	
	dict_of_students={'Ash':{'S1':90,'S2':85,'S3':72,'S4':63,'S5':59},'Beth':{'S1':32,'S2':83,'S3':97,'S4':77,'S5':69},'Cal':{'S1':91,'S2':83,'S3':77,'S4':57,'S5':99}}
	list_of_names=list(dict_of_students.keys())
	
	for i in list_of_names:
	#	print("Student:",i)
		one_student_dict=dict_of_students[i]
	#	print(one_student_dict)
		subs=list(one_student_dict.keys())
		for p in subs:
			m=one_student_dict[p]
			if 90<=m<=100:
				one_student_dict[p]="A+"
				#break
			elif 80<=m<=89:
				one_student_dict[p]="A"
				#break
			elif 70<=m<=79:
				one_student_dict[p]="B"
				#break
			elif 60<=m<=69:
				one_student_dict[p]="C"
				#break
			elif 50<=m<=59:
				one_student_dict[p]="D"
				#break
			else:
				one_student_dict[p]="F"

		dict_of_students[i]=one_student_dict

	return dict_of_students
