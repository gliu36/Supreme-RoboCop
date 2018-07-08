from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import re
import json

def findItem(keywords, color, size, category):
    path = r"C:\Users\gerry\Documents\SUPREME\python\chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.get("http://www.supremenewyork.com/shop/all/" + category)
    items_element = driver.find_elements_by_class_name("name-link")
    items = [x.text for x in items_element]

    text = items[0::2]
    colors = items[1::2]
    links = []
    for item in items_element:
        links.append(item.get_attribute('href'))
    links = links[0::2]

    catalog = {}
    count = 0;
    for t, c, l in zip(text, colors, links):
        catalog["item " + str(count)] = {}
        catalog["item " + str(count)] = ({
            'name': t,
            'color': c,
            'link': l
        })
        count += 1

  #  catalog_json = json.dumps(catalog, indent=4)

    matched_item = ""

    for key, value in catalog.items():
        for word in keywords:
            if word in value["name"] and color in value["color"]:
                matched_item = catalog[key]
                break

    print(matched_item)
    return driver


keywords = ["Striped"]
color = "Red"
size = "Large"
category = "tops_sweaters"

d = findItem(keywords, color, size, category)