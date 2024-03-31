import logging

from aiogram import Dispatcher, Bot, types, executor
from aiogram.utils.markdown import hbold

import car.Car
from Config import ID, TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from Keyboards.Keyboard import keyboard_price, car_1000d, car_5000d, car_10000d, car_50000d
from car.Car import Car_info

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

ADMINS = [ID]

Start = """
Привіт. Давай оберемо тобі машину!
Вибери свій бюджет: 
"""
Help = """Список команд:
/help - команди які виконує бот
/start - розпочати роботу з ботом
"""

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer(text=Start, reply_markup=keyboard_price())
    await message.delete()

category = ''
brend = ''

@dp.callback_query_handler(text='Car 1000$')
async def car_1(callback_query: types.CallbackQuery):
    global category
    category = 'Car 1000$'
    await callback_query.message.answer(text="Вибери марку:", reply_markup=car_1000d())

@dp.callback_query_handler(text='Car 5000$')
async def car_2(callback_query: types.CallbackQuery):
    global category
    category = 'Car 5000$'
    await callback_query.message.answer(text="Вибери марку:", reply_markup=car_5000d())

@dp.callback_query_handler(text='Car 10000$')
async def car_3(callback_query: types.CallbackQuery):
    global category
    category = 'Car 10000$'
    await callback_query.message.answer(text="Вибери марку:", reply_markup=car_10000d())

@dp.callback_query_handler(text='Car 50000$')
async def car_4(callback_query: types.CallbackQuery):
    global category
    category = 'Car 50000$'
    await callback_query.message.answer(text="Вибери марку:", reply_markup=car_50000d())

@dp.callback_query_handler(text='Ford Sierra')
async def ford_1000(callback_query: types.CallbackQuery):
    global brend
    brend = 0
    car = Car_info(category, brend)
    brend_info = car['brend']
    model_info = car['model']
    price_info = car['price']
    quality_info = car['quality']
    years_info = car['years']
    url_info = car['url']
    await callback_query.message.answer(text=f'Інформація про машину: \n' \
    f'Бренд - {brend_info}, {model_info}, {price_info}, {quality_info}, {years_info}, {url_info}')

@dp.callback_query_handler(text='BMW 3 Series')
async def ford_1000(callback_query: types.CallbackQuery):
    global brend
    brend = 1
    car = Car_info(category, brend)
    brend_info = car['brend']
    model_info = car['model']
    price_info = car['price']
    quality_info = car['quality']
    years_info = car['years']
    url_info = car['url']
    await callback_query.message.answer(text=f'Інформація про машину: \n' \
    f'Бренд - {brend_info}, {model_info}, {price_info}, {quality_info}, {years_info}, {url_info}')  

@dp.callback_query_handler(text='Audi 80')
async def ford_1000(callback_query: types.CallbackQuery):
    global brend
    brend = 'Audi 80'
    await callback_query.message.answer(text=f'Бренд - Audi 80')

@dp.callback_query_handler(text='Opel Kadett')
async def ford_1000(callback_query: types.CallbackQuery):
    global brend
    brend = 'Opel Kadett'
    await callback_query.message.answer(text=f'Бренд - Opel Kadett')

@dp.callback_query_handler(text='Renault Wind')
async def ford_1000(callback_query: types.CallbackQuery):
    global brend
    brend = 'Renault Wind'
    await callback_query.message.answer(text=f'Бренд - ')

@dp.callback_query_handler(text='Daewoo Lanos')
async def ford_1000(callback_query: types.CallbackQuery):
        global brend
        brend = 'Daewoo Lanos'
        await callback_query.message.answer(text=f'Бренд - ')

@dp.callback_query_handler(text='Skoda Fabia')
async def ford_1000(callback_query: types.CallbackQuery):
    global brend
    brend = 'Skoda Fabia'
    await callback_query.message.answer(text=f'Бренд - ')

@dp.callback_query_handler(text='Toyota Avensis')
async def ford_1000(callback_query: types.CallbackQuery):
    global brend
    brend = 'Toyota Avensis'
    await callback_query.message.answer(text=f'Бренд - ')

@dp.callback_query_handler(text='Porsche Cayenne')
async def ford_1000(callback_query: types.CallbackQuery):
    global brend
    brend = 'Porsche Cayenne'
    await callback_query.message.answer(text=f'Бренд - ')

@dp.callback_query_handler(text='Ford Focus')
async def ford_1000(callback_query: types.CallbackQuery):
    global brend
    brend = 'Ford Focus'
    await callback_query.message.answer(text=f'Бренд - ')

@dp.callback_query_handler(text='Audi A6')
async def ford_1000(callback_query: types.CallbackQuery):
    global brend
    brend = 'Audi A6'
    await callback_query.message.answer(text=f'Бренд - ')

@dp.callback_query_handler(text='Hyundai Elantra')
async def ford_1000(callback_query: types.CallbackQuery):
    global brend
    brend = 'Hyundai Elantra'
    await callback_query.message.answer(text=f'Бренд - ')

@dp.callback_query_handler(text='BMW X5')
async def ford_1000(callback_query: types.CallbackQuery):
    global brend
    brend = 'BMW X5'
    await callback_query.message.answer(text=f'Бренд - ')

@dp.callback_query_handler(text='Audi Q5')
async def ford_1000(callback_query: types.CallbackQuery):
    global brend
    brend = 'Audi Q5'
    await callback_query.message.answer(text=f'Бренд - ')

@dp.callback_query_handler(text='Tesla Model Y')
async def ford_1000(callback_query: types.CallbackQuery):
    global brend
    brend = 'Tesla Model Y'
    await callback_query.message.answer(text=f'Бренд - ')

@dp.callback_query_handler(text='BMW 5 Series')
async def ford_1000(callback_query: types.CallbackQuery):
    global brend
    brend = 'BMW 5 Series'
    await callback_query.message.answer(text=f'Бренд - B')

@dp.message_handler(commands='help')
async def help(message: types.Message):
    await message.answer(text=Help)

if __name__ == '__main__':
    executor.start_polling(dp)