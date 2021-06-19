from selenium import webdriver
import selenium.common.exceptions
from selenium.webdriver.common.keys import Keys
import time
from pprint import pprint
COST_LIST = {}
BUY = {}

def buy_stuff(driver):
        global COST_LIST
        more_upgrades=True
        # while more_upgrades:
        try:
                current_cookies = int(driver.find_element_by_id("money").text.replace(",",""))
                COST_LIST["cursor"] = int(driver.find_element_by_xpath('//*[@id="buyCursor"]/b').text.split()[-1].replace(",",""))
                COST_LIST["grandma"] = int(driver.find_element_by_xpath('//*[@id="buyGrandma"]/b').text.split()[-1].replace(",",""))
                COST_LIST["factory"] = int(driver.find_element_by_xpath('//*[@id="buyFactory"]/b').text.split()[-1].replace(",",""))
                COST_LIST["mine"] = int(driver.find_element_by_xpath('//*[@id="buyMine"]/b').text.split()[-1].replace(",",""))
                COST_LIST["shipment"] = int(driver.find_element_by_xpath('//*[@id="buyShipment"]/b').text.split()[-1].replace(",",""))
                COST_LIST["alchemy lab"] = int(driver.find_element_by_xpath('//*[@id="buyAlchemy lab"]/b').text.split()[-1].replace(",",""))
                COST_LIST["portal"] = int(driver.find_element_by_xpath('//*[@id="buyPortal"]/b').text.split()[-1].replace(",",""))
                COST_LIST["time machine"] = int(driver.find_element_by_xpath('//*[@id="buyTime machine"]/b').text.split()[-1].replace(",",""))
        except selenium.common.exceptions.StaleElementReferenceException:
                pass

        if current_cookies < min(COST_LIST.values()):
                more_upgrades=False
        else:
                driver.find_element_by_id(BUY[max_value(COST_LIST,current_cookies)]).click()


def max_value(cost_dict, current_cookies):
        current_cost = 0;
        cost_list = [[key,value] for (key,value) in cost_dict.items()]
        for cost in cost_list:
                if cost[1] > current_cost and cost[1]<=current_cookies:
                        buy_key=cost[0]
        return buy_key

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element_by_id("cookie")

BUY["cursor"] = "buyCursor"
BUY["grandma"] = "buyGrandma"
BUY["factory"] = "buyFactory"
BUY["mine"] = "buyMine"
BUY["shipment"] = "buyShipment"
BUY["alchemy lab"] = "buyAlchemy lab"
BUY["portal"] = "buyPortal"
BUY["time machine"] = "buyTime machine"

full_end = time.time() + 60 * 5

# while time.time() < full_end:
while True:
        t_end = time.time() + 60 * 0.1
        while time.time() < t_end:
                cookie.click()

        buy_stuff(driver)
cookies_per_second = driver.find_element_by_id("cps")
print(cookies_per_second.text)

driver.quit()