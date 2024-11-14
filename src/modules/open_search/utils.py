import asyncio
import logging
import webbrowser
import keyboard
import pyscreenshot
import requests
from bs4 import BeautifulSoup

from Interfece.Core.src.event import Event, EventTypes

logger = logging.getLogger(__name__)


def open_url(url):
    async def wrapper(event):
        webbrowser.open(url)
        logger.debug("maker url_opener отработал")

    return wrapper


def keyboard_shortcut(key):
    async def key_short(event):
        keyboard.send(key)
        logger.debug("maker keyboard_shortcut отработал")

    return key_short


async def video_on_youtube(event: Event):
    """ Поиск видео на YouTube с автоматическим открытием ссылки на список результатов
    :param args: фраза поискового запроса
    """
    webbrowser.get().open("https://www.youtube.com/results?search_query=" + event.value)


async def person_search(event: Event):
    """ Поиск человека по базе данных социальной сети ВКонтакте """
    if not event.value:
        return

    # Открытие ссылки на поисковик в браузере
    url_browser = "https://google.com/search?q=" + event.value
    webbrowser.open(url_browser)  # .get()

    # Открытие ссылки на поисковики социальных сетей в браузере
    vk_url = "https://vk.com/people/" + event.value
    webbrowser.open(vk_url)
    # save_to_file(file_path, 'Поиск завершен.')
    logger.debug("Поиск завершен.")


async def search_for_term_on_google(event: Event):
    """
    Поиск в Google с автоматическим открытием ссылок (на список результатов и на сами результаты, если возможно)
    :param args: фраза поискового запроса
    """

    # открытие ссылки на поисковик в браузере
    webbrowser.get().open("https://google.com/search?q=" + event.value)


async def definition_on_wikipedia(event: Event):
    url = "https://ru.wikipedia.org/wiki/" + event.value
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        summary = soup.find('p').get_text()
        webbrowser.get().open(url)
        # save_to_file(file_path, f"Вот что я нашел {args} на википедии: {summary}")
        return summary
    else:
        return "Ошибка при загрузке страницы."


async def screenshot():
    # To capture the screen
    image = pyscreenshot.grab()
    # To display the captured screenshot
    image.show()
    # To save the screenshot
    image.save("photo.png")

