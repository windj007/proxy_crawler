from os import path
from datetime import datetime

class ProxyCrawlerPipeline(object):
    def __init__(self):
        res_dir = path.join(path.dirname(__file__), 'results')
        out_file_path = path.join(res_dir,  datetime.today().strftime('proxies_%Y_%m_%d.lst'))
        print out_file_path
        self._res_file = open(out_file_path, 'w')

    def process_item(self, item, spider):
        print >> self._res_file, item['address']
