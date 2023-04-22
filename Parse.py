from bs4 import BeautifulSoup # импортируем библиотеку BeautifulSoup
import requests # импортируем библиотеку requests


def parse():
    url = 'https://omgtu.ru/general_information/faculties/'  # передаем необходимы URL адрес
    page = requests.get(url)  # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    soup = BeautifulSoup(page.text, "html.parser")  # передаем страницу в bs4
    blockfacultetov = soup.findAll('div', id='pagecontent')  # находим  контейнер с нужным классом
    description = ''
    for data in blockfacultetov:#добавление факультетов
        rows = data.find_all('li')
    for peremennaya in rows:
        if peremennaya.find('span'):
            description += peremennaya.text
            description += "\n"
    txtput(description)


def txtput(description):
    my_file = open("faculteti.txt", "w")
    my_file.write(description)
    my_file.close()
