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
  
  fh = open('reviews_new.txt','w')
  soup = BeautifulSoup(ufile)
  divs = soup.find_all(attrs={"class":"fclear fk-review fk-position-relative line "})

  for div in divs:
    star = div.find(attrs={"class":"fk_stars"})
    text = div.find(attrs={"class":"review-text"}).get_text()
    s = star['title']
    s.encode('utf-8')
    t = text.encode('utf-8').strip()
    fh.write(s+'\n\n'+t+'\n\n')
if __name__ == '__main__':
  main()
