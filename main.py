import telebot
from telebot import types

bot = telebot.TeleBot('7689115533:AAFMXoJ4x8Q04mjDWBeKBeHECKo5ZuN9vzU')

@bot.message_handler(commands = ['start'])
def language(message):
    markup = types.InlineKeyboardMarkup()

    btn_ru = types.InlineKeyboardButton('🇷🇺 Русский', callback_data='russian')
    btn_en = types.InlineKeyboardButton('🇺🇸 English', callback_data='english')

    markup.add(btn_ru)
    markup.add(btn_en)

    bot.reply_to(
        message,
        """Выберите язык:
        
Choose language:""",
        reply_markup=markup
    )



@bot.callback_query_handler(func=lambda call: call.data == 'russian')
def russian(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.send_message(
        call.message.chat.id,
        """Привет! 👋 Я — Media Catch Bot

Я помогу тебе скачать видео и фото с:
📹 YouTube
🎵 TikTok
📸 Instagram
📌 Pinterest

👉 Просто отправь ссылку — и получишь файл в лучшем качестве!
"""
    )

@bot.callback_query_handler(func=lambda call: call.data == 'english')
def english(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.send_message(
        call.message.chat.id,
        f"""Hi! 👋 I’m Media Catch Bot

I help you download videos and photos from:
📹 YouTube
🎵 TikTok
📸 Instagram
📌 Pinterest

👉 Just send a link — and you’ll get the file in the best quality! """
    )

bot.infinity_polling()