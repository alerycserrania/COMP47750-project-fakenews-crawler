import scrapy
import json
import os

class FrancheInfo(scrapy.Spider):
    name = "francheinfo"

    start_urls = [
        f'http://franchetvinfo.fr/catégorie/politique/page/{x}' 
        for x in range(1, 20)
    ]

    def parse(self, response):
        urls = response.css('#content a.post-title::attr(href)').getall()
        for url in urls:
            yield scrapy.Request(url, callback=self.parse_article)

    def parse_article(self, response):
        data = {
            'title': response.css('.post-title::text').get(),
            'author': response.css('.post-author::text').get(),
            'description': None,
            'date': response.css('.post-date::text').get(),
            'content':' '.join(response.css('article .post-content > p *::text').getall())
        }
        with open(os.path.join('francheinfo_data/', response.url.split('/')[-2]) + '.json', 'w', encoding='utf-8') as f:
           json.dump(data, f, ensure_ascii=False)


