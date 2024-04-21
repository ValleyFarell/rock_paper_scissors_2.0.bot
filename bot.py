import asyncio
import logging
from aiogram import Bot, Dispatcher
from config.config import Config, load_config
from handlers import user_handlers
from aiogram.fsm.storage.memory import MemoryStorage

logger = logging.getLogger(__name__)

async def main():
    logging.basicConfig(level=logging.INFO,
                format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')
    
    logger.info('Starting bot')

    config: Config = load_config('.env')

    bot: Bot = Bot(token=config.tg_bot.token,
                   parse_mode='HTML')
    storage: MemoryStorage = MemoryStorage()
    dp: Dispatcher = Dispatcher(storage=storage)
    dp.include_router(user_handlers.main_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())


