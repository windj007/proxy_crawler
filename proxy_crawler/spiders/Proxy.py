from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from proxy_crawler.items import ProxyItem
import re

class ProxySpider(CrawlSpider):
    name = 'Proxy'
    allowed_domains = ['spys.ru']
    start_urls = ['http://www.spys.ru/en/']
    _address_re = re.compile(r'\d+\.\d+\.\d+\.\d+\:\d+')
    
    rules = (
        Rule(SgmlLinkExtractor(allow = r'.*'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        for addr in ProxySpider._address_re.findall(response.body):
            yield ProxyItem(addr)
