class ProductDetailMixins:
    def get_detail(self, soup):
        detail = soup.find('div', class_='product__characteristic').get_text()
        return detail