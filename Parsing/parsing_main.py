import bs4
import requests
from fake_useragent import UserAgent
from pprint import pprint


KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'технологии', 'компании', 'систем', 'сети']

base_URL = "https://habr.com"
URL = base_URL + "/ru/all/"
HEADERS = headers={'User-Agent': UserAgent().chrome}

response = requests.get(URL, headers=HEADERS)
text = response.text

soup = bs4.BeautifulSoup(text, features="html.parser")

articles = soup.find_all("article")

def find_title():
    for article in articles:
        hubs_h2 = article.find_all(class_="article-formatted-body")
        for hub in hubs_h2:
            for keyword in KEYWORDS:
                if keyword in hub.text:
                    href = article.find(class_="tm-article-snippet__title-link")
                    title = article.find("h2").find("span").text
                    time = article.find("time")
                    print(f'Найдено совпадение по слову "{keyword}"! \n'
                          f'Дата - {time["title"]}\n'
                          f'Название - "{title}"\n'
                          f'Ссылка - {base_URL + href["href"]}')
                    break

def find_url():
    list_news_dict = []
    for article in articles:
        hubs_h2 = article.find_all(class_="article-formatted-body")
        for hub in hubs_h2:
            href = article.find(class_="tm-article-snippet__title-link")
            title = article.find("h2").find("span").text
            time = article.find("time")
            # print(f'{base_URL+href["href"]} - {title}')
            news_dict = {'href': base_URL+href["href"], 'title': title, 'time': time["title"]}
            list_news_dict.append(news_dict)
    return list_news_dict

def find_all_text():
    for news in find_url():
        response = requests.get(news["href"], headers=HEADERS)
        text = response.text
        soup = bs4.BeautifulSoup(text, features="html.parser")
        article = soup.find("article").find(class_="article-formatted-body")
        for keyword in KEYWORDS:
            if keyword in article.text:
                print("_"*50)
                print(f'Найдено совпадение по слову "{keyword}"! \n'
                  f'Дата - {news["time"]}\n'
                  f'Название - "{news["title"]}"\n'
                  f'Ссылка - {news["href"]}')
                break # поиск ведётся до первого соответствия критерию

# Поиск по заголовку - основное задание
# find_title()

# Поиск по всему тексту в статье
find_all_text()
