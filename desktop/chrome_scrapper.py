from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import re
import json
import time

def findItem(keywords, color, category):
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

    return [driver, matched_item]

def addToCart(size, driver):
    sizes = driver.find_elements_by_id("s")
    sizes_element = driver.find_elements_by_tag_name("option")
    sizes = sizes[0].text.split('\n')
    values = []
    for s in sizes_element:
        values.append(s.get_attribute("value"))
    print(sizes)
    print(values)
    select = Select(driver.find_element_by_id("s"))
    for s, value in zip(sizes, values):
        if s == size:
            select.select_by_value(value)
    driver.find_element_by_xpath("""//*[@id="add-remove-buttons"]/input""").click()

def goToCheckout(driver):
    driver.find_element_by_xpath("""//*[@id="cart"]/a[2]""").click()

def autoFill(driver, profile, delay):
    driver.execute_script("document.getElementById('order_billing_name').value =  '" + profile["name"] + "'")
    driver.execute_script("document.getElementById('order_email').value =  '" + profile["email"] + "'")
    driver.execute_script("document.getElementById('order_tel').value =  '" + profile["tel"] + "'")
    driver.execute_script("document.getElementById('bo').value =  '" + profile["address"] + "'")
    driver.execute_script("document.getElementById('oba3').value =  '" + profile["address2"] + "'")
    driver.execute_script("document.getElementById('order_billing_zip').value =  '" + profile["zip"] + "'")
    driver.execute_script("document.getElementById('order_billing_city').value =  '" + profile["city"] + "'")
    driver.execute_script("document.getElementById('order_billing_zip').value =  '" + profile["zip"] + "'")
    Select(driver.find_element_by_id("order_billing_state")).select_by_value(profile["state"])

    driver.execute_script("document.getElementById('nnaerb').value =  '" + profile["card_number"] + "'")
    Select(driver.find_element_by_id("credit_card_month")).select_by_value(profile["card_month"])
    Select(driver.find_element_by_id("credit_card_year")).select_by_value(profile["card_year"])
    driver.execute_script("document.getElementById('orcer').value =  '" + profile["cvv"] + "'")

    driver.find_element_by_xpath("""//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins""").click()
    time.sleep(delay)
    driver.find_element_by_xpath("""//*[@id="pay"]/input""").click()

keywords = ["Striped"]
color = "Brown"
size = "Large"
category = "tops_sweaters"
profile = {
    "name":"Hello Test",
    "email":"test@test.com",
    "tel":"6106106106",
    "address":"123 test dr",
    "address2":"apt 32",
    "zip":"99212",
    "city":"Spokane",
    "state":"WA",
    "country":"USA",
    "card_number":"4196319128375193",
    "card_month":"10",
    "card_year":"2019",
    "cvv":"237"
}
addToCartDelay = 0.25
checkoutDelay = 2

results = findItem(keywords, color, category)

item = results[1]
driver = results[0]

print(json.dumps(item, indent=4))

driver.get(item["link"])
addToCart(size, driver)
time.sleep(addToCartDelay)
goToCheckout(driver)
autoFill(driver, profile, checkoutDelay)

