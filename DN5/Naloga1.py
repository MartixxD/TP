import requests
import html

def get_html(url):
    page = requests.get(url)
    if page.status_code == 200:
        return page
    else: 
        return False

page = get_html("https://example.com/")

if page == False:
    print (False)
else:
    print(page.text)