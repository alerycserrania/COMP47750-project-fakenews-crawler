import json
import csv
import os

sources = [
    ('lefigaro', 'r'),
    ('legorafi', 'f'),
    ('lemonde', 'r'),
    ('mediaspress', 'f'),
    ('nouvelobs', 'r'),
    ('ripostelaique', 'f'),
    ('francheinfo', 'f')
]

output = open('data.csv', 'w', newline='', encoding='utf-8')
writer = csv.writer(output, quoting=csv.QUOTE_ALL,)
writer.writerow(['title', 'author', 'source', 'fake or real', 'description', 'date', 'content'])

for source, f_or_r in sources:
    for file in os.listdir(source + '_data'):
        with open(os.path.join(source + '_data', file), 'r', encoding='utf-8') as f:
            data = json.loads(f.read())
            writer.writerow([
                data['title'],
                data['author'],
                source,
                f_or_r,
                data['description'],
                data['date'],
                data['content']
            ])


output.close()