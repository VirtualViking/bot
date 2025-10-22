import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Función para el comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('¡Hola! Soy un bot de eco. Envíame un mensaje y te lo repetiré.')

# Función que repite el mensaje del usuario
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)

def main() -> None:
    # 1. AQUÍ ES DONDE LEE LA VARIABLE DE ENTORNO
    # Railway pondrá tu token secreto en esta variable "TELEGRAM_TOKEN"
    TOKEN = os.environ.get("AAHn0BwYczCdNuO5tp4tM6z0YsXeciOiz6k")

    if not TOKEN:
        print("Error: No se encontró la variable de entorno TELEGRAM_TOKEN")
        return

    # 2. Configura la aplicación con el token
    application = Application.builder().token(TOKEN).build()

    # 3. Define los comandos que el bot "escuchará"
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # 4. Inicia el bot
    print("Bot iniciado y esperando mensajes...")
    application.run_polling()

if __name__ == '__main__':
    main()