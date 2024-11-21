import asyncio
import logging
import speech_recognition as sr
from Interfece.Core.src.event import Event, EventTypes

logger = logging.getLogger(__name__)


async def recognize(event: Event):
    text = await voice_listening()  # Асинхронный вызов voice_listening
    event.value = text
    return event


async def voice_listening(queue: asyncio.Queue = None, config: dict = None):
    send_text_event = config["send_text_event"]
    ext_only = config["ext_only"]
    trigger_name = config["trigger_name"]
    if ext_only:
        return
    names = []
    if trigger_name:
        names = [i for i in trigger_name.split("|")]
    logger.info("Запуск распознавателя речи SpeechRecognition вход в цикл")
    r = sr.Recognizer()
    while True:
        await asyncio.sleep(0)  # Позволяем другим задачам выполняться
        with sr.Microphone() as source:
            # logger.info("Слушаем...")
            audio = r.listen(source)  # Устанавливаем таймаут для прослушивания
            try:
                user_command = r.recognize_google(audio, language="ru-RU").lower()
                logger.info(f"SpeechRecognition: '{user_command}'")

                if len(names):
                    for name in names:
                        if name not in user_command:
                            continue
                        logger.debug("Имя обнаружено!")
                        user_command = " ".join(user_command.split(name)[1:]).strip()
                        break
                    else:
                        logger.debug("Имя не найдено!")
                        continue
                await queue.put(Event(event_type=EventTypes.user_command, value=user_command))
                if send_text_event:
                    await queue.put(Event(event_type=EventTypes.text, value=user_command))
                logger.info(f"SpeechRecognition - передано в очередь: '{user_command}'")
                # Ожидание 2-3 секунды перед повторным прослушиванием
                await asyncio.sleep(0.5)  # Задержка перед новым прослушиванием
            except sr.UnknownValueError:
                logger.warning("Не удалось распознать речь")
                continue
            except sr.RequestError as e:
                logger.error(f"Ошибка запроса к сервису распознавания речи: {e}")
                continue
