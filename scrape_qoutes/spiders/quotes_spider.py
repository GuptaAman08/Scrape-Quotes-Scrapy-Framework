import scrapy
from ..items import ScrapeQoutesItem
from scrapy.http import FormRequest

class ScrapeQuotes(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "http://quotes.toscrape.com/login",
    ]
    
    # submitting a form on the website and passing the resultant repsonse to start_scraping_quotes function.
    def parse(self, response):
        token = response.css('form input::attr(value)').extract_first()
        return FormRequest.from_response(response, formdata={
            'csrf_token': token,
            'username': "abc",
            'password': "123"
        }, callback=self.start_scraping_quotes)

    # Fetch the required attributes
    def start_scraping_quotes(self, response):
        items = ScrapeQoutesItem()
        all_div = response.css("div.quote")

        for quote in all_div:
            title = quote.css(".text::text").extract()
            author = quote.css(".author::text").extract()
            tag = quote.css(".tag::text").extract()

            items["title"] = title
            items["author"] = author
            items["tag"] = tag

            yield items

