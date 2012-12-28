import os
from os import path
from datetime import datetime
from scrapy import log


class ProxyCrawlerPipeline(object):
    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings['PROXY_CHECK_TIMEOUT'] or 10.0,
                   crawler.settings['PROXY_CHECK_THREADS'] or 50,
                   crawler.settings['PROXY_RESULTS_FILE'] or None)

    def __init__(self, timeout = 1.0, check_threads = 50, result_file = None):
        if not result_file:
            res_dir = path.join(path.dirname(__file__), 'results')
            self._res_filename = path.join(res_dir,  datetime.today().strftime('proxies_%Y_%m_%d_%H_%M.lst'))
            if path.exists(self._res_filename):
                os.remove(self._res_filename)
                log.msg("Remove previously created %s" % self._res_filename, log.WARNING)
        else:
            self._res_filename = result_file

        self._out_file = open(self._res_filename, 'a')
        log.msg("Will write extracted addresses to %s" % self._res_filename, log.INFO)

        self._timeout = timeout
        log.msg("Connection timeout is %s" % self._timeout, log.INFO)

    def process_item(self, item, spider):
        log.msg("Gonna write %s" % item['address'], log.DEBUG)
        print >> self._out_file, item['address']

    def close_spider(self, spider):
        self._out_file.flush()
        self._out_file.close()
