from bs4 import BeautifulSoup
import requests

def parse ():
    # Создаются переменные для того, чтобы браузер не считал нас ботом
    URL = 'https://www.olx.kz/elektronika/kompyutery-i-komplektuyuschie/'
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0'}
    # Создаем ответ (response) на наш запрос (requests.get)
    response = requests.get(URL, headers=HEADERS)
    # Создаем переменную soup для получения контента страницы (response.content)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div', class_='offer-wrapper')
    comps = []
    # Пробигаемся по нашим найденым айтемам и добавляем их в список-словарь
    for item in items:
        i = 1
        comps.append({
            # Отсортируем наши елементы. С помощью .get_text достанем из них Text strip=True, без пробелов
            'title': item.find('a', class_='marginright5').get_text(strip=True),
            'price': item.find('p', class_='price').get_text(strip=True),
            'link': item.find('a', class_='marginright5').get('href')
            })
        # Создаем цикл, который будет просто выводить елементы по ключу 'title'
        for comp in comps:
            print(f"{comp['title']} -> Price: {comp['price']} -> link: {comp['link']}")


parse()
