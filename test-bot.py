import telebot
from telebot import types

import datetime

bot = telebot.TeleBot('ENTER YOUR TELEBOT API CREDENTIALS')

# Declaring the cart dictionary
cart = {}

# Defining the inventory items
inventory_items = {
    'Gobbles Bar Cake': {
        'price': 10,
        'quantity': 40,
        'type': 'Cake',
        'weight': '30g',
        'brand': 'Britannia',
        'manufacture_date': '2023-01-01',
        'expiry_date': '2024-01-31'
    },
    'Bounce Orange Creme Biscotti': {
        'price': 10,
        'quantity': 40,
        'type': 'Biscuit',
        'weight': '64g',
        'brand': 'Sunfeast',
        'manufacture_date': '2023-01-01',
        'expiry_date': '2024-01-31'
    },

    'Good Day Cashew Cookies': {
        'price': 10,
        'quantity': 50,
        'type': 'Biscuit',
        'weight': '52.5g',
        'brand': 'Britannia',
        'manufacture_date': '2023-02-01',
        'expiry_date': '2024-02-28'
    },
    'Maaza Juice Mango Refresh': {
        'price': 10,
        'quantity': 50,
        'type': 'Juice',
        'weight': '150ml',
        'brand': 'Maaza',
        'manufacture_date': '2023-02-01',
        'expiry_date': '2024-02-28'
    },
    'Slice Soft Drink - Mango': {
        'price': 40,
        'quantity': 50,
        'type': 'Juice',
        'weight': '500ml',
        'brand': 'Slice',
        'manufacture_date': '2023-02-01',
        'expiry_date': '2024-02-28'
    },
    'Tedhe Medhe': {
        'price': 10,
        'quantity': 50,
        'type': 'Snacks',
        'weight': '40g',
        'brand': 'Bingo',
        'manufacture_date': '2023-02-01',
        'expiry_date': '2024-02-28'
    },
    'Maggi': {
        'price': 14,
        'quantity': 50,
        'type': 'Noodles',
        'weight': '70g',
        'brand': 'Nestle',
        'manufacture_date': '2023-02-01',
        'expiry_date': '2024-02-28'
    },
    'Colgate Toothpaste': {
        'price': 66,
        'quantity': 50,
        'type': 'Toothpaste',
        'weight': '100g',
        'brand': 'Colgate',
        'manufacture_date': '2023-02-01',
        'expiry_date': '2024-02-28'
    },
    'Dettol Antiseptic Liquid ': {
        'price': 37,
        'quantity': 50,
        'type': 'Antiseptic Liquid',
        'weight': '60ml',
        'brand': 'Dettol',
        'manufacture_date': '2023-02-01',
        'expiry_date': '2024-02-28'
    },
    'Surf Excel Easy Wash Detergent Powder': {
        'price': 75,
        'quantity': 50,
        'type': 'Detergent',
        'weight': '500g',
        'brand': 'Surf Excel',
        'manufacture_date': '2023-02-01',
        'expiry_date': '2024-02-28'
    },
    'Mysore Sandal Soap': {
        'price': 42,
        'quantity': 50,
        'type': 'Soap',
        'weight': '75g',
        'brand': 'Mysore',
        'manufacture_date': '2023-02-01',
        'expiry_date': '2024-02-28'
    },
    'Dairy Milk': {
        'price': 10,
        'quantity': 50,
        'type': 'Chocolate',
        'weight': '13.2g',
        'brand': 'Cadbury',
        'manufacture_date': '2023-02-01',
        'expiry_date': '2024-02-28'
    },
    'Desi Popz': {
        'price': 5,
        'quantity': 50,
        'type': 'Candy',
        'weight': '9g',
        'brand': 'GO DESI',
        'manufacture_date': '2023-02-01',
        'expiry_date': '2024-02-28'
    },
    'Kit Kat': {
        'price': 20,
        'quantity': 50,
        'type': 'Coated Wafer',
        'weight': '18.5g',
        'brand': 'Nestle',
        'manufacture_date': '2023-02-01',
        'expiry_date': '2024-02-28'
    },
    'Maggi Cup Noodles': {
        'price': 50,
        'quantity': 50,
        'type': 'Cup Noodle',
        'weight': '70g',
        'brand': 'Nestle',
        'manufacture_date': '2023-02-01',
        'expiry_date': '2022-02-28'
    },
    'Mini Chocobar': {
        'price': 20,
        'quantity': 50,
        'type': 'Ice Cream',
        'weight': '40ml',
        'brand': 'Arun',
        'manufacture_date': '2023-02-01',
        'expiry_date': '2024-02-28'
    }
}

# Defining the handler for the "/start" command


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton(
        'Store Hours', callback_data='store_hours'))
    markup.add(types.InlineKeyboardButton(
        'Best Time to Visit', callback_data='best_time_to_visit'))
    markup.add(types.InlineKeyboardButton(
        'Shop Details', callback_data='shop_details'))
    markup.add(types.InlineKeyboardButton(
        'View Inventory Items', callback_data='view_inventory'))
    bot.reply_to(message, 'Welcome to Sunrise Superstore!',
                 reply_markup=markup)

