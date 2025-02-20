import requests
from .models.events import Events
from .models.news import News


def get_news():
    try:
        request = requests.get("http://46.148.48.25:3080/api/News")
        request.raise_for_status()
        validated_data = []
        for value in request.json():
            validated_data.append(News.model_validate_strings(value))
        return validated_data

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе: {e}")
        return None
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
        return None


def get_events():
    try:
        request = requests.get("http://46.148.48.25:3080/api/Events")
        request.raise_for_status()
        validated_data = []
        for value in request.json():
            validated_data.append(Events.model_validate_strings(value))
        return validated_data

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе: {e}")
        return None
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
        return None


print(get_news())
