from django.conf import settings

import requests as req
from bs4 import BeautifulSoup
import json


def downloader(link):
    # source = "https://ttdownloader.com/download_ajax/"
    # resp = req.post(source, data={"url":link}, verify=True)
    #
    # soup = BeautifulSoup(resp.text, 'html.parser')
    # links = soup.find_all('a')
    #
    # dictdata = ["without_watermark","watermark","audio"]
    # i = 0
    # links_list = {}
    #
    # for link in links:
    # 	links_list[dictdata[i]] = link["href"]
    # 	i = i + 1
    # return json.dumps(links_list)

    source = "https://freevideosdowloader.tk/services/downloader_api.php"
    resp = req.post(source, data={"url": link}, verify=True).text
    links_list = json.loads(resp)["VideoResult"][0]["VideoUrl"]


    # url = 'https://ssstik.io/'
    # resp = req.get(url)
    # soup = BeautifulSoup(resp.text, 'html.parser')
    # post_param = soup.find("form")["data-hx-post"][1:]
    # source = url + post_param
    #
    # resp = req.post(source,data={"id":link,"locale":"en","tt":0,"ts":0})
    # soup = BeautifulSoup(resp.text, 'html.parser')

    return links_list