# Defining the handler for the "Store Hours" button


@bot.callback_query_handler(func=lambda call: call.data == 'store_hours')
def store_hours(call):
    message_text = 'Our store is open from 6 AM to 10 PM, Monday to Sunday. We are open all days.'
    bot.answer_callback_query(callback_query_id=call.id)
    bot.send_message(call.message.chat.id, message_text)

# Defining the handler for the "Best Time to Visit" button


@bot.callback_query_handler(func=lambda call: call.data == 'best_time_to_visit')
def best_time_to_visit(call):
    message_text = 'Best times to visit the store:\n\''
    message_text = 'Least Busy: 🟢\nLess Busy: 🟡\nBusy: 🔴\nVery Busy: ⚫\n\n'
    # Defining a dictionary to map busyness levels to emojis
    busyness_emoji = {
        'Least Busy': '🟢',
        'Less Busy': '🟡',
        'Busy': '🔴',
        'Very Busy': '⚫'
    }
    # Defining the data stats
    data = [
        ['Day', '6AM-10AM', '10AM-4PM', '4PM-10PM'],
        ['Monday', 'Less Busy', 'Least Busy', 'Busy'],
        ['Tuesday', 'Less Busy', 'Least Busy', 'Busy'],
        ['Wednesday', 'Less Busy', 'Least Busy', 'Busy'],
        ['Thursday', 'Less Busy', 'Least Busy', 'Busy'],
        ['Friday', 'Less Busy', 'Least Busy', 'Busy'],
        ['Saturday', 'Less Busy', 'Busy', 'Very Busy'],
        ['Sunday', 'Busy', 'Busy', 'Very Busy']
    ]
    # Determining the width of each column
    col_width = [max(len(str(row[i])) for row in data)
                 for i in range(len(data[0]))]
    for i, row in enumerate(data):
        message_text += f"{str(row[0]).ljust(col_width[0] + 2)}"
        # Skipping the first row
        if i != 0:
            for j, col in enumerate(row[1:]):
                message_text += f"{busyness_emoji[col].ljust(col_width[j+1] + 2)}"
        else:
            for j, col in enumerate(row[1:]):
                # Printing the first row
                message_text += f"{str(col).ljust(col_width[j+1] + 2)}"
        message_text += '\n'
    bot.answer_callback_query(callback_query_id=call.id)
    bot.send_message(call.message.chat.id, message_text)

# Defining the handler for the "Shop Details" button


@bot.callback_query_handler(func=lambda call: call.data == 'shop_details')
def store_hours(call):
    message_text = 'Name: Sunrise Supermarket\nPhone: +91-1234567890\nAddress: Bhubaneswar, India'
    bot.answer_callback_query(callback_query_id=call.id)
    bot.send_message(call.message.chat.id, message_text)

# Defining the handler for the "View Inventory Items" button


