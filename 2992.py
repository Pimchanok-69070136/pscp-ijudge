'''
Helo

'''

num = input()
sign = input()

num1 = int(num)
num2 = int(num[1]+num[0])
if sign == "+":
    print(f'{num1} + {num2} = {num1+num2}')
else:
    print(f'{num1} * {num2} = {num1*num2}')
