import scrapy
from scrapy import Request
from scrapy.http import FormRequest
# from scrapy.utils.response import open_in_browser
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings as settings
listLinkMatkuls=None
listMatkuls=None
count=0
# from ..items import Quotetu
class SpotScrap(scrapy.Spider):
    name = 'spotscrap'
    start_urls = [u"https://sso.upi.edu/cas/login?service=https%3A%2F%2Fspot.upi.edu%2Fberanda"]

    def parse(self, response):
        global udah
        values = response.css('form input::attr(value)')[2].extract()
        token = values
        udah=True
        return FormRequest.from_response(response, formdata={
            "value": str(token),
            "username": "2205965",
            "password": "46ddfdb"
        }, callback=self.start_scraping)

    def start_scraping(self, response):
        global listLinkMatkuls, listMatkuls
        user = response.css('aside.sidebar p::text').extract()
        listLinkMatkuls = response.css('table.tablesaw.table-hover.table a::attr(href)').extract()
        listMatkuls = response.css('table.tablesaw.table-hover.table a::text').extract()
        file = open(f"{user[1]} -{user[0]}.txt", "w")
        idx=[]
        print("\n\n"+str(listLinkMatkuls)+"\n\n")
        print(u"https://spot.upi.edu"+listLinkMatkuls[0])
        udah=False

        yield response.follow(listLinkMatkuls[0], callback=self.scrape_matkul)

        # for i in listMatkuls:
        #     idx.append(i)
        #     file.write(f"{i}.,.{listLinkMatkuls[len(idx)-1]}\n")
        # file.close()

    def scrape_matkul(self, response):
        global listLinkMatkuls, listMatkuls, count
        count+=1
        listLinkPertemuan=response.css('div.col-md-6 a::attr(href)').extract()
        print(str(listLinkPertemuan)+"\n\n")
        requests = []
        if count < len(listLinkMatkuls):
            yield response.follow(listLinkMatkuls[count], callback=self.scrape_matkul)






if __name__ == "__main__":
    process = CrawlerProcess(settings())
    process.crawl(SpotScrap)
    process.start()

