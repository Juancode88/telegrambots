import telebot
from telebot import types
import requests

# Constants
TOKEN = '7045631485:AAFu7i3dvEgXk3LKlO6LPH3vzKD83OmV1hg'
API_KEY = 'YOUR_API_KEY'

# Bot Initialization
bot = telebot.TeleBot(TOKEN)

# Command Lists
COMMANDS = ['/start', '/register', '/location', '/data', '/service', '/store']
BTN_LIST_SERVICE = ['/store', '/software_project', '/speaker_section', '/advertising_campaign']
BTN_LIST_STORE = ['/singlets', '/caps', '/mugs', '/aiart']
BTN_LIST_OTHERS = ['/merchandise', '/merchandise2', '/merchandise3', '/merchandise4', '/newcustomer','/register_topic']

# Function to validate the message
@bot.message_handler(func=lambda message: message.text not in COMMANDS + BTN_LIST_SERVICE + BTN_LIST_STORE + BTN_LIST_OTHERS)
def handle_invalid_command(message):
    bot.send_message(message.chat.id, "Welcome! To start interacting with me, please type /start")

# Start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Hi, I am the virtual assistant of Juancode.')
    
    markup = types.InlineKeyboardMarkup(row_width=2)
    buttons = [
        types.InlineKeyboardButton('Instagram', callback_data='choice_instagram'),
        types.InlineKeyboardButton('Tiktok', callback_data='choice_tiktok'),
        types.InlineKeyboardButton('Youtube', callback_data='choice_youtube'),
        types.InlineKeyboardButton('Stackoverflow', callback_data='choice_stackoverflow')
    ]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Where do you know me from?", reply_markup=markup)

# Handling callbacks
@bot.callback_query_handler(func=lambda call: call.data)
def handle_callback_query(call):
    responses = {
        'choice_instagram': 'Ok follower, how can I assist you? Continue by typing /register.',
        'choice_tiktok': 'Ok follower, how can I assist you? Continue by typing /register.',
        'choice_youtube': 'Ok subscriber, how can I assist you? Continue by typing /register.',
        'choice_stackoverflow': 'Ok friend, how can I assist you? Continue by typing /register.'
    }
    
    response = responses.get(call.data)
    if response:
        bot.send_message(call.message.chat.id, response)

# Register command
@bot.message_handler(commands=['register'])
def register_user(message):
    bot.send_message(message.chat.id, 'What is your name?')
    bot.register_next_step_handler(message, process_user_name)

def process_user_name(message):
    user_name = message.text
    bot.reply_to(message, f'Ok {user_name}, nice to meet you! Continue by typing /data.')

# Data command
@bot.message_handler(commands=['data'])
def request_data(message):
    bot.send_message(message.chat.id, 'Press the button to send the information; your data is protected.')
    location_button = types.KeyboardButton('Where are you?', request_location=True)
    location_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    location_markup.add(location_button)
    bot.send_message(message.chat.id, 'Tell me something about yourself:', reply_markup=location_markup)
    bot.send_message(message.chat.id, 'Continue by typing /service.')

# Service command
@bot.message_handler(commands=['service'])
def choose_service(message):
    bot.reply_to(message, 'These are the services offered by Juancode:')
    
    service_buttons = [
        types.KeyboardButton('/store'),
        types.KeyboardButton('/software_project'),
        types.KeyboardButton('/speaker_section'),
        types.KeyboardButton('/advertising_campaign')
    ]
    service_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    service_markup.add(*service_buttons)
    bot.send_message(message.chat.id, "Choose a service:", reply_markup=service_markup)

# Store command
@bot.message_handler(commands=['store'])
def show_store_menu(message):
    bot.reply_to(message, 'These are the products offered in our store:')
    
    store_buttons = [
        types.KeyboardButton('/singlets'),
        types.KeyboardButton('/caps'),
        types.KeyboardButton('/mugs'),
        types.KeyboardButton('/aiart')
    ]
    store_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    store_markup.add(*store_buttons)
    bot.send_message(message.chat.id, "Choose a product:", reply_markup=store_markup)

# Singlets command
@bot.message_handler(commands=['singlets'])
def ask_tshirt_size(message):
    bot.send_message(message.chat.id, 'What is your t-shirt size?')
    bot.register_next_step_handler(message, process_tshirt_size)

def process_tshirt_size(message):
    user_size = message.text
    bot.reply_to(message, f'In your size: {user_size}, we have the following choices:')
    
    merchandise_button = types.KeyboardButton('/merchandise')
    merchandise_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    merchandise_markup.add(merchandise_button)
    bot.send_message(message.chat.id, 'Press the button', reply_markup=merchandise_markup)

