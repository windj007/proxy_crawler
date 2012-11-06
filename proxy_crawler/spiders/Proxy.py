from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from proxy_crawler.items import ProxyItem
import re


class ProxySpider(CrawlSpider):
    name = 'Proxy'
    start_urls = ['http://www.google.com/search?q=%2B%C3%A2%E2%82%AC%C2%9D%3A8080%C3%A2%E2%82%AC%C2%B3+%2B%C3%A2%E2%82%AC%C2%9D%3A3128%C3%A2%E2%82%AC%C2%B3+%2B%C3%A2%E2%82%AC%C2%9D%3A80%C3%A2%E2%82%AC%C2%B3+filetype%3Atxt#sclient=psy&q=%2B%E2%80%9D:8080%E2%80%B3+%2B%E2%80%9D%3A3128%E2%80%B3+%2B%E2%80%9D%3A80%E2%80%B3+filetype%3Atxt&aq=f&aqi=&aql=&oq=%2B%E2%80%9D:8080%E2%80%B3+%2B%E2%80%9D%3A3128%E2%80%B3+%2B%E2%80%9D%3A80%E2%80%B3+filetype%3Atxt&fp=1&cad=b&sei=gICTUPX5M6jP4QSEwIGwAQ&bav=on.2,or.r_gc.r_pw.r_qf.&sei=OoOTUJyZI8iA4gS1xYGABA']
    _address_re = re.compile(r'(\d{1,4}\.\d{1,4}\.\d{1,4}\.\d{1,4})[^0-9]+(\d+)')
    
    rules = (
        Rule(SgmlLinkExtractor(restrict_xpaths = '//h3[@class="r"]/a/@href'), callback='parse_list', follow=True),
    )

    def parse_list(self, response):
        ip_re = re.compile
        for row in ip_re.finditer(ip_re, response.body):
            res = ProxyItem()
            res['address'] = '%s:%s' % tuple(row.groups())
            yield res
