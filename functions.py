from urllib.parse import quote_plus

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


SearchTypesUrl = {
    "Веб": "https://www.google.com/search?q=",
    "Новости": "https://www.google.com/search?tbm=nws&q=",
    "Изображения": "https://www.google.com/search?tbm=isch&q=",
    "Видео": "https://www.google.com/search?tbm=vid&q="
}

SearchEnginesUrl = {
    "Google": "https://www.google.com/search?q=",
    "Bing": "https://www.bing.com/search?q=",
    "DuckDuckGo": "https://duckduckgo.com/?q="
}

GoogleLanguages = {
    "Авто": None,
    "Русский": ("ru", "lang_ru"),
    "English": ("en", "lang_en"),
    "Deutsch": ("de", "lang_de"),
    "Français": ("fr", "lang_fr"),
    "Español": ("es", "lang_es")
}

GoogleRegions = {
    "Не ограничивать": None,
    "Россия": "ru",
    "США": "us",
    "Великобритания": "uk",
    "Германия": "de",
    "Франция": "fr",
    "Европа": "eu"
}

Sources = {
    "Все источники": None,
    "GitHub": "site:github.com",
    "Reddit": "site:reddit.com",
    "YouTube": "site:youtube.com",
    "Scratch": "site:scratch.mit.edu",
    "LinkedIn": "site:linkedin.com",
    "Wikipedia": "site:wikipedia.org"
}


def RunOsint(
    request,
    se,
    inc,
    safe_mode,
    search_type,
    Search_Engine,
    target_type,
    source_type,
    language,
    region
):
    options = webdriver.ChromeOptions()

    if inc:
        options.add_argument("--incognito")

    if Search_Engine not in SearchEnginesUrl:
        raise ValueError(f"Неизвестная поисковая система: {Search_Engine}")

    if search_type not in SearchTypesUrl:
        raise ValueError(f"Неизвестный тип поиска: {search_type}")

    query = request.strip()

    if target_type in {
        "Username",
        "E-mail",
        "Телефон",
        "IP-адрес",
        "URL",
        "Имя"
    }:
        query = f'"{query}"'
    elif target_type == "Домен":
        query = f"site:{query}"

    if se and not (query.startswith('"') and query.endswith('"')):
        query = f'"{query}"'

    source_operator = Sources.get(source_type)

    if source_operator:
        query = f"{query} {source_operator}"

    encoded_query = quote_plus(query)

    if Search_Engine == "Google":
        base_url = SearchTypesUrl[search_type]

    elif Search_Engine == "Bing":
        if search_type == "Веб":
            base_url = "https://www.bing.com/search?q="
        elif search_type == "Новости":
            base_url = "https://www.bing.com/news/search?q="
        elif search_type == "Изображения":
            base_url = "https://www.bing.com/images/search?q="
        elif search_type == "Видео":
            base_url = "https://www.bing.com/videos/search?q="
        else:
            raise ValueError(
                f"Неподдерживаемый тип поиска Bing: {search_type}"
            )

    elif Search_Engine == "DuckDuckGo":
        if search_type != "Веб":
            raise ValueError(
                f"Тип '{search_type}' пока не реализован для DuckDuckGo"
            )

        base_url = "https://duckduckgo.com/?q="

    else:
        raise ValueError(
            f"Неизвестная поисковая система: {Search_Engine}"
        )

    url = f"{base_url}{encoded_query}"

    if Search_Engine == "Google":
        if safe_mode:
            url += "&safe=active"

        language_data = GoogleLanguages.get(language)

        if language_data:
            hl, lr = language_data
            url += f"&hl={hl}&lr={lr}"

        region_code = GoogleRegions.get(region)

        if region_code:
            url += f"&gl={region_code}"

    elif Search_Engine == "Bing":
        if safe_mode:
            url += "&safeSearch=Strict"
        else:
            url += "&safeSearch=Off"

        BingLanguages = {
            "Авто": None,
            "Русский": "ru-RU",
            "English": "en-US",
            "Deutsch": "de-DE",
            "Français": "fr-FR",
            "Español": "es-ES"
        }

        bing_language = BingLanguages.get(language)

        if bing_language:
            url += f"&setlang={bing_language[:2]}"
            url += f"&cc={bing_language[-2:]}"

    elif Search_Engine == "DuckDuckGo":
        if safe_mode:
            url += "&kp=1"

    print("=" * 60)
    print("PySint")
    print("=" * 60)
    print("Исходный запрос:", request)
    print("Итоговый запрос:", query)
    print("Точный поиск:", se)
    print("Инкогнито:", inc)
    print("SafeSearch:", safe_mode)
    print("Тип поиска:", search_type)
    print("Поисковая система:", Search_Engine)
    print("Тип цели:", target_type)
    print("Источник:", source_type)
    print("Язык:", language)
    print("Регион:", region)
    print("URL:", url)
    print("=" * 60)

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.get(url)

    return driver