from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from dotenv import find_dotenv, load_dotenv
from time import sleep
import chromedriver_binary
import os
import csv

load_dotenv(find_dotenv())

CNPJ = os.getenv('CNPJ')
PASS = os.getenv('PASS')

browser = webdriver.Chrome()
browser.get('https://www.oderco.com.br/')

WebDriverWait(browser, 60).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'groupmenu')))

itensMenu = browser.find_elements_by_css_selector(
    '.groupdrop-link > li > a')
linksMenu = list(map(lambda item: item.get_attribute('href'), itensMenu))

for category in linksMenu:
    browser.get(category)
    sleep(3)
    itensPage = browser.find_elements_by_css_selector('.product-item-link')
    linksItens = list(
        map(lambda item: item.get_attribute('href'), itensPage))
    break

WebDriverWait(browser, 60).until(
    EC.presence_of_element_located((By.ID, 'authorization-trigger')))
browser.find_element_by_id('authorization-trigger').click()

cnpjLogin = browser.find_element_by_id('cnpj')
cnpjLogin.clear()
cnpjLogin.send_keys(CNPJ)

passLogin = browser.find_element_by_id('pass')
passLogin.clear()
passLogin.send_keys(PASS)

buttonLogin = browser.find_element_by_css_selector('[type=submit]')
buttonLogin.click()

fild = ['Titulo', 'SKU', 'Preço', 'Marca',
        'Estoque', 'Descrição', 'Peso', 'Largura', 'Altura', 'Filial']
c = open('./data.csv', 'w', encoding='utf-8')
writer = csv.DictWriter(f=c, fieldnames=fild)
writer.writeheader()

for item in linksItens:
    if item:
        browser.get(item)
        sleep(3)
        title = browser.find_element_by_css_selector(
            '.page-title > .base').text
        sku = browser.find_element_by_css_selector('div.value').text
        price = browser.find_element_by_css_selector('.price').text
        marca = browser.find_element_by_css_selector(
            'a[style="color: #005fad !important;"]').text
        stock = browser.find_element_by_css_selector('.stock > span').text
        details = browser.find_element_by_css_selector(
            '.description > .value').text
        weight = browser.find_element_by_css_selector(
            '[data-th="Peso(Kg)"]').text
        width = browser.find_element_by_css_selector(
            '[data-th="Largura"]').text
        height = browser.find_element_by_css_selector(
            '[data-th="Altura"]').text
        filial = browser.find_element_by_css_selector(
            '[data-th="Filial"]').text
        writer.writerow({'Titulo': title, 'SKU': sku,
                        'Preço': price, 'Marca': marca, 'Estoque': stock, 'Descrição': details, 'Peso': weight, 'Largura': width, 'Altura': height, 'Filial': filial})
        break
    else:
        continue
browser.close()
