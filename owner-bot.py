import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot('ENTER YOUR TELEBOT API CREDENTIALS')
shop_owner_chat_id = 'ENTER YOUR CHAT ID'

# Defining the dictionary to store the order details
order_details = {}

# Defining the handler function for the /start command


@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(
        message.chat.id, 'Welcome to the shop. Please enter your order details in the following format:\n\nItem: Quantity\n')

# Defining the handler function for receiving the order details


@bot.message_handler(func=lambda message: True)
def order_handler(message):
    # Getting the user's chat ID
    user_chat_id = message.chat.id
    # Saving the order details in the dictionary
    order_details[user_chat_id] = message.text
    # Sending the order details to the shop owner
    bot.send_message(shop_owner_chat_id,
                     f'New order from user {user_chat_id}:\n\n{message.text}')
    # Creating the inline keyboard with accept and decline buttons
    keyboard = InlineKeyboardMarkup()
    accept_button = InlineKeyboardButton(
        text='Accept', callback_data=f'accept {user_chat_id}')
    decline_button = InlineKeyboardButton(
        text='Decline', callback_data=f'decline {user_chat_id}')
    keyboard.add(accept_button, decline_button)
    # Asking the shop owner to accept or decline the order
    bot.send_message(shop_owner_chat_id,
                     'Do you want to accept or decline this order?', reply_markup=keyboard)

# Defining the handler function for the accept and decline buttons


@bot.callback_query_handler(func=lambda call: True)
def accept_decline_handler(call):
    # Getting the user's chat ID and the decision
    user_chat_id = call.data.split()[-1]
    decision = call.data.split()[0]
    # Sending the decision to the user
    bot.send_message(
        user_chat_id, f'Your order has been {decision}d by the shop owner')
    # Deleting the order details from the dictionary
    del order_details[user_chat_id]
    # Answering the callback query to remove the inline keyboard
    bot.answer_callback_query(call.id)


# Starting the bot
bot.polling()
