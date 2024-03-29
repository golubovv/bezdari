import requests
from bs4 import BeautifulSoup

def test_parse():
    url_icehow = "https://iceshow-perm.ru/"
    url_kassy= "https://perm.kassy.ru/"

    headers = {
        "Accept":"*/*",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"
        }

    req = requests.get(url=url_icehow, headers=headers)
    src = req.text

    soup = BeautifulSoup(src, "lxml")
    all_class_event = soup.find_all(class_="sueta-afisha-element")

    all_event_list = []
    for item in all_class_event:
        dict_event = {}
        item_date = item.find(class_="sueta-afisha-date").text
        item_title = item.find(class_="sueta-afisha-title").text
        item_content = item.find(class_="sueta-afisha-description").text
        item_img = "https://iceshow-perm.ru/" + str(item.find("img").get("src"))
        item_date = item_date.split(",")

        dict_event['title'] = item_title
        dict_event['date'] = item_date[0]
        dict_event['content'] = item_content
        dict_event['img'] = item_img
        dict_event['location'] = item_date[1]

        all_event_list.append(dict_event)

    return all_event_list