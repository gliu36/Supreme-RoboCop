from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup
import re
import json

def findItem(category, keyWords):
    url = "https://www.supremenewyork.com/mobile/#categories/"
    uCLient = uReq(url)
    page_html = uCLient.read()
    uCLient.close()
    soup = BeautifulSoup(page_html, "html.parser")
    pattern = re.compile(r"var allCategoriesAndProducts = (.*?);")
    script = soup.find("script", text=pattern)
    items = pattern.search(script.text).group(1)
    json_stringify = json.loads(items)
    category = json_stringify["products_and_categories"][category]

    #for item in category:



    prettyPrint = json.dumps(category, indent=4)
    return prettyPrint

keyWords = ["Striped"]
print(findItem("Tops/Sweaters", keyWords))
