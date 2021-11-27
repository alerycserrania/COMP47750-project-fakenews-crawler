import scrapy
import json
import os

class NouvelObs(scrapy.Spider):
    name = "nouvelobs"

    start_urls = [
        f'https://www.nouvelobs.com/election-presidentielle-2022/page/{x}' 
        for x in range(2, 15)
    ]

    def parse(self, response):
        urls = response.css('.list-article a.listArticle-title::attr(href)').getall()
        for url in urls:
            yield scrapy.Request(url, callback=self.parse_article)

    def parse_article(self, response):
        data = {
            'title': response.css('.article-page__title::text').get(),
            'author': response.css('.article-page__published .author::text').get(),
            'description': ' '.join(response.css('.article-page__chapo *::text').getall()),
            'date': response.url.split('/')[-2],
            'content':' '.join(response.css('.article-page__body-content p *::text').getall())
        }
        with open(os.path.join('nouvelobs_data/', response.url.split('/')[-1]) + '.json', 'w', encoding='utf-8') as f:
           json.dump(data, f, ensure_ascii=False)


