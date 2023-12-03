import scrapy
from genesis.items import GenesisItem
from scrapy import Selector, Request

MAX_ENTRIES = 10000

class SpecSpider(scrapy.Spider):
    name = "spec"
    # allowed_domains = ["www.spec.org"]
    start_urls = ['https://www.spec.org/cpu2017/results/cfp2017.html']

    def parse(self, response):
        selector = Selector(response)
        infos = selector.xpath("//tbody")
        for info in infos:
            # print("info = ", info)
            for n in range(MAX_ENTRIES):
                try:
                    item = GenesisItem()
                    item["test_sponsor"] = info.xpath('tr[{}]/td[1]/text()'.format(n)).extract_first()
                    sysname_html = info.xpath('tr[{}]/td[2]/span/a[1]/@href'.format(n)).extract_first()
                    # print("sysname_html = ", sysname_html)
                    item["parallel"] = info.xpath('tr[{}]/td[3]/text()'.format(n)).extract_first()
                    # print("parallel = ", item["parallel"])
                    item["base_threads"] = info.xpath('tr[{}]/td[4]/text()'.format(n)).extract_first()
                    # print("base_threads = ", item["base_threads"])
                    item["enable_cores"] = info.xpath('tr[{}]/td[5]/text()'.format(n)).extract_first()
                    # print("enable_cores = ", item["enable_cores"])
                    item["enable_chips"] = info.xpath('tr[{}]/td[6]/text()'.format(n)).extract_first()
                    # print("enable_chips = ", item["enable_chips"])
                    item["threads_core"] = info.xpath('tr[{}]/td[7]/text()'.format(n)).extract_first()
                    # print("threads_core = ", item["threads_core"])
                    item["base_results"] = info.xpath('tr[{}]/td[8]/text()'.format(n)).extract_first().replace('\xa0','')
                    # print("base_results = ", item["base_results"])
                    item["peak_results"] = info.xpath('tr[{}]/td[9]/text()'.format(n)).extract_first().replace('\xa0','')
                    # print("peak_results = ", item["peak_results"])
                    detail_url = 'https://www.spec.org/cpu2017/results/' + sysname_html 
                    # print("item = ", item)
                    yield scrapy.Request(detail_url, callback=self.getHtml, meta={'item': item})               
                except:
                    print("error in entry", n)

    def getHtml(self, response):
        item = response.meta['item']
        # print("item = ", item)
        selector2 = Selector(response)
        # selector2 = selector.xpath("//table[@class='resultTable']")

        #hardware
        hardware_info = selector2.xpath("//*[@id='Hardware']/tbody")
        item["cpu_name"] = hardware_info.xpath('tr[1]/td/text()').extract_first()
        item["max_mhz"] = hardware_info.xpath('tr[2]/td/text()').extract_first()
        item["nominal"] = hardware_info.xpath('tr[3]/td/text()').extract_first()
        item["oderable"] = hardware_info.xpath('tr[5]/td/text()').extract_first()
        item["cache_l1"] = hardware_info.xpath('tr[6]/td/text()').extract_first()
        item["cache_l2"] = hardware_info.xpath('tr[7]/td/text()').extract_first()
        item["cache_l3"] = hardware_info.xpath('tr[8]/td/text()').extract_first()
        item["cache_other"] = hardware_info.xpath('tr[9]/td/text()').extract_first()
        item["memory"] = hardware_info.xpath('tr[10]/td/text()').extract_first()
        item["storage"] = hardware_info.xpath('tr[11]/td/text()').extract_first()
        item["hardware_other"] = hardware_info.xpath('tr[12]/td/text()').extract_first()

        #software
        software_info = selector2.xpath("//*[@id='Software']/tbody")
        oslist = software_info.xpath('tr[1]/td//text()').extract()
        item["os"] = ';'.join(oslist)
        cplist = software_info.xpath('tr[2]/td//text()').extract()
        item["compiler"] = ';'.join(cplist)
        item["firmware"] = software_info.xpath('tr[4]/td/text()').extract_first()
        item["file_sys"] = software_info.xpath('tr[5]/td/text()').extract_first()
        item["sys_state"] = software_info.xpath('tr[6]/td/text()').extract_first()
        item["base_pointers"] = software_info.xpath('tr[7]/td/text()').extract_first()
        item["peak_pointers"] = software_info.xpath('tr[8]/td/text()').extract_first()
        item["software_other"] = software_info.xpath('tr[9]/td/text()').extract_first()
        try:
            item["power_management"] = software_info.xpath('tr[10]/td/text()').extract_first()
        except:
            item["power_management"] = 'None'

        
        yield item