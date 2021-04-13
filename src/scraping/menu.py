from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from bs4 import BeautifulSoup
import chromedriver_binary


def getLinkMenu():

    browser = webdriver.Chrome()
    try:
        browser.get('https://www.oderco.com.br/')
        WebDriverWait(browser, 60).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, '.groupdrop-link > li > a'))
        )
        html = browser.page_source
        soap = BeautifulSoup(html, 'html.parser')
        menuItems = soap.select('.groupdrop-link > li > a')
        linksMenu = list(map(lambda item: item.get('href'), menuItems))
        print(linksMenu)
    finally:
        print('Pegamos os links dos menu')
        return linksMenu


getLinkMenu()
