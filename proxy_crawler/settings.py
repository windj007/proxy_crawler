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
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.79 Safari/537.1'

ITEM_PIPELINES = [
    'proxy_crawler.pipelines.ProxyCrawlerPipeline'
]

LOG_ENABLED = True
LOG_FILE = 'proxy.log'
#LOG_LEVEL = 'WARNING'

DOWNLOAD_DELAY = 0.25