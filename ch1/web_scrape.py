from lxml import html
import requests

page = requests.get('https://github.com/pricing/')
tree = html.fromstring(page.content)
print("Page Object: {}".format(tree))
plans = tree.xpath('//h2[@class="princing-card-name alt-h3"]/text()')
pricing = tree.xpath('//span[@class="default-currency"]/text()')
print("Plans: {} nPricing: {}".format(plans, pricing))