import os
from os import path
from datetime import datetime
import requests
from scrapy import log

class ProxyCrawlerPipeline(object):
    def __init__(self):
        res_dir = path.join(path.dirname(__file__), 'results')
        self._res_filename = path.join(res_dir,  datetime.today().strftime('proxies_%Y_%m_%d_%H_%M.lst'))
        if path.exists(self._res_filename):
            os.remove(self._res_filename)

    def process_item(self, item, spider):
        if self.test_proxy(item['address']):
            with open(self._res_filename, 'a') as out_file:
                print >> out_file, item['address']

    def test_proxy(self, proxy):
        try:
            resp = requests.head('http://google.com', proxies = { 'http': proxy })
            return resp.status_code < 400;
        except Exception as ex:
            log.msg(ex, log.WARNING)
            return False