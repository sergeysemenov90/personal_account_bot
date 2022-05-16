from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton

share_kb = KeyboardButton('Поделиться контактом', request_contact=True)
contact_request_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(share_kb)


get_kp = KeyboardButton('получить кп')
get_deals = KeyboardButton('получить сделки')
all_func_kb = ReplyKeyboardMarkup().row(get_kp, get_deals)
