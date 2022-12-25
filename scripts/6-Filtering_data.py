import pandas as pd


path = r"C:\Users\lmman\Desktop\Training\Udemy_training\itversity\retail_db\orders\part-00000"

path_retail_orders = open(path)

orders_file = path_retail_orders.read()
orders_raw = orders_file.splitlines()

#orders_raw[0:3]

def get_customer_orders(customer_id, order_raw):
    orders_filter = []
    for order in orders_raw:
        if int(order.split(',')[2]) == customer_id:
            orders_filter.append(order)
    return orders_filter
    
# int(order_raw.split(',')[2]) == 12111 

#task_1
get_customer_orders(12431, orders_raw)

#task_2
import datetime
from datetime import datetime as dt

orders_raw[0].split(',')[1].startswith('2013-07') 

#'2013-07-25 00:00:00.0'

# datetime_object = datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')

# dt.strptime(orders_date,"%Y-%m-%d %H:%M:%S.%f")

# dt.strftime(datetime_object,"%Y-%m")

def get_customer_orders_for_month(orders,month_orders, order_id):
    order_month_filter = []
    for order in orders:
        if order.split(',')[1].startswith(month_orders) and int(order.split(',')[2]) == order_id :
            order_month_filter.append(order)
    return order_month_filter

get_customer_orders_for_month(orders_raw,"2014-01", 12431)


# Task 3

def get_customer_orders_status(orders, customer_id,month_orders):
    orders_status_filter = []
    orders = get_customer_orders_for_month(orders_raw,month_orders, customer_id)
    for order in orders:
        
        if order.split(',')[-1]  == "PENDING_PAYMENT" or order.split(',')[-1] == "PROCESSING":
            orders_status_filter.append(order)

    return orders_status_filter

get_customer_orders_status(orders_raw, 12431, "2014-01")




