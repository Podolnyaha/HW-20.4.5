import  json

with open(r"C:\Users\sasha\PycharmProjects\project1\my_file\orders_july_2023.json", "r", encoding='utf-8') as my_file:
    orders_july = my_file.read()
    orders = json.loads(orders_july)
   # 1. Какой номер самого дорогого заказа за июль
max_price = 0
max_order = ''
# цикл по заказам
for order_num, orders_data in orders.items():
    # получаем стоимость заказа
    price = orders_data['price']
    # если стоимость больше максимальной - запоминаем номер и стоимость заказа
    if price > max_price:
        max_order = order_num
        max_price = price
print(f'Номер заказа с самой большой стоимостью: {max_order}, стоимость заказа: {max_price}')


#2 Какой номер заказа с самым большим количеством товаров?
max_quantity = 0
max_order_number = ''
for order_number, order_details in orders.items():
    if order_details['quantity'] > max_quantity:
        max_quantity = order_details['quantity']
        max_order_number = order_number
print(f'Номер заказа с самым большим количеством товаров: {max_order_number}')


#3 В какой день в июле было сделано больше всего заказов?
date_dict = {}

for order_num, orders_data in orders.items():
    date = orders_data['date']
    date_dict[date] = date_dict.get(date, 0) + 1
max_order = max(date_dict.values())
for date in sorted(date_dict):
    if date_dict[date] == max_order:
        print(f'В день {date} было сделано больше всего заказов: {max_order}')

#4 Какой пользователь сделал самое большое количество заказов за июль?
max_orders = 0
user_dict = {}
for order_num, orders_data in orders.items():
    user_id = orders_data['user_id']
    user_dict[user_id] = user_dict.get(user_id, 0) +1
    orders_2 = user_dict.get(user_id)
if orders_2 > max_orders:
    max_orders = orders_2
    print(f'Пользователь {user_id} делал самое большое количество заказов за июль - {max_orders}')


#5 У какого пользователя самая большая суммарная стоимость заказов за июль?
user_total_spent = {}
for order_num, order_data in orders.items():
        user_id = order_data['user_id']
        price = order_data['price']
if user_id in user_total_spent:
        user_total_spent[user_id] += price
else:
        user_total_spent[user_id] = price
max_spent = 0
max_user_id = {}

for user_id, total_spent in user_total_spent.items():
    if total_spent > max_spent:
        max_spent = total_spent
        max_user_id = user_id

print(f'Пользователь с ID {max_user_id} имеет самую большую суммарную стоимость заказов: {max_spent}')


#6 Какая средняя стоимость заказа была в июле?
total_price = 0
order_count = len(orders)
for order_data in orders.values():
    total_price += order_data['price']
if order_count > 0:
    average_price = total_price / order_count
print(f'Средняя стоимость заказа в июле: {average_price:.2f}')


#7 Какая средняя стоимость товаров в июле?
sum_all, count = 0, 0
for orders, date in orders.items():
    sum_all += date ['price']
    count += date['quantity']
print(f'Средняя стоимость товаров в июле: {sum_all/count:.3}')
