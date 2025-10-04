import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

TOKEN = os.getenv("TG_TOKEN")

if not TOKEN:
    raise SystemExit("❌ Please set the TG_TOKEN environment variable.")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Received /start command")
    await update.message.reply_text("👋 Welcome! Type /akhil or /pranav.")

async def akhil(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Received /akhil command")
    await update.message.reply_text("/like gays")

async def pranav(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Received /pranav command")
    await update.message.reply_text("/like ind 7672189143")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Received message: {update.message.text}")
    await update.message.reply_text("I got your message!")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("akhil", akhil))
    app.add_handler(CommandHandler("pranav", pranav))

    # Optional: catch-all for non-command texts
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
