from concurrent.futures import ThreadPoolExecutor
from threading import Semaphore, Condition, RLock
import concurrent
from collections import deque

import logging

def crawl(root_url):
    frontier = deque([root_url])
    visited = set()
    
    while frontier:
        url = frontier.popleft()
        if url in visited:
            continue
        
        visited.add(url)
        
        for neighbor_link in extract_links(url):
            if neighbor_link not in visited:
                frontier.append(neighbor_link)
    
    return visited

def Crawler(object):
    def __init__(self, root_url, max_workers=10):
        self.root_url = root_url
        self.frontier = deque([root_url])
        self.visited = set()
        self.semaphore = Semaphore(max_workers)
        self.condition = Condition(RLock())
        self.n = max_workers

    def crawl_multi(self, root_url):
        futures = []
        
        while:
            with self.condition.lock():
                while self.semaphore == 0:
                    self.condition.wait()
                if self.semaphore == self.max_workers and self.frontier:
                    return links
                    
            if self.frontier:
                url = self.frontier.pop()
                if url in self.visited:
                    continue
                self.visited.add(url)

                self.semaphore.acquire()
                future = self.pool.submit(extract_links_pro, url)
                futures.append(future)

        
    def extract_links_pro(self, page):
        links = extract_links(page)
        for neighbor_link in links:
            if neighbor_link not in self.visited:
                self.frontier.append(neighbor_link)

        with self.condition.lock():
            self.semaphore.release()
            self.condition.notify()
        
    def get_results(self):
        return self.visited

def extract_links(page):
    # Assume this implementation is given through an API
    pass

if __name__ == "__main__":
    root_url = 'https://www.dropbox.com'
    pool = ThreadPoolExecutor(10)
    crawler = Crawler(root_url, 10)