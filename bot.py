from aiogram import Bot, Dispatcher, executor, types
from config import BOT_TOKEN
from database import is_subscribed
from payments import create_payment_link
from content import PARKING_FINE_EE

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(msg: types.Message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("🚗 Штрафы", "💳 Подписка")
    await msg.answer("Привет! Я помогу со штрафами в ЕС.", reply_markup=kb)

@dp.message_handler(lambda m: m.text == "🚗 Штрафы")
async def fines(msg: types.Message):
    if not is_subscribed(msg.from_user.id):
        link = create_payment_link()
        await msg.answer(f"🔒 Доступ по подписке\nОплатить: {link}")
        return
    await msg.answer(PARKING_FINE_EE)

executor.start_polling(dp)
