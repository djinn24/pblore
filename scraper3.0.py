import sys
import os
import urllib
from bs4 import BeautifulSoup


def fetch_urls():
  start = 'http://www.flipkart.com/moto-g-2nd-gen/product-reviews/ITMDYGZ8GQK2W3XP?pid=MOBDYGZ6SHNB7RFC&rating=1,2,3,4,5&reviewers=all&type=all&sort=most_helpful&start=' 
  urls=[]
  
  for i in range(0,50):
    temp = start+str(10*(i+1))
    urls.append(temp)
    
  return urls
  

def main():
  urls = fetch_urls()
  count=0
  #fh = open('reviews3.txt','w')
  for url in urls:
    try:
      ufile = urllib.urlopen(url)
    except IOError:
      print 'problem reading url:', url
  
    soup = BeautifulSoup(ufile)
    divs = soup.find_all(attrs={"class":"fclear fk-review fk-position-relative line "})
    if not divs:
      print 'empty',url+'\n'
    
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
      count+=1
    #print str(count/10),'done'
  print('done.rev-count:%d'%(count))
      
if __name__ == '__main__':
    main()
