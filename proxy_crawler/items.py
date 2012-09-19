# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class ProxyItem(Item):
    address = Field()
    
    def __init__(self, addr):
        super(Item, self).__init__()
        self['address'] = addr
