import requests


def get_stock_data():

    url = 'https://jsonplaceholder.typicode.com/todos/1'

    r = requests.get(url)
    data = r.json()

    return data
