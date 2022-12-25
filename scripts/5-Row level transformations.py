path_name = open('/Users/mac/Desktop/Training/Udemy_training/itversity/retail_db/orders/part-00000')

order_file = path_name.read()

order_raw = order_file.splitlines()

def convert_to_tuple(str: str):
    order_tup = tuple(str)
    return order_tup

order_tup = convert_to_tuple(order_raw)

order_tup[0].split(",")[0]

#Get all order ids and associated statuses

def task_1(order_raw: tuple):
    order_task_1 = []
    for i in range(len(order_raw)):
        order_detail = order_raw[i].split(",")[0]+ ", " +order_raw[i].split(",")[-1]
        order_task_1.append(order_detail)
    return order_task_1

task_1(order_tup)

# def get_task_1(str:str):
#     order_statuses = []
#     for order in str:
#         order_statuses.append(','.join([order.split(',')[0], order.split(',')[3]]))


#########

#{'order_id': 1, 'order_date': '2020-12-22', 'order_status': 'COMPLETE'}

order_raw[0].split(",")[-1]

def get_dict_item (str_input:str):
    order_dict = {}
    order_dict_full  = []
    for i in range(len(str_input)):
        order_id = str_input[i].split(",")[0]
        order_date = str_input[i].split(",")[1]
        order_status = str_input[i].split(",")[-1]
        order_dict = {'order_id': order_id,'order_date': order_date, 'order_status': order_status }
        order_dict_full.append(order_dict)
    return order_dict_full

get_dict_item(order_raw)



    

    

