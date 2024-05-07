from aiogram import Bot, Dispatcher
import asyncio

from app.handlers import router
from app.database.models import async_main


async def main():
    await async_main()
    bot = Bot(token="6976905939:AAH4QdNWxZG77O7lTe0dTDaPzUUxPzTlKaE")
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        print("Start polling...")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Keyboard pressed.")
