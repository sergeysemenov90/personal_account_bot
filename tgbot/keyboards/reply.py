from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton

a = KeyboardButton('Поделиться контактом', request_contact=True)
contact_request_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(a)

