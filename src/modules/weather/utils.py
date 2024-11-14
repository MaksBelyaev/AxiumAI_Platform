import asyncio
import logging
import traceback
import re
import pymorphy2
import pyowm

from Interfece.Core.src.event import Event, EventTypes

logger = logging.getLogger(__name__)

api_ow = ""

async def get_weather_forecast(event: Event):
    """ Получение и озвучивание прогноза погоды """
    global api_ow
    city_name = event.value

    # Используем регулярное выражение для извлечения названия города
    match = re.search(r'в ([^>]+)', city_name)
    if match:
        city_name = match.group(1).strip()
    else:
        logger.debug("Не удалось извлечь название города из: " + city_name)
        return
    # Определяем морфологическую форму города в именительном падеже
    morph = pymorphy2.MorphAnalyzer()
    city_name_normalized = morph.parse(city_name)[0].normal_form.capitalize()



    try:
        open_weather_map = pyowm.OWM(api_ow)
        weather_manager = open_weather_map.weather_manager()
        observation = weather_manager.weather_at_place(city_name_normalized)
        weather = observation.weather

        # status = weather.detailed_status()
        temperature = weather.temperature('celsius')["temp"]
        wind_speed = weather.wind()["speed"]
        # pressure = int(weather.pressure["press"] / 1.333)

        # save_to_file(file_path, colored("Погода в " + city_name +
        #                                 # "\n * Status: " + status +
        #                                 "\n * Скорость ветра в м/с: " + str(wind_speed) +
        #                                 "\n * Температура (Celsius): " + str(temperature), "yellow"))
        logger.info("Погода в " + city_name +
            # "\n * Status: " + status +
            "\n * Скорость ветра в м/с: " + str(wind_speed) +
            "\n * Температура (Celsius): " + str(temperature))

        await event.reply(f"В {city_name} сейчас\n"
            f"Температура  {str(temperature)} градусов\n"
            f"Скорость ветра {str(wind_speed)} метров в секунду")



    except Exception as e:
        # save_to_file(file_path, "Попробуйте ещё раз!")
        logger.debug("Попробуйте ещё раз!")
        traceback.print_exc()

def init(config):
    global  api_ow
    api_ow = config["api_open_weather"]