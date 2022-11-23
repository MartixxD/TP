import requests
import html

file = open("HTML_koda.txt","w")

file.write(requests.get('https://www.rtvslo.si/iskalnik?q=iskalni%20niz').text)