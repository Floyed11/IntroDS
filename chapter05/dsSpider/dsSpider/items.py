# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DsspiderHomeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    info = scrapy.Field()
    group = scrapy.Field()
    recommend = scrapy.Field()
    new = scrapy.Field()

class DsspiderBookItem(scrapy.Item):
    name = scrapy.Field()
    writer = scrapy.Field()
    price = scrapy.Field()
    picture = scrapy.Field()
    publisher = scrapy.Field()

