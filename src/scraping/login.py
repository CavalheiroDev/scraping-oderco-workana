from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_binary


def loggingSite(cnpj: str, password: str):
    browser = webdriver.Chrome()
    browser.get('https://www.oderco.com.br/')
    try:
        WebDriverWait(browser, 60).until(
            EC.presence_of_element_located((By.ID, 'authorization-trigger')))
        browser.find_element_by_id('authorization-trigger').click()

        cnpjLogin = browser.find_element_by_id('cnpj')
        cnpjLogin.clear()
        cnpjLogin.send_keys(cnpj)

        passLogin = browser.find_element_by_id('pass')
        passLogin.clear()
        passLogin.send_keys(password)

        buttonLogin = browser.find_element_by_css_selector('[type=submit]')
        buttonLogin.click()
    finally:
        print('Ta logado, meu bom!')