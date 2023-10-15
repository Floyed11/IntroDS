import scrapy
from dsSpider.items import DsspiderBookItem
from dsSpider.items import DsspiderHomeItem

class DangdangSpider(scrapy.Spider):
    name = "dangdanghome"
    allowed_domains = ["www.dangdang.com"]
    start_urls = ["https://book.dangdang.com/01.54.htm"]

    def parse(self, response):
        filename = "IThome.html"
        with open(filename, 'wb') as f:
            f.write(response.body)

class DangdangbookSpider(scrapy.Spider):
    name = "dangdangbook"
    allowed_domains = ["www.dangdang.com"]
    start_urls = ['http://category.dangdang.com/pg1-cp01.54.00.00.00.00.html']
    items = []

    def parse(self, response):
        #items = DsspiderBookItem()
        #print('\n\nresponse= ',response.xpath('//li').extract(),'\n\n')
        item = DsspiderBookItem()
        for each in response.xpath('//li'):
            try:
                item['name'] = each.xpath('p[@class="name"]/a/text()').extract()[0]
                item['writer'] = each.xpath('p[@class="search_book_author"]/span[1]/a/text()').extract()[0]
                item['price'] = each.xpath('p[@class="price"]/span[@class="search_now_price"]/text()').extract()[0]
                item['publisher'] = each.xpath('p[@class="search_book_author"]/span[3]/a/text()').extract()[0]
                print(item)
                yield item
            except:
                continue

        for i in range(2,10):
            page_url = 'http://category.dangdang.com/pg{}-cp01.54.00.00.00.00.html'.format(i)
            yield scrapy.Request(url = page_url, callback=self.getInfo,dont_filter=True)


    def getInfo(self, response):
        item = DsspiderBookItem()
        print('\n\nthis is getInfo\n\n')
        #print('\n\nresponse= ',response.xpath('//li').extract(),'\n\n')
        for each in response.xpath('//li'):
            try:
                item['name'] = each.xpath('p[@class="name"]/a/text()').extract()[0]
                item['writer'] = each.xpath('p[@class="search_book_author"]/span[1]/a/text()').extract()[0]
                item['price'] = each.xpath('p[@class="price"]/span[@class="search_now_price"]/text()').extract()[0]
                item['publisher'] = each.xpath('p[@class="search_book_author"]/span[3]/a/text()').extract()[0]
                yield item
            except:
                continue