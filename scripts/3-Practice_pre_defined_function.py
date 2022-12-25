#condition

i = input('Enter the number:')

if i % 2 == 0:
    print('even')
else: 
    print('odd')

######
i = 5
print('even') if i % 2 == 0 else print('odd')

##########


ages = [7, 3, 15, 145, 217, 18]

for age in ages:
    if age <= 6:
        print(f"{age} is New Born or Infant")
    elif age > 6 and age <= 18:
        print(f"{age} is Toddler")
    elif age >= 19 and age < 144:
        print(f'{age} is Grown up')
    elif age >= 145 and age < 216:
        print(f"{age} is youth")
    else:
        print(f'check all again condition')



#running os command
from ipaddress import summarize_address_range
import os

os.getcwd

os.environ.get('HOME')

os.environ.get?

os.environ.get('PASSWORD', 'Passwords should be confidential')

import subprocess

output = subprocess.check_output(['ls','-ltr'])

for rec in output.splitlines():
    print(rec)

# Get sum of integers for a given range.

list_sum = [1, 6, 8, 3, 7, 2, 9]

sum_even_number = 0
sum_divisible = 0
for number in list_sum:
    if number % 2 == 0:
        sum_even_number += number
    if number % 3 == 0:
        sum_divisible += number
print(sum_even_number)
print(sum_divisible)

######


sum_even_number = 0
for number in range(5, 10+1):
    if number % 2 == 0:
        sum_even_number += number
print(sum_even_number)


