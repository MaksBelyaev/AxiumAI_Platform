import asyncio
import os.path

import pyttsx3
import sounddevice

from Interfece.Core.src.event import Event

name: str = None




async def say_acceptor(queue: asyncio.Queue = None, config: dict = None):
    global name
    while True:
        while True:
            await asyncio.sleep(0)

            if not queue.empty():
                event: Event = await queue.get()
                tts = pyttsx3.init()

                voices = tts.getProperty('voices')

                # Задать голос по умолчанию
                tts.setProperty('voice', 'ru')

                # Попробовать установить предпочтительный голос
                for voice in voices:
                    if voice.name == name:
                        tts.setProperty('voice', voice.id)
                tts.say(event.value)
                tts.runAndWait()


def gen_voice(event: Event):
    tts = pyttsx3.init()

    voices = tts.getProperty('voices')

    # Задать голос по умолчанию
    tts.setProperty('voice', 'ru')

    # Попробовать установить предпочтительный голос
    for voice in voices:
        if voice.name == name:
            tts.setProperty('voice', voice.id)
    tts.say(event.value)
    tts.runAndWait()
    

async def init(config: dict):
    global name

    name = config["name"]

    