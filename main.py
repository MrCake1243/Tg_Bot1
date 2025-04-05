import telebot
import config
import random
import math


bot = telebot.TeleBot(config.TG_API_TOKEN)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Введите команду")


@bot.message_handler(commands=["rnd"])
def send_welcome(message):
    bot.reply_to(message, str(random.randint(1, 3)))



@bot.message_handler(commands=["joke"])
def send_welcome(message):
    jokes = int(random.randint(1, 5))
    match jokes:
        case 1:
            bot.reply_to(
                message, "Дагестанские учёные расщепляют атомы на саламалекулы"
            )
        case 2:
            bot.reply_to(
                message, "У девочки, болеющей раком, во время игры в покер выпало каре"
            )
        case 3:
            bot.reply_to(
                message,
                "Почему брачное агентство для геев терпит убытки? Они еле сводят концы с концами",
            )
        case 4:
            bot.reply_to(
                message, "У физрука четыре сына: первый, второй, первый, второй"
            )
        case 5:
            bot.reply_to(message, "В кружке по скалолазанью не любят сорванцов")

@bot.message_handler(commands=["math"])
def send_math(message):

    a = random.randint(1, 50)
    x = random.randint(1, 20)
    operation = random.randint(1, 3)
    c = random.randint(1, 100)
    if operation == 1:
        b = a * x + c
        equ = f"{a}x + {c} = {b}"
        sol = (b - c) // a
    elif operation == 2:
        b = a * x * c
        equ = f"{a}x * {c} = {b}"
        sol = b // (a * c)
    elif operation == 3:
        b = a * x - c
        equ = f"{a}x - {c} = {b}"
        sol = (b + c) // a  
    bot.send_message(message.chat.id, f"{equ} <tg-spoiler>  Ответ x = {sol} </tg-spoiler>", parse_mode='HTML')


@bot.message_handler(commands=["about"])
def send_welcome(message):
    bot.reply_to(message, "Разработчик: Бузаев В.Э.\nГруппа: Т-233901-ИСТ")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == "Глупая машина":
        bot.send_message(message.chat.id, "Зато мне не надо на учёбу")
    elif message.text == "Ты чего грубишь?":
        bot.send_message(message.chat.id, "Ты первый начал")
    elif message.text == "Ладно, извини":
        bot.send_message(message.chat.id, "И ты меня извини")


bot.infinity_polling()
