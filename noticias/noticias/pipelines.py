# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
#from itemadapter import ItemAdapter
import mysql.connector
import json
import csv

class NoticiasPipeline(object):
  def __init__(self):
        # self.conn = MySQLdb.connect('host', 'user', 'passwd', 
        #                             'dbname', charset="utf8",
        #                             use_unicode=True)
        self.mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="example",
                    database="noticias"
                  )
        self.cursor = self.mydb.cursor()

  def process_item(self, item, spider):    
      
    self.cursor.execute("""INSERT INTO noticias (title, author, text, link, source)  
                VALUES (%s, %s, %s, %s, %s)""", 
                (item['title'].encode('utf-8'), 
                item['author'].encode('utf-8'),
                item['text'].encode('utf-8'),
                item['link'].encode('utf-8'),
                item['source'].encode('utf-8')))            
    self.mydb.commit()
    return item         
      
  
#class NoticiasPipeline(object):
    # #def open_spider(self, spider):
    #   #self.file = open('notices.txt', 'w')
    # def close_spider(self, spider):
    #   self.file.close()

    # def process_item(self, item, spider):
    #   print(item)
    #   #line = json.dumps(dict(item)) + '\n'
    #   #line = csv.writer(item)
    #   #self.file.write(line)
    #   return item
