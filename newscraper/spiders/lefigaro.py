import scrapy
import json
import os

class LeFigaro(scrapy.Spider):
    name = "lefigaro"

    start_urls = [
        f'https://www.lefigaro.fr/elections/presidentielles?page={x}' 
        for x in range(2, 10)
    ] + [
        f'https://www.lefigaro.fr/politique?page={x}'
        for x in range(2, 10)
    ]

    def parse(self, response):
        urls = response.css('.fig-main-col .fig-profile__link::attr(href)').getall()
        for url in urls:
            yield scrapy.Request(url, callback=self.parse_article)

    def parse_article(self, response):
        date = response.url.split('/')[-1].split('-')[-1]
        data = {
            'title': response.css('.fig-headline::text').get(),
            'author': response.css('.fig-content-metas__author::text').get(),
            'description': ' '.join(response.css('.fig-standfirst *::text').getall()),
            'date': date[:4] + '-' + date[4:6] + '-' + date[6:],
            'content':' '.join(response.css('.fig-paragraph *::text').getall())
        }
        with open(os.path.join('lefigaro_data/', response.url.split('/')[-1]) + '.json', 'w', encoding='utf-8') as f:
           json.dump(data, f, ensure_ascii=False)


