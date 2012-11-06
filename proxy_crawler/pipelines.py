import os
from os import path
from datetime import datetime
import requests
from scrapy import log
import threading


class ProxyCrawlerPipeline(object):
    def __init__(self):
        res_dir = path.join(path.dirname(__file__), 'results')
        self._res_filename = path.join(res_dir,  datetime.today().strftime('proxies_%Y_%m_%d_%H_%M.lst'))
        if path.exists(self._res_filename):
            os.remove(self._res_filename)
        self._out_file = open(self._res_filename, 'a')
        self._write_lock = threading.RLock()

    def process_item(self, item, spider):
        if self.test_proxy(item['address']):
            with self._write_lock:
                print >> self._out_file, item['address']

    def test_proxy(self, proxy):
        try:
            resp = requests.head('http://ya.ru', proxies = { 'http': proxy })
            return resp.status_code < 400;
        except Exception as ex:
            log.msg(ex, log.WARNING)
            return False

    def close_spider(self, spider):
        self._out_file.flush()
        self._out_file.close()
