import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ChatJoinRequestHandler, ContextTypes

BOT_TOKEN = "8637298706:AAFFaJWyUYkZAuJcZKW_a2Yjno8hgiWCOEc"
CHANNEL_ID = -1004448642076

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot is working! Auto-approve is ON")

async def auto_approve(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user = update.chat_join_request.from_user
        chat = update.chat_join_request.chat
        await context.bot.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
        print(f"✅ {user.first_name} approved!")
    except Exception as e:
        print(f"❌ Error: {e}")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(ChatJoinRequestHandler(auto_approve))
    print("🤖 Bot running! Auto-approving everyone...")
    app.run_polling()

if __name__ == "__main__":
    main()
