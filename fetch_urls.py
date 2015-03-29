import sys
import os
import urllib
from bs4 import BeautifulSoup

def urls():
  start = 'http://www.flipkart.com/moto-g-2nd-gen/product-reviews/ITMDYGZ8GQK2W3XP?pid=MOBDYGZ6SHNB7RFC&rating=1,2,3,4,5&reviewers=all&type=all&sort=most_helpful&start=' 
  url=[]
  for i in range(0,10):
    temp = start+str(10*(i+1))
    url.append(temp)
    
  for u in url:
    print u+'\n'
  
  
if __name__ == '__main__':
  urls()
  
  
  
