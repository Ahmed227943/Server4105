import keep_alive
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

ردود_هزار = [
    "يا عم ده كلام يخض! 😂",
    "كمل كده وهنرش عليك ميه 😂",
    "انت جبت الكلام ده منين؟ من كوكب الهبد؟ 🌚",
    "كلامك ده يتحط في متحف النكت البايخة 🤣",
    "برافو... ضحكتنا وأنت مش قاصد! 👏",
    "جبت الكلام ده منين؟ من بنك الهبل؟ 🏦",
    "شكلك لسه صاحي من كابوس 😂",
    "قول تاني عشان نسجل الحلقة دي 🎥",
    "مين علمك كده؟ 😂",
    "عاوزين نسقفلك جامد 👏👏👏"
]

async def رد_هزار(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.from_user.is_bot:
        return
    await update.message.reply_text(random.choice(ردود_هزار))

TOKEN = "7500396574:AAH7EQo0EnZ5Y9IKUJD_nNBlUgVi38NjdZUK"
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, رد_هزار))
keep_alive.keep_alive()
app.run_polling()