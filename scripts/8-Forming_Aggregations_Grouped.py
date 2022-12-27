#Task 1
path_orders = "/Users/mac/Desktop/Training/Udemy_training/itversity/retail_db/orders/part-00000"

orders_file = open(path_orders).read()

orders_raw = orders_file.splitlines()


def get_orders_status(orders):
    order_status = []
    for order in orders:
        order_status.append(order.split(",")[-1])
    return order_status

'''
{'CANCELED',
 'CLOSED',
 'COMPLETE',
 'ON_HOLD',
 'PAYMENT_REVIEW',
 'PENDING',
 'PENDING_PAYMENT',
 'PROCESSING',
 'SUSPECTED_FRAUD'}
'''

def get_count_by_order_status(orders):
    #order_count_status = []
    orders_status = get_orders_status(orders)
    order_count_status = dict((x, orders_status.count(x)) for x in set(orders_status))
    return order_count_status

#Task 2

path_order_items = "/Users/mac/Desktop/Training/Udemy_training/itversity/retail_db/order_items/part-00000"

order_items_file = open(path_order_items).read()

order_items_raw = order_items_file.splitlines()

# order_items_schema = [
#     "order_item_id",
#     "order_item_order_id",
#     "order_item_product_id",
#     "order_item_quantity",
#     "order_item_subtotal", --revenue
#     "order_item_product_price"
# ]

def get_list_orders_revenue(order_items):
    dict_orders_revenue = {}
    for order in order_items:
        dict_orders_revenue.append([order.split(",")[1], order.split(",")[-1]])
    return dict_orders_revenue

