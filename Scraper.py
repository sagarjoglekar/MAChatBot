from bs4 import BeautifulSoup
from bs4.element import Comment
import requests as rq
import urllib2


class Scraper:
	maxLength = None
	def __init__(self,maxLength = None):
		if maxLength != None:
			self.maxLength = maxLength

	def tag_visible(self, element):
	    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
	        return False
	    if isinstance(element, Comment):
	        return False
	    return True

	def text_from_html(self,body):
	    soup = BeautifulSoup(body, 'html.parser')
	    texts = soup.findAll(text=True)
	    visible_texts = filter(self.tag_visible, texts)  
	    return u" ".join(t.strip() for t in visible_texts)

	def scrape(self, url):
		page = urllib2.urlopen(url)
		text = self.text_from_html(page)
		return text
	
	def extractLogo(self, url):
		soup = BeautifulSoup(urllib2.urlopen(url).read(), 'html.parser')
		urls = ''
		print '=================== \n'
		results = soup.find_all(id='logo')
		print str(results) + '\n=============='
		for x in results:
			try:
				if x.name == 'img':
					urls += x['src']
			except:pass
		return urls
		
