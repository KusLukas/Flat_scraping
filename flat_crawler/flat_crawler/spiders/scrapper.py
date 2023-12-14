import scrapy
import json
#import scrapy_playwright


class ScrapperSpider(scrapy.Spider):
    name = "scrapper"
    allowed_domains = ["sreality.cz"]
    num_of_entries=500
    start_urls = ["https://www.sreality.cz/api/cs/v2/estates?per_page={}".format(num_of_entries)]


    def parse(self, response):
        flat_db = json.loads(response.body)
        flats = flat_db["_embedded"]["estates"]

        for flat_id in flats:
            flat_ref = flat_id["_links"]["self"]["href"]
            try:
                yield scrapy.Request(url="https://www.sreality.cz/api"+flat_ref, callback=self.parse_flat)
            except:
                print("Something went wrong with Request!",flat_ref)
                continue


    def parse_flat(self, response):
        flat_db = json.loads(response.body)
        flats_items = {"Title": flat_db["name"]["value"],
                       "Image_url": flat_db["_embedded"]["images"][0]["_links"]["gallery"]["href"]}
        yield flats_items
