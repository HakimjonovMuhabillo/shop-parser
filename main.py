from baseparser import Baseparser
from time import time
from database import DataBase
from mixin import ProductDetailMixins


class TexnomartParser(Baseparser, DataBase, ProductDetailMixins):
    def __init__(self):
        Baseparser.__init__(self)
        DataBase.__init__(self)

        self.create_categories_table()
        self.create_products_table()

    def get_data(self):
        soup = self.get_soup(self.get_html())
        promotions = soup.find('div', class_='swiper-container')
        categories = promotions.find_all('div', class_='swiper-slide')
        for category in categories[:3]:
            category_title = category.find('a').get_text(strip=True)
            category_link = 'https://texnomart.uz/' + category.find('a').get('href')
            self.category_page_parser(category_link, category_title)

    def category_page_parser(self, category_link, category_title):
        soup = self.get_soup(self.get_html(category_link))
        catalog = soup.find('div', class_='catalog-content__products')

        products = catalog.find_all('div', class_='col-3')

        category_id = self.get_category_id(category_title)
        for product in products[:1]:
            product_title = product.find('div', class_='product-bottom__left').get_text(strip=True)
            print(product_title)
            product_price = product.find('div', class_='product-price__current').get_text(strip=True)
            print(product_price)
            product_installment_plan = product.find('div', class_='installment-price').get_text(strip=True)
            print(product_installment_plan)
            product_link = self.host + product.find('a', class_='product-link').get('href')
            print(product_link)
            product_soup = self.get_soup(self.get_html(product_link))
            product_detail = self.get_detail(product_soup)
            print(product_detail)
            self.save_product(
                product_title=product_title,
                product_price=product_price,
                product_detail=product_detail,
                product_link=product_link,
                product_installment_plan=product_installment_plan,
                category_id=category_id)


def start_parsing():
    parser = TexnomartParser()

    start = time()
    parser.get_data()

    finish = time()
    print(f'Парсер отработал за {finish - start} секунд')


start_parsing()
