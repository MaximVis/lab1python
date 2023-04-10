from bs4 import BeautifulSoup # импортируем библиотеку BeautifulSoup
import requests # импортируем библиотеку requests

def parse():
    url = 'https://omgtu.ru/general_information/faculties/'  # передаем необходимы URL адрес
    page = requests.get(url)  # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    soup = BeautifulSoup(page.text, "html.parser")  # передаем страницу в bs4
    block = soup.findAll('div', class_='main__content')  # находим  контейнер с нужным классом
    description = ''
    for data in block:  # проходим циклом по содержимому контейнера
        if data.find('ul'):  # находим тег <ul>
            description = data.text  # записываем в переменную содержание тега
    my_file = open("faculteti.txt", "w")
    my_file.write(description)
    my_file.close()


if __name__ == '__main__':
    parse()
