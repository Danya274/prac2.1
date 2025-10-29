import logging
import asyncio
from bot import client



async def main():
    ...



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        logging.info('Start bot')
        client.run_until_disconnected()
    except Exception as e:
        logging.info(f'Error: {e}')
    except KeyboardInterrupt:
        logging.info('Programm stopped')

