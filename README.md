# Quotes Web Scraper

Простой и чистый парсер цитат с сайта [quotes.toscrape.com](https://quotes.toscrape.com/).

## Технологии
- Python 3
- Requests
- BeautifulSoup4

## Что делает скрипт
1. Отправляет GET-запрос к сайту и проверяет статус ответа сервера (HTTP 200).
2. Извлекает текст цитат и имена авторов из HTML-кода страницы.
3. Сохраняет структурированные данные в файл `quotes_data.json` в кодировке UTF-8.
