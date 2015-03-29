import sys
import os
import urllib
from bs4 import BeautifulSoup

def main():
  url = 'http://www.flipkart.com/apple-iphone-6/product-reviews/ITMEYGPZAKJYVWQT?pid=MOBEYHZ2YAXZMF2J&sort=most_recent#RVU9Z3ZNQS07UIUB2'
  try:
    ufile = urllib.urlopen(url)
  except IOError:
    print 'problem reading url:', url
  
  fh = open('reviews.txt','w')
  soup = BeautifulSoup(ufile)
  spans = soup.find_all(attrs={"class": "review-text"})
  for span in spans:
    text = span.get_text()
    s = text.encode('utf-8').strip()
    fh.write(s+'\n\n')
if __name__ == '__main__':
  main()
