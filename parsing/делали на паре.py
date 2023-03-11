import requests
from bs4 import BeautifulSoup
import lxml

cookies = {
    'qrator_ssid': '1678192005.161.HyINmmmowVncuNfI-qk514i6t57q1vphsamctrvj94pn8f4bm',
    'stest201': '0',
    'stest207': 'acc0',
    'stest209': 'ct2',
    'tp_city_id': '38733',
    'PHPSESSID': '181c36e82333fb366bbc7d0105fa5b2c',
    'user_public_id': 'Hme7iYAmDJVZ7MKU0N74Hfz7ADOa3I1ofBA2XsRpU%2FcpPTwLTKsuagqeZorVzZ%2Fo',
    '_gcl_au': '1.1.1949732666.1678181205',
    '_gid': 'GA1.2.1216130161.1678181206',
    'tmr_lvid': 'dd5a8a36f7b852809fd1f7da86a401ac',
    'tmr_lvidTS': '1678181205591',
    '_ym_uid': '1678181206897226647',
    '_ym_d': '1678181206',
    '_ym_isad': '2',
    '_ym_visorc': 'w',
    'afUserId': '70a2de1b-6f2b-425e-9fc5-cf49933b66a0-p',
    'AF_SYNC': '1678181206595',
    'adrdel': '1',
    'adrcid': 'AzqqjbhvY2Z7bHYjnywyGNQ',
    '_userGUID': '0:ley1rgxc:z2XMfmOEVOVvbUGPOQsNgF0L5LJx7_wB',
    'game3dTopperClosed': 'true',
    'dSesn': '9059f355-41b6-6c0f-d67b-b9c6e4fc0631',
    '_dvs': '0:ley1rgxc:lEpbgSAn1LMnnIp9dZx6klykJTHHulsD',
    'c2d_widget_id': '{%229eb3fbdda817d48faffc65c3446228e8%22:%22[chat]%20385197bca1bf0e19c799%22}',
    'promo1000closed': 'true',
    'pageviewTimerFired15': 'true',
    'pageviewTimerFired30': 'true',
    'pageviewTimerFired60': 'true',
    'qrator_jsid': '1678192004.419.DMdenx8swfRIiv8f-fob7epbk8vddd5q5tpnc6rjq29u1oi12',
    'visitedPagesNumber': '4',
    '_ga_RD4H4CBNJ3': 'GS1.1.1678181205.1.1.1678182532.55.0.0',
    '_ga': 'GA1.1.774084394.1678181206',
    'tmr_detect': '0%7C1678182535229',
    'mindboxDeviceUUID': '35e9f5c1-61db-473d-a44d-72d4e1765d3d',
    'directCrm-session': '%7B%22deviceGuid%22%3A%2235e9f5c1-61db-473d-a44d-72d4e1765d3d%22%7D',
    'pageviewTimer': '1574.7469999999998',
}

headers = {
    'authority': 'sochi.technopark.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'qrator_ssid=1678192005.161.HyINmmmowVncuNfI-qk514i6t57q1vphsamctrvj94pn8f4bm; stest201=0; stest207=acc0; stest209=ct2; tp_city_id=38733; PHPSESSID=181c36e82333fb366bbc7d0105fa5b2c; user_public_id=Hme7iYAmDJVZ7MKU0N74Hfz7ADOa3I1ofBA2XsRpU%2FcpPTwLTKsuagqeZorVzZ%2Fo; _gcl_au=1.1.1949732666.1678181205; _gid=GA1.2.1216130161.1678181206; tmr_lvid=dd5a8a36f7b852809fd1f7da86a401ac; tmr_lvidTS=1678181205591; _ym_uid=1678181206897226647; _ym_d=1678181206; _ym_isad=2; _ym_visorc=w; afUserId=70a2de1b-6f2b-425e-9fc5-cf49933b66a0-p; AF_SYNC=1678181206595; adrdel=1; adrcid=AzqqjbhvY2Z7bHYjnywyGNQ; _userGUID=0:ley1rgxc:z2XMfmOEVOVvbUGPOQsNgF0L5LJx7_wB; game3dTopperClosed=true; dSesn=9059f355-41b6-6c0f-d67b-b9c6e4fc0631; _dvs=0:ley1rgxc:lEpbgSAn1LMnnIp9dZx6klykJTHHulsD; c2d_widget_id={%229eb3fbdda817d48faffc65c3446228e8%22:%22[chat]%20385197bca1bf0e19c799%22}; promo1000closed=true; pageviewTimerFired15=true; pageviewTimerFired30=true; pageviewTimerFired60=true; qrator_jsid=1678192004.419.DMdenx8swfRIiv8f-fob7epbk8vddd5q5tpnc6rjq29u1oi12; visitedPagesNumber=4; _ga_RD4H4CBNJ3=GS1.1.1678181205.1.1.1678182532.55.0.0; _ga=GA1.1.774084394.1678181206; tmr_detect=0%7C1678182535229; mindboxDeviceUUID=35e9f5c1-61db-473d-a44d-72d4e1765d3d; directCrm-session=%7B%22deviceGuid%22%3A%2235e9f5c1-61db-473d-a44d-72d4e1765d3d%22%7D; pageviewTimer=1574.7469999999998',
    'if-none-match': '"144d53-1wncIXqGgjxbBhXtvKt9Rmz+8lM"',
    'referer': 'https://sochi.technopark.ru/?utm_referrer=https%3A%2F%2Fwww.yandex.ru%2F',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}

response = requests.get('https://sochi.technopark.ru/smartfony/', cookies=cookies, headers=headers)
#with open("technopark.html","w", encoding="UTF-8") as f:
   # f.write(response.text)

with open("technopark.html", "r", encoding="UTF-8") as file:
    page = file.read()
    bs = BeautifulSoup(page, "lxml")
    containers = bs.find_all("div", "product-card-big__container")
    result = {}
    for i in containers:
        name = i.find("div", "product-card-big__name").text
        price = i.find("div", "product-card-big__price").text
        result[name] = price
    print(result)
