##Get second largest integer

example_list = [1, 5, 2, 1, 7, 5, 7, 3]

def get_second_largest_integer(input_list->list):
    try:
        output_list = list(set(input_list))
        return(f'The second largest integer in input_list: {output_list[-2]}' )
    except:
        print('please, input list type in function')

get_second_largest_integer(example_list)

get_second_largest_integer(1,2)

##Create a list for integers

list_demo = ([1, 'Hello', None, 5, 0.15, 1, 5])

def extract_integers(input_list):
    list_integer = []
    try:
        for element in input_list:
          if isinstance(element, int) == True:
                list_integer.append(element)
                continue
        return list_integer  
    except:
        print('please, check logic function again')

extract_integers(list_demo)

##Get top n salaries

salaries = [
    18732.8, 12842.28, 13391.69, 14061.23,
    25509.77, 13636.95, 11841.63, 11519.12,
    16719.45, 25066.37, 12842.28, 25066.37
]


def top_n_salaries(input_list_salary, number_of_show):
    output_list_salary = sorted(input_list_salary, reverse= True)
    return(f'Top {number_of_show} in salary is {output_list_salary[0:number_of_show]}')
    
top_n_salaries(salaries, 3)

top_n_salaries(salaries, 5)