import requests, json
from bs4 import BeautifulSoup

# url_cinema = "https://afisha.yandex.ru/perm/selections/cinema-today?utm_source=direct_search&utm_medium=paid_performance&utm_campaign=95779077%7CMSCAMP-60_%5BAF-PT%5D_%7BWS%3AS%7D_RU-50_goal-REV_Category-general-Broad-main&utm_term=%D0%BA%D1%83%D0%B4%D0%B0%20%D0%BF%D0%BE%D0%B9%D1%82%D0%B8&utm_content=INTid%7C0100000047072603441_47072603441%7Ccid%7C95779077%7Cgid%7C5283339641%7Caid%7C14993620208%7Cpos%7Cpremium1%7Csrc%7Csearch_none%7Cdvc%7Cdesktop%7Cevid%7C0%7Cretid%7C0"

def parser_iceShow():
    url_icehow = "https://iceshow-perm.ru/"
    
    headers = {
        "Accept":"*/*",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"
        }

    req = requests.get(url=url_icehow, headers=headers)
    src = req.text

    soup = BeautifulSoup(src, "lxml")
    all_class_event = soup.find_all(class_="sueta-afisha-element")

    iceshow_event = []
    for item in all_class_event:
        dict_event = {}
        item_date = item.find(class_="sueta-afisha-date").text
        item_title = item.find(class_="sueta-afisha-title").text
        item_content = item.find(class_="sueta-afisha-description").text
        item_img = "https://iceshow-perm.ru/" + str(item.find("img").get("src"))
        item_date_loc = item_date.split(",")

        dict_event['title'] = item_title
        dict_event['content'] = item_content
        dict_event['image'] = item_img
        dict_event['location'] = item_date_loc[1]

        iceshow_event.append(dict_event)

    return iceshow_event


def parser_kassy():
    url_kassy = "https://perm.kassy.ru/"
    
    headers = {
        "Accept":"*/*",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"
    }
    
    req = requests.get(url=url_kassy, headers=headers)
    src = req.text
    
    soup = BeautifulSoup(src, "lxml")
    all_event = soup.find_all("li")
    
    all_event_list = []
    
    for event in all_event:
        
        all_class_img = event.find_all(class_="img")
        all_class_content = event.find_all(class_="announce")
        
        img_list = []
        for item in all_class_img:
            item_img = "https://perm.kassy.ru" + item.find("img").get("src")
            img_list.append(item_img)
        
        count = 0
        for item in all_class_content:
            data_dict = {}
            item_title = item.find("a").text
            item_href = "https://perm.kassy.ru" + item.find("a").get("href")
            
            data_dict['title'] = item_title
            data_dict['image'] = img_list[count]
            data_dict['href'] = item_href 
            
            all_event_list.append(data_dict)
            
    kassy_event = []
    l = []
    for event in all_event_list:
        req = requests.get(url=event.get('href'), headers=headers)
        src = req.text
        
        soup = BeautifulSoup(src, "lxml")
        
        content = soup.find(class_="fw-light").text
        event['content'] = content
        
        kassy_event.append(event)
        
    for event in all_event_list:
        req = requests.get(url=event.get('href'), headers=headers)
        src = req.text
        
        soup = BeautifulSoup(src, "lxml")
        
        table = soup.find(class_="table repertuar")
        l.append(table)
        for item in l:
            if item == None:
                continue
            else:
                table = item.find("tbody").find_all("tr")
        
        for item in table:
            item_td = item.find("td", class_="descr")
            
            if item_td != None:
                item_loc = item_td.find("a").text
            else:
                continue
            
            event['location'] = item_loc
            
            kassy_event.append(event)

            events = []
            for event in kassy_event:
                if event not in events:
                    events.append(event)
        
    return events

def parser_kinopoisk():
    url = "https://www.kinopoisk.ru/afisha/new/city/432/"
    
    headers = {
        "Accept":"*/*",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"
    }
    
    req = requests.get(url=url, headers=headers)
    src = req.text
    
    soup = BeautifulSoup(src, "lxml")
    all_event_cinema = soup.find(class_="filmsListNew js-rum-hero").find_all(class_="item")
    
    event_afisha = []
    for item in all_event_cinema:
        dict_event = {}
        item_href = "https://www.kinopoisk.ru/afisha/new/city/432/"+item.find(class_="name").find("a").get("href")
        item_img = item.find(class_="poster").find("img").get("src")
        item_title = item.find(class_="name").find("a").text
        item_gray = item.find_next(class_="gray").text
        
        dict_event['title'] = item_title
        dict_event['image'] = item_img
        dict_event['href'] = item_href
        dict_event['content'] = item_gray
        
        event_afisha.append(dict_event)

    events = []
    for event in event_afisha:
        if event not in events:
            events.append(event)
        
    return events

