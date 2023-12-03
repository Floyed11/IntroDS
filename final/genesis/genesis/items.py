# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GenesisItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 28 项
    test_sponsor = scrapy.Field()
    cpu_name = scrapy.Field()
    max_mhz = scrapy.Field()
    nominal = scrapy.Field()
    oderable = scrapy.Field()
    cache_l1 = scrapy.Field()
    cache_l2 = scrapy.Field()
    cache_l3 = scrapy.Field()
    cache_other = scrapy.Field()
    memory = scrapy.Field()
    storage = scrapy.Field()
    hardware_other = scrapy.Field()
    os = scrapy.Field()
    compiler = scrapy.Field()
    firmware = scrapy.Field()
    file_sys = scrapy.Field()
    sys_state = scrapy.Field()
    base_pointers = scrapy.Field()
    peak_pointers = scrapy.Field()
    software_other = scrapy.Field()
    power_management = scrapy.Field()
    parallel = scrapy.Field()
    base_threads = scrapy.Field()
    enable_cores = scrapy.Field()
    enable_chips = scrapy.Field()
    threads_core = scrapy.Field()
    base_results = scrapy.Field()
    peak_results = scrapy.Field()
