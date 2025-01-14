from aiogram import Bot, Dispatcher, executor, types, filters
from config import TOKEN, DB_URL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from DataBase.User import User
from DataBase.Base import Base
from aiocron import crontab
import asyncio
from datetime import datetime


mybot = Bot(token=TOKEN)
dp = Dispatcher(mybot)

engine = create_engine(DB_URL)

Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    session = Session()

    user = session.query(User).filter_by(telegram_id=message.from_user.id).first()

    if user and user.server == 'ruoff':
        await message.answer('Доступные команды:\n'
                             '\n'
                             '/start - запуск бота\n'
                             '/about - о боте\n'
                             '/mysettings - персональные настройки\n'
                             '/help - список команд\n'
                             '/donate - разработчику на мармелад\n'
                             '/feedback - оставить предложение\n'
                             '\n'
                             '/stop - отменить все оповещения\n'
                             '\n'
                             '/time - установить время работы оповещений\n'
                             '/event - не подвезли\n'
                             '/festival - Секретная лавка\n'
                             '/calendar - закончился\n'
                             '/kuka - Кука и Джисра\n'
                             '/keber - Кебер\n'
                             '/loa - Логово Антараса\n'
                             '/frost - Замок Монарха Льда\n'
                             '/fortress - Крепость Орков\n'
                             '/balok - Битва с Валлоком\n'
                             '/olympiad - Всемирная Олимпиада\n'
                             '/hellbound - Остров Ада\n'
                             '/siege - Осада Гирана\n'                             
                             '/primetime - Прайм Тайм Зачистки\n'
                             '/purge - Зачистка\n'
                             '/invasion - Вторжение\n'
                             '\n'
                             '/options - раздел персональных настроек\n'
                             '/bigwar - раздел для бигвара\n')

    session.close()
