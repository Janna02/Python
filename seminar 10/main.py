# Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters, ConversationHandler
import logic, Logger

A = 0


app = ApplicationBuilder().token("TOKEN").build()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Привет, {update.effective_user.first_name}!\nВведите выражение для вычисления без пробелов: ')
    return A

async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    try:
        result = logic.button_click(text)
        await update.message.reply_text(f'Ответ = {round(result, 3)}')
        Logger.log_command(update, context, result)
    except ValueError:
        await update.message.reply_text(f'Что не то ввели, попробуйте еще раз!')
    return A

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Пока")
    return ConversationHandler.END    

app.add_handler(ConversationHandler(entry_points=[CommandHandler("calc", start)], 
                                    states={A:[MessageHandler(filters.TEXT, calc)]}, 
                                    fallbacks=[CommandHandler('cancel', cancel)]))

app.run_polling()