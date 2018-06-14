import requests as rq
import json
import datetime as dt
import Scraper


class gdeltNewsCrawler():

	apiURLdoc = "https://api.gdeltproject.org/api/v2/doc/doc?query=" #api for document queries
	apiURLgeo = "https://api.gdeltproject.org/api/v2/geo/geo?query=" #api for geo queries 
	recordFrag = "maxrecords=" 
	maxRecords = 250 #Number of records per query
	duration = 15 #number of days before today to look for
	sourcecountry = "uk" #country to get articles from

	startDate = None
	endDate = None
	def __init__(self,delta=None):
		if delta!=None:
			self.duration = delta
		
		self.endDate = dt.datetime.strftime(dt.datetime.today(),'%Y%m%d%H%M%S')
		self.startDate = dt.datetime.strftime((dt.datetime.today() - dt.timedelta(days=self.duration)),'%Y%m%d%H%M%S')

	def printDates(self):
		print "crawling for: %s to %s"%(self.startDate,self.endDate)



def test():
	crawler = gdeltNewsCrawler()
	crawler.printDates()


if __name__ == '__main__':
	test()
			

