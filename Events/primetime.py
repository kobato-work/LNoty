import asyncio
from aiogram import types, Bot, Dispatcher
from datetime import datetime
from models import User, Base, Setting
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DB_URL, TOKEN

mybot = Bot(token=TOKEN)
dp = Dispatcher(mybot)

engine = create_engine(DB_URL)

Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)


async def primetime_notification_wrapper():
    session = Session()
    users = session.query(User).all()

    for user in users:
        setting = session.query(Setting).filter_by(id_user=user.telegram_id).first()
        if setting.primetime is True:
            await primetime_notification(user)
    session.close()


async def primetime_notification(user: User):
    now = datetime.now().strftime('%H:%M')
    if now == '11:56' or now == '18:56':
        await mybot.send_message(user.telegram_id, '☄️ Хот-тайм зачистки начнется через 4 минуты')
        print(now, user.telegram_id, user.username, 'получил сообщение о начале Прайм-тайма')
    elif now == '13:56' or now == '22:56':
        await mybot.send_message(user.telegram_id, '☄️ Хот-тайм зачистки закончится через 4 минуты')
        print(now, user.telegram_id, user.username, 'получил сообщение о конце Прайм-тайма')
    else:
        print(now, 'Неподходящее время для Прайм-тайма')