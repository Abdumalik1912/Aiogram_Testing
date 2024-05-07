from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from app.database import requests as rq
from aiogram.utils.keyboard import InlineKeyboardBuilder

reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Katalog")],
    [KeyboardButton(text="Korzinka")],
    [KeyboardButton(text="Aloqalar"), KeyboardButton(text="Biz haqimizda")]],
    resize_keyboard=True,
    input_field_placeholder="Qator tanlang..."
)


async def categories():
    all_categories = await rq.get_categories()

    keyboard = InlineKeyboardBuilder()

    for category in all_categories:
        keyboard.add(InlineKeyboardButton(text=f"{category.name}", callback_data=f"category_{category.id}"))
    keyboard.add(InlineKeyboardButton(text="Main Menu", callback_data="to_main"))
    return keyboard.adjust(2).as_markup()


async def items(category_id):
    all_items = await rq.get_category_items(category_id)

    keyboard = InlineKeyboardBuilder()

    for item in all_items:
        keyboard.add(InlineKeyboardButton(text=f"{item.name}", callback_data=f"item_{item.id}"))
    keyboard.add(InlineKeyboardButton(text="Main Menu", callback_data="to_main"))
    return keyboard.adjust(2).as_markup()