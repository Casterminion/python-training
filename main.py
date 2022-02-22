'''
name = input("Write your name: ")
age = input("What's your age? ")
print(f'Hello, {name}')
print(f'Your age is {age}')

print('-'*20)
print('Write down two numbers that you would like to sum ')
a = int(input('Type first number = '))
b = int(input('Type second number = '))
def sum(a, b):
	print(f'{a} + {b} = {a + b }')
sum( a , b)
print('-'*20)


#Tito pamoka

a =10
b = int(input ('B: '))


if a>b:
	print('A > B')
else:
	print('A < B')

if a>b:
	print('A > B')
elif a == b:
	print('A < B')
else:
	print('A < B')

	
#If with bools	
c = False

if not c:
	print('C is False')

#If negation
d = True

if  d:
	print('C is True')

#If and

a1 = 2
a2 = True

if a1 < 5 and a2:
	print('Trigger')

# < > == !== >=  <=

b1 = 5
b2 = 10
if b1 > 1 or b2 > 5:
	print('Trigger2')


#naudojimas boolean
# name -str
#autorius -str
#Rented - bool

#-----------------------------------------------


#While loop
i = 0

while i < 10:
	print(i)
	i +=1 # i = i +1     
#Kol yra teisinga tol suksis kodas, kai false baigsis loop      


#For loop

grades = [10 , 8 , 7,  5 , 10] 

sum = 0 
sum += grade
for grade in grades:
	print(grade)

print(sum)

#For loop with range

for i in range (1, 3):
	print(i)
'''
'''
#custom step
for i in range(1 , 10, 2):
	print(i)

#Reverse
for i in range (10, 0, -1):
	print(i)

#list

list = [10 , 8 , 7,  5 , 10] 
list = ['lemp', 'stalas', 'zuvis']

for element in list:
	print(element)

print(list[0])

obj = {
	'name': 'Titas',
	'Age': 20
	'friends': ['none', None, 2]
}
print(obj['friends'])

'''

