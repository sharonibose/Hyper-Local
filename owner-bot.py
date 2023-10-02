import os
from dotenv import load_dotenv
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Load API credentials from .env file
load_dotenv()
TELEGRAM_API_TOKEN = os.getenv('ENTER YOUR TELEBOT API CREDENTIALS')
SHOP_OWNER_CHAT_ID = os.getenv('ENTER YOUR CHAT ID')

bot = telebot.TeleBot(TELEGRAM_API_TOKEN)
shop_owner_chat_id = SHOP_OWNER_CHAT_ID

order_details = {}

def process_order(user_chat_id, order_text):
    order_details[user_chat_id] = order_text
    keyboard = InlineKeyboardMarkup()
    accept_button = InlineKeyboardButton(
        text='Accept', callback_data=f'accept {user_chat_id}')
    decline_button = InlineKeyboardButton(
        text='Decline', callback_data=f'decline {user_chat_id}')
    keyboard.add(accept_button, decline_button)
    bot.send_message(shop_owner_chat_id,
                     f'New order from user {user_chat_id}:\n\n{order_text}')
    bot.send_message(shop_owner_chat_id,
                     'Do you want to accept or decline this order?', reply_markup=keyboard)

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(
        message.chat.id, 'Welcome to the shop. Please enter your order details in the following format:\n\nItem: Quantity\n')

@bot.message_handler(regexp=r'^[a-zA-Z]+:\s*\d+$')
def order_message_handler(message):
    user_chat_id = message.chat.id
    order_text = message.text
    process_order(user_chat_id, order_text)

@bot.callback_query_handler(func=lambda call: True)
def accept_decline_handler(call):
    user_chat_id = call.data.split()[-1]
    decision = call.data.split()[0]
    bot.send_message(
        user_chat_id, f'Your order has been {decision}d by the shop owner')
    del order_details[user_chat_id]
    bot.answer_callback_query(call.id)

# Start the bot
bot.polling()
