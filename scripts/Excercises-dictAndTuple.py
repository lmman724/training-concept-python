path = '/Users/mac/Desktop/Training/Udemy_training/itversity/retail_db/orders/part-00000'

order_file = open(path)

type(order_file)

order_raw = order_file.read()

order = order_raw.splitlines()

def covert_to_tuple(str: str):
    return tuple(str)

order_tup = covert_to_tuple(order)

order_tup[0].split(',')[1]


#### Covert string to dict

def covert_list_to_dict(str:str):
    order_split_list = covert_to_tuple(str)
    get_order_dict = {
        'order_id': order_split_list[0],
        'order_date': order_split_list[1],
        'order_customer_id': order_split_list[2],
        'order_status': order_split_list[3]
    }
    return get_order_dict

order_dict = covert_list_to_dict(order)

order_

