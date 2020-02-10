from django.conf import settings

import requests as req
from bs4 import BeautifulSoup
import json


def downloader(link):
    source = "https://ttdownloader.com/download_ajax/"
    resp = req.post(source, data={"url":link}, verify=True)

    soup = BeautifulSoup(resp.text, 'html.parser')
    links = soup.find_all('a')
    links_list = []
    for link in links:
    	links_list += (link["href"],)
    return json.dumps(links_list)
