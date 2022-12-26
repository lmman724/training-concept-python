import pandas as pd

orders_path = r"C:\Users\lmman\Desktop\Training\Udemy_training\itversity\retail_db\orders\part-00000"

orders_schema = [
    "order_id",
    "orders_date",
    "order_customer_id",
    "status"
]

orders = pd.read_csv(orders_path,header= None,names = orders_schema)

orders.orders_date

orders["orders_date"]


####

sals_ld = [(1, 1500.0), (2, 2000.0, 10.0), (3, 2200.00)]

sals_df = pd.DataFrame(sals_ld, columns= ["id", "sal", "comm"])

sals_ld = [
    {'id': 1, 'sal': 1500.0},
    {'id': 2, 'sal': 2000.0},
    {'id': 3, 'sal': 2200.0}
]

sals_df_list = pd.DataFrame(sals_ld)

# sals_ld_dict = {{'id': 1, 'sal': 1500.0},
#     {'id': 2, 'sal': 2000.0},
#     {'id': 3, 'sal': 2200.0}}

path_orders_items = r"C:\Users\lmman\Desktop\Training\Udemy_training\itversity\retail_db\order_items\part-00000"


order_items_schema = [
    "order_item_id",
    "order_item_order_id",
    "order_item_product_id",
    "order_item_quantity",
    "order_item_subtotal",
    "order_item_product_price"
]

orders_items = pd.read_csv(path_orders_items,
                    header= None, names= order_items_schema)

