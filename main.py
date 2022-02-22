
name = input("Write your name: ")
age = input("What's your age? ")
print(f'Hello, {name}')
print(f'Your age is {age}')

print('-'*20)
print('Write down two numbers that you would like to sum ')
a = int(input('Type first number = '))
b = int(input('Type second number = '))
def sum(a, b):
	print(f'{a} + {b} = {a + b}')
sum(a , b)