@bot.callback_query_handler(func=lambda call: call.data == 'view_inventory')
def send_inventory_items(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    for item in inventory_items:
        button = types.InlineKeyboardButton(item, callback_data=item)
        markup.add(button)
    cart_button = types.InlineKeyboardButton(
        'View Cart', callback_data='view_cart')
    markup.add(cart_button)
    bot.answer_callback_query(callback_query_id=call.id)
    bot.send_message(call.message.chat.id,
                     'Please select an item:', reply_markup=markup)

# Defining the handler for the inventory item selection


@bot.callback_query_handler(func=lambda call: call.data in inventory_items)
def show_item_details(call):
    item = call.data
    details = inventory_items[item]
    message_text = f"Item: {item}\nPrice: ₹{details['price']}\nQuantity: {details['quantity']}\nType: {details['type']}\nWeight: {details['weight']}\nBrand: {details['brand']}\nManufacture Date: {details['manufacture_date']}\nExpiry Date: {details['expiry_date']}"
    markup = types.InlineKeyboardMarkup(row_width=2)
    add_to_cart_button = types.InlineKeyboardButton(
        'Add to Cart', callback_data=f"add_to_cart_{item}")
    markup.add(add_to_cart_button)
    back_button = types.InlineKeyboardButton(
        'Back to Inventory', callback_data='back_to_inventory')
    markup.add(back_button)
    view_cart_button = types.InlineKeyboardButton(
        'View Cart', callback_data='view_cart')
    markup.add(view_cart_button)
    bot.answer_callback_query(callback_query_id=call.id)
    bot.send_message(call.message.chat.id, message_text, reply_markup=markup)

# Defining the handler for the "Add to Cart" button


@bot.callback_query_handler(func=lambda call: call.data.startswith('add_to_cart_'))
def add_to_cart_(call):
    item = call.data.split('_')[3]
    user_id = call.from_user.id
    if user_id not in cart:
        cart[user_id] = {}
    if item not in cart[user_id]:
        cart[user_id][item] = 0
    cart[user_id][item] += 1
    bot.answer_callback_query(
        callback_query_id=call.id, text='Item added to cart!')

# Defining the handler for the "Back to Inventory" button


@bot.callback_query_handler(func=lambda call: call.data == 'back_to_inventory')
def back_to_inventory(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    for item in inventory_items:
        button = types.InlineKeyboardButton(item, callback_data=item)
        markup.add(button)
    view_cart_button = types.InlineKeyboardButton(
        'View Cart', callback_data='view_cart')
    markup.add(view_cart_button)
    bot.answer_callback_query(callback_query_id=call.id)
    bot.send_message(call.message.chat.id,
                     'Please select an item:', reply_markup=markup)

# Defining the handler for the "View Cart" button


@bot.callback_query_handler(func=lambda call: call.data == 'view_cart')
def view_cart(call):
    user_id = call.from_user.id
    if user_id not in cart:
        bot.answer_callback_query(
            callback_query_id=call.id, text='Your cart is empty!')
        return
    cart_items = []
    total_price = 0
    for item in cart[user_id]:
        quantity = cart[user_id][item]
        price = inventory_items[item]['price']
        item_price = price * quantity
        cart_items.append(f"{item} ({quantity} x ₹{price}): ₹{item_price}")
        total_price += item_price
    message_text = '\n'.join(cart_items)
    message_text += f"\n\nTotal price: ₹{total_price}"
    markup = types.InlineKeyboardMarkup(row_width=1)
    back_button = types.InlineKeyboardButton(
        'Back to Inventory', callback_data='back_to_inventory')
    markup.add(back_button)
    # Passing the total price as callback data
    checkout_button = types.InlineKeyboardButton(
        'Checkout', callback_data=f"checkout,{total_price}")
    markup.add(checkout_button)
    bot.answer_callback_query(callback_query_id=call.id)
    bot.send_message(call.message.chat.id, message_text, reply_markup=markup)

# Defining the handler for the "Checkout" button


@bot.callback_query_handler(func=lambda call: call.data.startswith('checkout'))
def checkout(call):
    user_id = call.from_user.id
    if user_id not in cart:
        bot.answer_callback_query(
            callback_query_id=call.id, text='Your cart is empty!')
        return
    # Getting the total price from the callback data
    total_price = float(call.data.split(',')[1])
    message_text = f"Your total price is ₹{total_price}. Thank you for shopping with us."
    # Decrementing the quantities from the inventory
    for item_id, quantity in cart[user_id].items():
        inventory_items[item_id]['quantity'] -= quantity
    cart[user_id] = {}
    # Providing the user with "ETA" and "Feedback" buttons
    eta_button = types.InlineKeyboardButton(
        'Estimated Time of Arrival', callback_data='eta')
    feedback_button = types.InlineKeyboardButton(
        'Feedback', url='https://forms.gle/WnPP4BvNXKs12Tkc9')
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(eta_button, feedback_button)
    bot.send_message(call.message.chat.id, message_text, reply_markup=markup)
    bot.answer_callback_query(callback_query_id=call.id)

# Defining the handler for the "ETA" button


@bot.callback_query_handler(func=lambda call: call.data.startswith('eta'))
def eta(call):
    user_id = call.from_user.id
    if user_id not in cart:
        bot.answer_callback_query(
            callback_query_id=call.id, text='Your cart is empty!')
        return
    # Calculating the estimated time of delivery as 45 minutes from the current time
    eta_time = datetime.datetime.now() + datetime.timedelta(minutes=45)
    message_text = f"Your products will be delivered in approximately 45 minutes, by {eta_time.strftime('%I:%M %p')}. Thank you for shopping with us."
    bot.answer_callback_query(callback_query_id=call.id)
    bot.send_message(call.message.chat.id, message_text)

# Defining a function to send the order details to the shop owner


def send_cart_to_owner(cart_items, total_price):
    owner_chat_id = '123456789'
    message_text = 'New order:\n\n'
    message_text += '\n'.join(cart_items)
    message_text += f"\n\nTotal price: ₹{total_price}"
    markup = types.InlineKeyboardMarkup(row_width=2)
    confirm_button = types.InlineKeyboardButton(
        'Confirm', callback_data='confirm_order')
    decline_button = types.InlineKeyboardButton(
        'Decline', callback_data='decline_order')
    markup.add(confirm_button, decline_button)
    bot.send_message(owner_chat_id, message_text, reply_markup=markup)

# Defining the handler for the "Confirm" and "Decline" buttons


@bot.callback_query_handler(func=lambda call: call.data.startswith(('confirm_order', 'decline_order')))
def handle_confirmation(call):
    message_text = ''
    if call.data == 'confirm_order':
        message_text = 'Order confirmed by seller'
    elif call.data == 'decline_order':
        message_text = 'Order declined by seller'
    bot.answer_callback_query(callback_query_id=call.id)
    bot.send_message(call.message.chat.id, message_text)


# Starting the bot
bot.polling()
