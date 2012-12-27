import os
from os import path
from datetime import datetime
import requests
from scrapy import log
import threading


class ProxyCrawlerPipeline(object):
    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings['PROXY_CHECK_TIMEOUT'])
        

    def __init__(self, timeout = 1.0):
        res_dir = path.join(path.dirname(__file__), 'results')
        self._res_filename = path.join(res_dir,  datetime.today().strftime('proxies_%Y_%m_%d_%H_%M.lst'))
        log.msg("Will write extracted addresses to %s" % self._res_filename, log.INFO)
        if path.exists(self._res_filename):
            os.remove(self._res_filename)
            log.msg("Remove previously created %s" % self._res_filename, log.WARNING)
        self._out_file = open(self._res_filename, 'a')
        self._write_lock = threading.RLock()
        self._timeout = timeout
        log.msg("Connection timeout is %s" % self._timeout, log.INFO)

    def process_item(self, item, spider):
        if self.test_proxy(item['address']):
            log.msg("Proxy %s is good!" % item['address'], log.DEBUG)
            with self._write_lock:
                print >> self._out_file, item['address']

    def test_proxy(self, proxy):
        try:
            log.msg("Checking proxy %s" % proxy, log.DEBUG)
            resp = requests.head('http://ya.ru', proxies = { 'http': proxy }, timeout = self._timeout)
            return resp.status_code < 400
        except Exception as ex:
            log.msg(ex, log.WARNING)
            return False

    def close_spider(self, spider):
        self._out_file.flush()
        self._out_file.close()
