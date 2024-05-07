from aiogram import Router, F
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.filters import Command, CommandStart

from app.keyboards import reply_keyboard, categories, items
from app.database import requests as rq

router = Router()


@router.message(CommandStart())
async def simple_start(message: Message):
    await rq.set_user(tg_id=message.from_user.id)
    await message.answer("Hello", reply_markup=reply_keyboard)


@router.message(F.text == "Katalog")
async def catalog(message: Message):
    await message.answer("Choose a product from the catalog.", reply_markup=await categories())


@router.callback_query(F.data.startswith("category_"))
async def category(callback: CallbackQuery):
    await callback.answer("You chose a category")
    await callback.message.answer("Choose a product from category:",
                                  reply_markup=await items(callback.data.split("_")[1]))


@router.callback_query(F.data.startswith("item_"))
async def item(callback: CallbackQuery):
    found_item = await rq.get_item(callback.data.split("_")[1])
    await callback.answer("You chose an item")
    await callback.message.answer(f"Name: {found_item.name}\nDescription: {found_item.description}"
                                  f"\nPrice: {found_item.price}",
                                  reply_markup=await items(callback.data.split("_")[1]))


