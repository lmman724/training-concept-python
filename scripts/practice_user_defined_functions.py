import datetime as dt
#from time import strftime

dt.datetime.now()

dt.datetime.today().strftime('%Y-%m-%d')

dt.datetime.today().strftime('%d-%m-%Y')

int(dt.datetime.today().strftime('%Y%m%d'))

print(__name__)

#######

list_string = ('ITVersity','level','RaceCar')

for str in list_string:
    if str == reversed(str):
        print(f'{str} is palindromes words')
    else:
        print(f'{str} is not palindromes words ')

########
#'sun - 23'

import calendar

some_day_str = '2020/10/18'

some_day_date = dt.datetime.strptime(some_day_str,'%Y/%m/%d')

get_day = str(some_day_date.day)

get_weekday = dt.datetime.weekday(some_day_date)

date_name = calendar.day_name[get_weekday][:3]

combine_time = get_day + '-'+ date_name

print(combine_time)

########

student = 'student_id=1;student_name=Some X;join_date=2020-10-02'

student_split = student.split(';')



student_name = student_split[1].split('=')[1]

join_date = student_split[2].split('=')[1]

join_date_dt = dt.datetime.strptime(join_date,'%Y-%m-%d')


join_date_dt_convert = dt.datetime.strftime(join_date_dt, '%Y-%b-%d')


##### varying arguments

#####keyword arguments

def add_employee(employee_id, **degrees):
    print(f'length: {len(degrees)}')
    print(f'Type: {type(degrees)}')
    print(degrees)


def add_employee_1(employee_id, *degrees):
    print(f'length: {len(degrees)}')
    print(f'Type: {type(degrees)}')
    print(degrees)

add_employee(1, bachelors='B. Sc', masters='M. C. A')
add_employee_1(1, 'B. Sc','M. C. A')


#####

def check_salary(salary = 3000):
    invalid_salary_flag = False
    if salary < 3000:
        invalid_salary_flag = False
        print(f'Invalid salary: {salary}, salary should be at least 3000')

check_salary()
    
def get_invalid_phone_count(employee_id,*phone_numbers):
    valid_phone_count = 0
    invalid_phone_count = 0
    if phone_numbers == 10:
        valid_phone_count += 1
        print(f'{employee_id} have {valid_phone_count}')
    else:
        invalid_phone_count += 1
        print(f'{employee_id} have {invalid_phone_count} phone numbers out of {len(phone_numbers)} are not valid')

get_invalid_phone_count('Man','0368800977, 0976800977' )

##bachelors, masters, executive, doctorate

def check_invalid_degrees(*degrees):
    list_degrees = {'bachelors', 'masters', 'executive', 'doctorate'}
    invalid_degree_flag = False
    for degrees in list_degrees:
        if degrees not in list_degrees:
            invalid_degree_flag = True
            print('One or more degrees are not valid')

check_invalid_degrees('masters')


#@#####
def add_employee(employee_id, salary = 3000, *phone_numbers, **degrees):
    check_salary(salary)
    get_invalid_phone_count(employee_id, phone_numbers)
    check_invalid_degrees()
    #if invalid_degree_flag == True and invalid_phone_count == True:
    print(f'Employee {employee_id} with {degrees} of degrees is successfully added and his salary is {salary}')
add_employee(1,3000,'1234567890', '1234567890', bachelors='B. Sc', masters='M. C. A')


#####
# Sum of Integers from 1 to n

def sum_n(n):
    sum_range = 0
    try:
        for number in range(1, n+1):
            sum_range += number
        return(f'sum of integers within a range of 1 to {n} is {sum_range}', )
    except:
        print(f'{n} is not a valid integer')  
sum_n(7)
sum_n('7')

#######

def sum_of_integers(lb, ub):
    try:
        sum_number = 0
        if lb > ub:
                print(f'{lb} is not lower than {ub}')
        for number in range(lb,ub):
            sum_number += number
        return(f'sum numbers of range {lb} to {ub} is {sum_number}')
    except:
        print(f'Either {lb} or {ub} are not integers')

sum_of_integers(1,10)
sum_of_integers(1,'10')
sum_of_integers(10,1)