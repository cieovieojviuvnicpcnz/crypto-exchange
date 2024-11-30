from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Ouvrir l'Exchange Crypto", web_app={"url": "https://https://cieovieojviuvnicpcnz.github.io/crypto-exchange"})]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Cliquez pour accéder à l’Exchange Crypto.', reply_markup=reply_markup)

if __name__ == "__main__":
    app = ApplicationBuilder().token("7691843688:AAF3tOKix8gQPUD-py-ElqHap-e83A8Duxs").build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
