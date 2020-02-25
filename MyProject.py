import scrapy
class NewSpider(scrapy.Spider):
    name = "User_spider"
    start_urls = ['http://172.17.50.43/spicyx']
    def parse(self, response):
        css_sel = 'img' #xpath sel = '//img'
        for x in response.css(css_sel):
    #   for x in response.xpath (xpath_sel):
            newpathsel = '@src'
            yield {
                'IMAGE link': x.xpath(newpathsel) .extract_first()
            }
        next_sel = '.next a::attr(href)'
        next_page = response.css(next_sel).extract_first()
        if next_page: #not last page
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )