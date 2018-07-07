from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

def findItem(keywords, color, size, category):
    path = r"C:\Users\gerry\Documents\SUPREME\python\chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.get("http://www.supremenewyork.com/shop/all/" + category)
    items_element = driver.find_elements_by_class_name("name-link")
    items = [x.text for x in items_element]
    print(items)
    return driver

keywords = ["Striped"]
color = "Red"
size = "Large"
category = "tops_sweaters"

d = findItem(keywords, color, size, category)





