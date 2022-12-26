import pandas as pd


path = "/Users/mac/Desktop/Training/Udemy_training/itversity/retail_db/orders/part-00000"

path_retail_orders = open(path)

orders_file = path_retail_orders.read()
orders_raw = orders_file.splitlines()

orders_raw[0:10]


def total_number_record_month(orders, time_records):
    orders_month_filter = []
    for order in orders:
        if order.split(",")[1].replace("-","").startswith(time_records):
            orders_month_filter.append(order)
    return len(orders_month_filter)

total_number_record_month(orders_raw,"201401")


#task 2

path_order_details = open("/Users/mac/Desktop/Training/Udemy_training/itversity/retail_db/order_items/part-00000")

# order_items_schema = [
#     "order_item_id",
#     "order_item_order_id",
#     "order_item_product_id",
#     "order_item_quantity",
#     "order_item_subtotal", --revenue
#     "order_item_product_price"
# ]

order_item_product_id = 

order_details_file = path_order_details.read()

order_details_raw = order_details_file.splitlines()

#order_item_product_id

order_details_raw[0].split(",")[2]

def product_id_filter(order_items, order_item_product_id):
    product_id_filter = []
    for order_item in order_items:
        if order_item.split(",")[2] == order_item_product_id:
            product_id_filter.append(order_item)
    return product_id_filter

def total_revenue_product_id(order_items,order_item_product_id):
    data = product_id_filter(order_items,order_item_product_id)
    total_revenue = []
    for product_id in data:
        total_revenue.append(float(product_id.split(",")[-2]))
    return round(sum(total_revenue),2)

# data = product_id_filter(order_details_raw,"957")

# data_1 = total_revenue_product_id(order_details_raw,"502")

# task 3

def product_id_filter(order_items, order_item_product_id):
    product_id_filter = []
    for order_item in order_items:
        if order_item.split(",")[2] == order_item_product_id:
            product_id_filter.append(order_item)
    return product_id_filter

def get_product_metric(order_items,order_item_product_id):
    data = product_id_filter(order_items,order_item_product_id)
    total_revenue = []
    product_sold = []
    for product_id in data:
        total_revenue.append(float(product_id.split(",")[-2]))
        product_sold.append(int(product_id.split(",")[3]))
        sum_revenue_product = round(sum(total_revenue),2)
        number_product_sold = sum(product_sold)
    return (number_product_sold,sum_revenue_product)


data_1 = get_product_metric(order_details_raw,"502")


#   Task 4


transactions = [(376.0, 8),
(548.23, 14),
(107.93, 8),
(838.22, 14),
(846.85, 21),
(234.84,),
(850.2, 21),
(992.2, 21),
(267.01,),
(958.91, 21),
(412.59,),
(283.14,),
(350.01, 14),
(226.95,),
(132.7, 14)]

# sale = transactions[0]
#commission_amount = round(sale[0] * (sale[1] / 100), 2)