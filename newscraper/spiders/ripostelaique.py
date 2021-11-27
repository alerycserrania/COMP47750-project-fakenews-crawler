import scrapy
import json
import os

class RiposteLaique(scrapy.Spider):
    name = "ripostelaique"

    start_urls = [
        f'https://ripostelaique.com/category/collabos/page/{x}' 
        for x in range(1, 30)
    ]

    def parse(self, response):
        urls = response.css('#main-content article .entry-title a::attr(href)').getall()
        for url in urls:
            yield scrapy.Request(url, callback=self.parse_article)

    def parse_article(self, response):
        date = response.url.split('/')[-1].split('-')[-1]
        data = {
            'title': response.css('h1.entry-title::text').get(),
            'author': response.css('.entry-meta-author a::text').get(),
            'description': None,
            'date': response.css('.entry-meta-date a::text').get(),
            'content':' '.join(response.css('#main-content article.post .entry-content p *::text').getall())
        }
        with open(os.path.join('ripostelaique_data/', response.url.split('/')[-1]) + '.json', 'w', encoding='utf-8') as f:
           json.dump(data, f, ensure_ascii=False)


