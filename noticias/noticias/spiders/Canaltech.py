import scrapy
from noticias.items import CanalItem

class CanaltechSpider(scrapy.Spider):
    name = 'Canaltech'
    allowed_domains = ['canaltech.com.br']
    start_urls = ['http://canaltech.com.br/ultimas']

    def parse(self, response):
      for article in response.css("article"):
        link    = article.css("a::attr(href)").extract_first()
        
        yield response.follow(link, self.parse_article)

    def parse_article(self, response):
      link   = response.url
      title  = response.css("a h3.titulo-listagem ::text").extract_first()
      author = response.css("a span.catag ::text").extract_first()
      #text   =  "".join(response.css("a span.catag ::text").extract())
      text = ""
      source = "CanalTech"
      if title is None:
        title = ""
      if author is None:
        author = "" 
      if text is None:
        text = ""  

      notice = CanalItem(title=title, author=author, text=text, link=link, source=source)
      yield notice
