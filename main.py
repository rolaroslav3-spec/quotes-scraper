#импорты
import json
import requests
from bs4 import BeautifulSoup
#сылка
url = "https://quotes.toscrape.com/"
response = requests.get(url)

print(f"статус сервер: {response.status_code}")
if response.status_code == 200:#проверка сайта
    soup = BeautifulSoup(response.text, "html.parser")
    quote_block = soup.find_all("div", class_="quote")
    quotes_data = []
    for block in quote_block:
        text = block.find("span", class_="text").text
        author = block.find("small", class_="author").text
        quotes_data.append({"author": author, "text": text})
    with open("quotes_data.json", "w", encoding="utf-8") as f:
        json.dump(quotes_data, f, ensure_ascii=False, indent=1)
    print("Все цитаты успешно сохранены в файл quotes.json!")
else:
    print(f"{response.status_code}")
