import requests as rq
import json
import datetime as dt
from Scraper import Scraper
import urllib
import sys
from mongoengine import *
sys.path.insert(0,'../')
from storage.data_models import *
from flask import Flask, render_template, request
from flask_cors import CORS

app = Flask(__name__, static_folder='../static', template_folder='../templates')

def connect_to_mongo(IP=None, Port=None):
	if IP==None and Port == None:
		IP = '127.0.0.1'
		Port = 27017

	print('I am connecting to MongoDB ')
	connect('MA_NewsDB', host=IP, port=Port)


def start_server():
    global app
    CORS(app)
    connect_to_mongo()


class gdeltNewsCrawler():

	apiURLdoc = "https://api.gdeltproject.org/api/v2/doc/doc?query=" #api for document queries
	apiURLgeo = "https://api.gdeltproject.org/api/v2/geo/geo?query=" #api for geo queries
	params = {} 
	params['maxrecords'] = "250"
	duration = 7 #number of days before today to look for
	sourcecountry = "uk" #country to get articles from
	savePath = '.'
	params['format']='json' #defaultJson

	startDate = []
	endDate = []
	def __init__(self, maxRecords = None , delta=None , savePath = '.'):
		if maxRecords!=None:
			self.params['maxrecords'] = maxRecords
		self.savePath = savePath
		if delta!=None:
			if delta < self.duration:
				self.endDate = [dt.datetime.strftime(dt.datetime.today(),'%Y%m%d%H%M%S')]
				self.startDate = [dt.datetime.strftime((dt.datetime.today() - dt.timedelta(days=self.duration)),'%Y%m%d%H%M%S')]
			else:
				if delta > 90:
					delta = 90
				#calculate the number of weeks 
				chunks = delta/self.duration + 1
				for k in reversed(range(1,chunks+1)):
					start = dt.datetime.strftime(dt.datetime.today()-dt.timedelta(days=k*7),'%Y%m%d%H%M%S')
					end = dt.datetime.strftime(dt.datetime.today()-dt.timedelta(days=(k-1)*7),'%Y%m%d%H%M%S')
					self.endDate.append(end)
					self.startDate.append(start)

		else:
			self.endDate = [dt.datetime.strftime(dt.datetime.today(),'%Y%m%d%H%M%S')]
			self.startDate = [dt.datetime.strftime((dt.datetime.today() - dt.timedelta(days=self.duration)),'%Y%m%d%H%M%S')]

	def printDates(self):
		for i in range(len(self.startDate)):
			print "crawling for: %s to %s"%(self.startDate[i],self.endDate[i])

	def writeNewstoDb(self,json):
		articles = json['articles']
		for art in articles:
			text = ''
			try:
				print art['url']
				text = self.scrapeNewsText(art['url'])
			except:
				print "scraping failed!! Moving on"
			news = News(domain=art['domain'] , language=art['language'] , title = art['title'] , url = art['url'] , country = art['sourcecountry'] , imageUrl = art['socialimage'] , date = art['seendate'] , text = text)
			news.save()

	def scrapeNewsText(self,url):
		scraper =  Scraper()
		text = scraper.scrape(url)
		return ' '.join(text.split())

	def doQueries(self,topicList,sourcecountry,sourcelang=None):
		if len(topicList) > 1:
			query = "("
			for k in topicList[:-1]:
				query = query + '"' + k + '"' +  " OR "
			query = query + '"' + topicList[-1] + '"' + ")"
		else:
			query = '"' + topicList[0] + '"'

		query = query + " sourcecountry:"+sourcecountry+" sourcelang:"+sourcelang
		self.params['query'] = query

		requestUrls = []
		for i in range(len(self.startDate)):
			requesturl = self.apiURLdoc + self.params['query'] + '&format=' + self.params['format'] + '&maxrecords=' + self.params['maxrecords'] + "&STARTDATETIME=" + self.startDate[i] + "&ENDDATETIME=" + self.endDate[i]
			requestUrls.append(requesturl)
			print requesturl

		for i in range(len(requestUrls)):
			name = str(self.savePath) + "/" + self.startDate[i] + "_" + self.endDate[i] + ".json"
			print name
			url = requestUrls[i]
			r = rq.get(url)
			print r.status_code
			if r.status_code == 200:
				print "Writing Json!"
				self.writeNewstoDb(r.json())
				# with open(name , 'w' ) as f:
				# 	json.dump(r.json() , f)


@app.route("/getnews", methods=['POST'])
def getNews():
    """Respond to incoming calls with a simple text message."""
    print request.form
    keywords = request.form.get('keywords').split(",")
    print len(keywords)
    language = request.form.get('language')
    country = request.form.get('country')
    days = request.form.get('days')
    records = request.form.get('records')

    crawler = gdeltNewsCrawler(maxRecords = records, delta = days, savePath ='../results/')
    crawler.doQueries(keywords,country,language)
    return "Success"
    
def test():
	crawler = gdeltNewsCrawler(maxRecords = 10 , delta = 100 , savePath = 'results/')
	crawler.doQueries(["nigel Farage",'Donald Trump'],'uk','english')




if __name__ == '__main__':
	test()
			

