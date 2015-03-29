import os
import sys

class rev:
  target = []
  data = []

def ex_dataset():
  fh = open('reviews3.txt','r')
  the_whole_thing = fh.read()
  parts = the_whole_thing.split('\n\n')
  for i in range(0,1000):
    if i%2==0:
      rev.target.append(int(parts[i]))
    else:
      rev.data.append(parts[i])
  
  return rev
  
  
#if __name__ == '__main__':
#  ex_dataset()
  
    
