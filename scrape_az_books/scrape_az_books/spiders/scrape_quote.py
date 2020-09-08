# -*- coding: utf-8 -*-
import scrapy


class ScrapeQuoteSpider(scrapy.Spider):
    name = 'scrape_quote'
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        all_div = response.css("div.quote")

        for quote in all_div:
            title = quote.css(".text::text").extract()
            author = quote.css(".author::text").extract()
            tag = quote.css(".tag::text").extract()

            yield {
                "title": title,
                "author": author,
                "tag": tag
            }
