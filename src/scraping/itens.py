from menu import getLinkMenu
from bs4 import BeautifulSoup


def getItensInPage(html):
    try:
        soap = BeautifulSoup(html, 'html.parser')
        itens = soap.select('.product-item-link')
        linkItens = list(map(lambda item: item.get('href'), itens))
    finally:
        print('Os links dos itens foram pegos')
        return linkItens
