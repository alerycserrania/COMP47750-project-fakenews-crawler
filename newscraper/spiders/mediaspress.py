import scrapy
import json
import os

class MediasPress(scrapy.Spider):
    name = "mediaspress"

    start_urls = [
        f'https://www.medias-presse.info/category/politique/page/{x}' 
        for x in range(1, 30)
    ]

    def parse(self, response):
        urls = response.css('#recent-posts .post-content h2 a::attr(href)').getall()
        for url in urls:
            yield scrapy.Request(url, callback=self.parse_article)

    def parse_article(self, response):
        date = response.url.split('/')[-1].split('-')[-1]
        data = {
            'title': response.css('h1.title font::text').get(),
            'author': response.css('.post-meta a[rel=author]::text').get(),
            'description': None,
            'date': response.css('.post-meta *::text').getall()[-1].strip(),
            'content':' '.join(response.css('.post .entry > p *::text').getall())
        }
        with open(os.path.join('mediaspress_data/', response.url.split('/')[-3]) + '.json', 'w', encoding='utf-8') as f:
           json.dump(data, f, ensure_ascii=False)


