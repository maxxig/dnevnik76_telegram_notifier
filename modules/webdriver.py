import time
from datetime import datetime
from itertools import islice
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup

RU_MONTH_VALUES = {
    'января': 1,
    'февраля': 2,
    'марта': 3,
    'апреля': 4,
    'мая': 5,
    'июня': 6,
    'июля': 7,
    'августа': 8,
    'сентября': 9,
    'октября': 10,
    'ноября': 11,
    'декабря': 12,
}

def init_webdrv():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def replace_month_in_date(item):
    # strptime not work, fix
    for k, v in RU_MONTH_VALUES.items():
        item = item.replace(k, str(v))
    return item

def login_to_dnevnik76(driver, login, password, logger):
    driver.get('https://my.dnevnik76.ru/accounts/login/')
    time.sleep(3)
    element = driver.find_element(By.XPATH, "//div[contains(@class,'custom-select__selected')]")
    element.click()
    time.sleep(3)
    element = driver.find_element(By.XPATH, "//div[contains(@data-value,'76000001000/3')]")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    element.click()
    time.sleep(3)
    element = driver.find_element(By.XPATH, "(//div[contains(@class,'custom-select__selected')])[2]")
    element.click()
    time.sleep(3)
    element = driver.find_element(By.XPATH, "//div[contains(@data-value,'760218')]")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(2)
    element.click()
    time.sleep(1)
    element = driver.find_element(By.XPATH, "//div[contains(@id,'continue-button')]")
    element.click()
    time.sleep(1)
    element = driver.find_element(By.XPATH, "//input[contains(@id,'id_fake_username')]")
    element.send_keys(login)
    element = driver.find_element(By.XPATH, "//input[contains(@id,'id_password')]")
    element.send_keys(password)
    element = driver.find_element(By.XPATH, "//input[@type='submit']")
    element.click()
    time.sleep(2)
    return driver

def get_timetable(driver):
    driver.get('https://my.dnevnik76.ru/homework/')
    time.sleep(1)
    element = driver.find_element(By.XPATH, "//select[contains(@id,'items_perpage')]")
    element.click()
    element = driver.find_element(By.XPATH, "//select[contains(@id,'items_perpage')]//option[contains(@value,'50')]")
    element.click()
    time.sleep(1)
    table = driver.find_element(By.XPATH, "//table[contains(@class,'list mtop')]/tbody")
    table_data = [[cell.text for cell in row("td")] for row in BeautifulSoup(table.get_attribute("outerHTML"), features="html.parser")("tr")]
    table_data = list(filter(lambda y: y[2] != '- ' and len(y[2].strip())>1, list(
        map(lambda x: [datetime.strptime(replace_month_in_date(x[0]), '%d %m %Y г.').strftime('%d.%m.%Y'), x[2], x[3]], table_data))))
    timetable_dict = {}
    for item in table_data:
        if item[0] not in timetable_dict:
            timetable_dict[item[0]] = {item[1]: item[2]}
        elif item[1] not in timetable_dict[item[0]]:
            timetable_dict[item[0]][item[1]] = item[2]
        else:
            timetable_dict[item[0]][item[1]] += ', '+item[2]

    timetable_dict = dict(islice(timetable_dict.items(), 3))
    return timetable_dict, driver