# Scrapy settings for proxy_crawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'proxy_crawler'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['proxy_crawler.spiders']
NEWSPIDER_MODULE = 'proxy_crawler.spiders'
USER_AGENT = 'w3m/0.5.3+cvs-1.1055' 


ITEM_PIPELINES = [
    'proxy_crawler.pipelines.ProxyCrawlerPipeline'
]
CONCURRENT_ITEMS = 100

LOG_ENABLED = True
LOG_FILE = 'proxy.log'
LOG_LEVEL = 'INFO'

DOWNLOAD_DELAY = 0.25

PROXY_CHECK_TIMEOUT=5.0