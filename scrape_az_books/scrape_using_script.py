from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

process = CrawlerProcess(get_project_settings())


process.crawl('az_spider')
process.crawl('scrape_quote')
process.start()
process.stop()