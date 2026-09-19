import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ChatJoinRequestHandler, ContextTypes

# ---------- CONFIG ----------
BOT_TOKEN = "8637298706:AAFFaJWyUYkZAuJcZKW_a2Yjno8hgiWCOEc"
ADMIN_ID = 8961906024  # sirf ye admin log dekh sakta hai

# ---------- START ----------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return
    await update.message.reply_text(
        "✅ Bot is working!\n"
        "🔓 Auto-approve is ON for ALL groups/channels.\n"
        "🔇 No welcome message will be sent."
    )

# ---------- AUTO APPROVE (SAB JAGAH) ----------
async def auto_approve(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        req = update.chat_join_request
        user = req.from_user
        chat = req.chat

        # ✅ Approve karo - koi message nahi bhejna
        await context.bot.approve_chat_join_request(
            chat_id=chat.id,
            user_id=user.id
        )

        # 🔇 Koi welcome message NAHI bhejna
        # 🔇 User ke DM me kuch NAHI bhejna
        # 🔇 Group me kuch NAHI bhejna

        print(f"✅ {user.first_name} ({user.id}) approved in {chat.title} ({chat.id})")

    except Exception as e:
        print(f"❌ Error: {e}")

# ---------- MAIN ----------
def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(ChatJoinRequestHandler(auto_approve))

    print("=" * 50)
    print("🤖 Auto-Approve Bot Running!")
    print("🔓 Approving ALL join requests in ALL chats")
    print("🔇 No welcome messages sent")
    print("=" * 50)

    app.run_polling()

if __name__ == "__main__":
    main()
