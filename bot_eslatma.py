import asyncio
import os
import nest_asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import schedule
import time
import threading

# Token kodda saqlanmaydi: uni TOKEN muhit o'zgaruvchisi orqali bering (Render -> Environment)
TOKEN = os.environ.get("TOKEN")
if not TOKEN:
    raise SystemExit("❌ TOKEN muhit o'zgaruvchisi o'rnatilmagan. @BotFather'dan olingan tokenni TOKEN ga yozing.")
CHAT_ID = 878579291

# nest_asyncio -> loop muammosini hal qiladi
nest_asyncio.apply()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom Maqsudxon! Men eslatma botiman. Sizga kuningizni samarali tartiblashga yordam beraman")

async def test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Test xabari yuborildi!")
    await context.bot.send_message(chat_id=CHAT_ID, text="🧪 Bu test xabari.")

async def send_scheduled_message(app, text):
    await app.bot.send_message(chat_id=CHAT_ID, text=text)

def schedule_task(app, loop, text):
    asyncio.run_coroutine_threadsafe(send_scheduled_message(app, text), loop)

# To'liq eslatmalar
schedule_tasks = [
    ("05:30", "🌅 Hayrli tong, Maqsudxon! Bugungi kuningiz barakali bo‘lsin. Yuzingizni yuvib, yangi kunni niyat bilan boshlang!"),
    ("06:00", "🏃‍♀️ Mashg‘ulot va yurish vaqti! Salomatligingiz – sizning kuchingiz!"),
    ("06:45", "🍳 Nonushta vaqti! Miyangiz va tanangiz uchun energiya zaryadi oling."),
    ("07:15", "📖 Ilm olish vaqti! Bilim sizni kuchli va o‘zgacha qiladi!"),
    ("09:15", "🎬 Endi esa ijod va video ishlari vaqti! Foydali kontent orqaga emas, olg‘a olib boradi!"),
    ("11:00", "☕ Yengil tanaffus va choy vaqti! Bosh miyangizga biroz dam bering."),
    ("11:15", "🎤 Tovush yozish va tahrir qilish vaqti! Har bir detallni e’tibor bilan bajaring."),
    ("12:15", "🍽️ Tushlik vaqti! Sog‘lom ovqat – sog‘lom fikr!"),
    ("13:00", "🧑‍🏫 Endi o‘quvchilaringizga ilhom berish vaqti! Siz bilimni ulashayotgan buyuk ustozsiz!"),
    ("15:15", "🧑‍🏫 Darslar o'tish davomida qisqa tanafus qiling, bu sizni samarali ishlashingizga yordam beradi!"),
    ("18:15", "📿 Ma’naviy dam olish! Ruhingizni oziqlantiring."),
    ("18:45", "🥣 Yengil kechki ovqat tayyor bo‘lsa kerak! Sog‘lom ovqat bilan kunni tugating."),
    ("19:15", "🌇 Havo toza, yurishga chiqing yoki yaqinlaringiz bilan suhbatlashing."),
    ("20:00", "🎧 Endi o‘rganish yoki ilhom olish vaqti! Siz har kuni o‘sayotgan insonsiz."),
    ("21:30", "📓 Bugun qanday o‘tdi? Shukr yozing va ertangi kuningizni rejalang."),
    ("22:00", "🌙 Hayrli tun, Maqsudxon. Yaxshi uxlash sizni ertaga yanada kuchli qilish uchun kerak!"),
]

def run_schedule(app, loop):
    for time_str, text in schedule_tasks:
        schedule.every().day.at(time_str).do(schedule_task, app=app, loop=loop, text=text)
    while True:
        schedule.run_pending()
        time.sleep(1)

async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("test", test))

    loop = asyncio.get_running_loop()
    threading.Thread(target=run_schedule, args=(app, loop), daemon=True).start()

    print("✅ Bot ishga tushdi!")
    await app.run_polling()

# Asosiy ishga tushirish
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
