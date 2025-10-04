import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TG_TOKEN")

if not TOKEN:
    raise SystemExit("❌ Please set the TG_TOKEN environment variable.")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome! Type /akhil or /pranav.")

async def akhil(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🙋‍♂️ This is Akhil.")

async def pranav(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🧑‍💻 This is Pranav.")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("akhil", akhil))
    app.add_handler(CommandHandler("pranav", pranav))
    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
