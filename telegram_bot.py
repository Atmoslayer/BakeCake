from aiogram.utils import executor
from create_bot import dispatcher
from handlers import client, other


if __name__ == '__main__':
    async def on_startup(_):
        print('Бот вышел в онлайн')
    

    client.register_handlers_client(dispatcher)
    other.register_handlers_other(dispatcher)

    executor.start_polling(dispatcher, skip_updates=True, on_startup=on_startup)
