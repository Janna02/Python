# Прикрутить телеграмм бота к задачам с предыдущего семинара:

# Условие задачи: На столе лежит 221 конфета.
#  Играют два игрока делая ход друг после друга. 
#  Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
#   Все конфеты оппонента достаются сделавшему последний ход.

#     Добавьте игру против бота ( где бот берет рандомное количество конфет от 0 до 28)

#     Подумайте как наделить бота ""интеллектом""
#      (есть алгоритм, позволяющий выяснить какое количество конфет
#       необходимо брать, чтобы гарантированно победить, соответственно внедрить этот алгоритм боту )



from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters, ConversationHandler
from random import randint
import Functions




app = ApplicationBuilder().token("TOKEN").build()

app.add_handler(ConversationHandler(entry_points= [CommandHandler("game", Functions.game)], 
                                    states={Functions.my_turn:[MessageHandler(filters.TEXT, Functions.gamer_turn)], 
                                           Functions.bot:[MessageHandler(filters.TEXT, Functions.bot_turn)]},
                                    fallbacks=[CommandHandler("cancel", Functions.cancel)]))

app.add_handler(CommandHandler("hello", Functions.hello))


app.run_polling()