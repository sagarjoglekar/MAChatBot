import requests as rq
import json
import datetime as dt
import Scraper
import urllib

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
	def __init__(self, delta=None , savePath = '.'):
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
				with open(name , 'w' ) as f:
					json.dump(r.json() , f)



def test():
	crawler = gdeltNewsCrawler(100)
	crawler.doQueries(["nigel Farage",'Donald Trump'],'uk','english')


if __name__ == '__main__':
	test()
			