# Merchandise command
@bot.message_handler(commands=['merchandise'])
def show_merchandise(message):
    img_url_1= 'https://static.vecteezy.com/system/resources/previews/014/397/507/original/coding-love-computer-programming-and-programmer-typography-coder-t-shirt-design-vector.jpg'
    bot.send_photo(chat_id=message.chat.id, photo=img_url_1, caption='Season: I love programming')

# Caps command
@bot.message_handler(commands=['caps'])
def ask_cap_style(message):
    bot.send_message(message.chat.id, 'What is your cap style? Press the command: /merchandise2')

# Merchandise2 command
@bot.message_handler(commands=['merchandise2'])
def show_caps(message):
    img_url_2= 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSeGtLvPukCF2z-9ruBGJgfK1ufoqI63244lw&s'
    bot.send_photo(chat_id=message.chat.id, photo=img_url_2, caption='Season: Free caps style')

# Mugs command
@bot.message_handler(commands=['mugs'])
def ask_for_mugs(message):
    bot.send_message(message.chat.id, 'Looking for mugs? Check out our best designs by pressing the command: /merchandise3')

# Merchandise3 command
@bot.message_handler(commands=['merchandise3'])
def show_mugs(message):
    img_url_3= 'https://publicitarcomco.b-cdn.net/wp-content/uploads/2023/02/MUG-BLANCO-COLOR-INTERNO-11OZ.jpg'
    bot.send_photo(chat_id=message.chat.id, photo=img_url_3, caption='Season: White is the mode')

# AI Art command
@bot.message_handler(commands=['aiart'])
def show_ai_art(message):
    bot.send_message(message.chat.id, 'Are you interested in AI art? You can view our best designs by pressing the command: /merchandise4')

# Merchandise4 command
@bot.message_handler(commands=['merchandise4'])
def show_ai_art_2(message):
    img_url_4= 'https://media.licdn.com/dms/image/C5622AQHuLakjUABRsw/feedshare-shrink_800/0/1654630064389?e=2147483647&v=beta&t=gr5FEeFWZzc3bd3Mrjp5vggRPv0lk2l7dhrL9ZV7Qdo'
    bot.send_photo(chat_id=message.chat.id, photo=img_url_4, caption='Season: Art in the cities')

# Software Project command
@bot.message_handler(commands=['software_project'])
def handle_software_project(message):
    bot.send_message(message.chat.id, 'Welcome to the coworking room. Juancode and his team are ready to assist with your project.')
    bot.send_message(message.chat.id, 'First time with our team? Press the command: /newcustomer')
    bot.send_message(message.chat.id, 'If you already have a product with us, you can place your request through the bot: servicecommunity88')
#btn - request contact
contact_button = types.KeyboardButton('What is your cellphone number?', request_contact=True)
contact_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
contact_markup.add(contact_button)
# New Customer command
@bot.message_handler(commands=['newcustomer'])
def new_customer_service(message):
    bot.send_message(message.chat.id, 'Welcome to the new customer service line.')
    bot.send_message(message.chat.id, 'Please provide your contact information so we can meet with you.', reply_markup=contact_markup)

# Speaker Section command
@bot.message_handler(commands=['speaker_section'])
def handle_speaker_cont(message):
    bot.send_message(message.chat.id, 'Welcome to the speaker room. Are you ready for the best podcast of the year?')
    bot.send_message(message.chat.id,'Please provide your contact information so we can meet with you.', reply_markup=contact_markup)
    bot.send_message(message.chat.id,'register the topic in the next command:/register_topic')
# Register topic command
@bot.message_handler(commands=['register_topic'])    
def handle_speaker_topic(message):    
    bot.send_message(message.chat.id, 'What is the central topic of your podcast?')
    bot.register_next_step_handler(message, process_podcast_detail) 

# Process request topic 
def process_podcast_detail(message):
    user_topic = message.text
    bot.reply_to(message, f'It added for this day: {user_topic} for decoration of the podcast room according to your request.')

# Advertising Campaign command 
@bot.message_handler(commands=['advertising_campaign'])
def camping(message):
    bot.send_message(message.chat.id, 'Welcome to business room, thank you for you believe in us')
    bot.send_message(message.chat.id, 'The next button provides your contact information so we can connect with you and share important details based on your ideas about the product or service offered.',reply_markup=contact_markup)
#bolling and runner main according to the true value.
if __name__ == "__main__":
    bot.polling(none_stop=True)                     