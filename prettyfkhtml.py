import sys
import os
import urllib
from bs4 import BeautifulSoup

def main():
  url = 'http://www.flipkart.com/moto-g-2nd-gen/product-reviews/ITMDYGZ8GQK2W3XP?pid=MOBDYGZ6SHNB7RFC&type=all'
  try:
    ufile = urllib.urlopen(url)
  except IOError:
    print 'problem reading url:', url
  
  fh = open('review2.html','w')
  soup = BeautifulSoup(ufile)
  s = soup.prettify().encode('utf-8')
  fh.write(s)
if __name__ == '__main__':
  main()
