import requests
import html
import json

def get_api_data(url):

    page = requests.get(url)
    if page.status_code == 200:
        page = page.text
        data1 = json.loads(page)
        return data1
    else: 
        return False


data = get_api_data("https://jsonplaceholder.typicode.com/todos/1")

if data == False:
    print (False)
else:
    print(data)
