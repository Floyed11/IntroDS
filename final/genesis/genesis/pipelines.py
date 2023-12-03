# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv


class GenesisPipeline:
    file_name = './spec_cfp2017_1.csv'
    file = None

    def process_item(self, item, spider):
        # print('pipelines item =', item)
        writer = csv.writer(self.file)
        writer.writerow([item['test_sponsor'], item['cpu_name'], item['max_mhz'], item['nominal'], item['oderable'], item['cache_l1'], item['cache_l2'], item['cache_l3'], item['cache_other'], item['memory'], item['storage'], item['hardware_other'],
                         item['os'], item['compiler'], item['firmware'], item['file_sys'], item['sys_state'], item['base_pointers'], item['peak_pointers'], item['software_other'], item['power_management'],
                         item['parallel'], item['base_threads'], item['enable_cores'], item['enable_chips'], item['threads_core'], item['base_results'], item['peak_results']])
        return item
    
    def open_spider(self, spider):
        self.file = open(self.file_name, 'a', newline='', encoding='utf-8')
        writer = csv.writer(self.file)
        writer.writerow(['Test Sponsor', 'Cpu Name', 'Max MHz', 'Nominal', 'Oderable', 'Cache L1', 'L2', 'L3', 'Cache Other', 'Memory', 'Storage', 'Hardware Other',
                     'OS', 'Compiler', 'Firmware', 'File System', 'System State', 'Base Pointers', 'Peak Pointers', 'Software Other', 'Power Management',
                     'Paralled', 'Base Threads', 'Enabled Cores', 'Enabled Chips', 'Threads/Core', 'Base Results', 'Peak Results']) # write header

    def close_spider(self, spider):
        self.file.close()
