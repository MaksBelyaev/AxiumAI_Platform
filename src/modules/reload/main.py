import os
import sys
import logging

from Interfece.Core.src.event import Event

logger = logging.getLogger("root")


async def reload(event: Event):  # полный перезапуск
    logger.debug(f"Reload...")
    os.execv(sys.executable, [sys.executable] + sys.argv)


intents = [
    {
        "name": "reload",
        "function": reload
    }
]
