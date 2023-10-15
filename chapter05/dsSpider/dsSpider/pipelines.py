# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv

class DsspiderPipeline(object):
    file_name = 'dangdangbook.csv'
    file = None


    def open_spider(self, spider):
        self.file = open(self.file_name, 'a', newline='', encoding='utf-8')
        writer = csv.writer(self.file)
        writer.writerow(['书名','作者','价格','出版社'])


    def process_item(self, item, spider):
        writer = csv.writer(self.file)
        writer.writerow([item['name'], item['writer'], item['price'], item['publisher']])
        return item
    
    def close_spider(self, spider):
        self.file.close()
