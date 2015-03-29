import sys
import os
import urllib
from bs4 import BeautifulSoup

def main():
  url = 'http://www.flipkart.com/moto-g-2nd-gen/product-reviews/ITMDYGZ8GQK2W3XP?pid=MOBDYGZ6SHNB7RFC&rating=1,2,3,4,5&reviewers=all&type=all&sort=most_helpful&start=40'
  try:
    ufile = urllib.urlopen(url)
  except IOError:
    print 'problem reading url:', url
  
  fh = open('reviews_new.txt','w')
  soup = BeautifulSoup(ufile)
  divs = soup.find_all(attrs={"class":"fclear fk-review fk-position-relative line "})

  for div in divs:
    star = div.find(attrs={"class":"fk-stars"})
    text = div.find(attrs={"class":"review-text"}).get_text()
    s = star['title'].encode('utf-8').split()
    s = int(s[0])
    if s>3:
      sent=1
    elif s<3:
      sent=-1
    else:
      sent=0   
    t = text.encode('utf-8').strip()
    fh.write(str(sent)+'\n\n'+t+'\n\n')
if __name__ == '__main__':
  main()
