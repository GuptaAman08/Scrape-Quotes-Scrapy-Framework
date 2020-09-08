# -*- coding: utf-8 -*-
import scrapy
from ..items import ScrapeAzBooksItem

from pprint import pprint

class AzSpiderSpider(scrapy.Spider):
    name = 'az_spider'
    start_urls = [
        "https://www.amazon.co.uk/Best-Sellers-Books/zgbs/books"
    ]

    def parse(self, response):
        items = ScrapeAzBooksItem()

        
        items["image_urls"] = response.css(".a-spacing-small img::attr(src)").extract()
        items["title"] = response.css(".p13n-sc-truncated").extract()
        items["author"] = response.xpath("//*[@id='zg-ordered-list']/li[1]/span/div/span/div[1]/a/text()").extract()
        items["price"] = response.css(".p13n-sc-price , .a-size-small+ .a-row span.p13n-sc-price::text").extract()

        yield items

        print(items.images)
        # coupon_code = response.css(".get-offer-code::attr(data-offer-value)").extract()
        # coupon_txt = response.css(".offer-get-code-link::attr(data-offer-value)").extract()
        # pprint(coupon_code)
        # pprint(coupon_txt)
        # yield {
        #     "coupon_code": coupon_code,
        #     "coupon_txt": coupon_txt
        # }