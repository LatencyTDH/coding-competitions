from collections import deque
import requests as r
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from pprint import pprint
import logging
import sys
import time

IGNORED_EXTENSIONS = {'.pdf', '.docx'}
logger = logging.getLogger('crawlerApp')
logger.setLevel(logging.INFO)

class Crawler(object):
	def __init__(self):
		self.visited = set()

	def crawl(self, root_url):
		q = set([root_url])
		while q:
			link = q.pop()
			if link in self.visited:
				continue
			print('Currently at url', link)
			links = self.get_links(link)
			self.visited.add(link)

			for url in links:
				if url not in self.visited:
					q.add(url)
			
			print('Sleeping for the next 10 seconds')
			print('Exploration set has size', len(q))
			print()
		return self.visited

	def get_links(self, url, same_domain=True):
		try:
			resp = r.get(url, headers={'Accept-Encoding': 'identity'})
		except Exception as e:
			logging.error("Unable to retrieve content from the URL", e)
			return set()
		bs = BeautifulSoup(resp.content, "html.parser")
		out = set()
		pieces = urlparse(url)
		base_url = pieces.scheme + '://' + pieces.netloc
		for a_tag in bs.find_all('a', href=True):
			link = a_tag.get('href')
			if (link == '#' 
				or link.startswith('mailto:')
				or any(link.endswith(banned) for banned in IGNORED_EXTENSIONS)):
				continue
			link = urljoin(base_url, link)
			if link not in self.visited and not (same_domain and base_url not in link):
				out.add(link)
		
		# pprint(out)
		print("Found", len(out), "links.")
		return out

if __name__ == '__main__':
	c = Crawler()
	starting_url = sys.argv[1]
	explored_urls = c.crawl(starting_url)
	pprint(explored_urls)
	print('We found {} links at the domain ({})!'.format(len(explored_urls), starting_url))
