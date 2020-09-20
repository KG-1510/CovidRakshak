from django.shortcuts import render
import requests
import json

def database():
    re= requests.get("http://gsx2json.com/api?id=104iTkc01Gnq79wi0ax1PmbDWZgwFqYGgiJovzF7zLMI&sheet=1")
    je= re.json()
    print(je)
    return 0 #render(request, 'app1/database.html', s)

database()    