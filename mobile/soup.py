from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup
import re
import json
from selenium import webdriver

def getHTML(url):
    uCLient = uReq(url)
    page_html = uCLient.read()
    uCLient.close()
    return BeautifulSoup(page_html, "html.parser")

def findItemId(category, keyWords):
    url = "https://www.supremenewyork.com/mobile/#categories/"
    soup = getHTML(url)
    pattern = re.compile(r"var allCategoriesAndProducts = (.*?);")
    script = soup.find("script", text=pattern)
    items = pattern.search(script.text).group(1)
    json_stringify = json.loads(items)
    category = json_stringify["products_and_categories"][category]

    for item in category:
        name = item["name"]
        for key in keyWords:
            if key in name:
                return [item["name"], item["id"]]

def addToCart(id):
    url = "http://www.supremenewyork.com/mobile/#products/" + id
    path = r"C:\Users\gerry\Documents\SUPREME\python\chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.get(url)


     #prettyPrint = json.dumps(category, indent=4)
     #return prettyPrint

keyWords = ["Striped"]


item = findItemId("Tops/Sweaters", keyWords)
print("Matched with: \"" + str(item[0]) + "\" with id: " + str(item[1]))
print(addToCart(str(item[1])))

