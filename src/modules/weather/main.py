from .utils import init, get_weather_forecast

intents = [
    {
        "name": "get_weather_forecast",
        "function": get_weather_forecast
    }
]