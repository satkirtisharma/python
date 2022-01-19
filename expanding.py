# -*- coding: utf-8 -*-
"""
write a function that takes input as a list of integers l and returns true if the absolute difference between adjacent pair of elements strictly increases
Created on Wed Jan 19 17:23:27 2022

@author: SATKIRTI SHARMA
"""

def expanding(lst):
    diff=[]

    for i in range(len(lst)):

     if(i<len(lst)-1):

      x=lst[i]-lst[i+1]

      if(x<0):

       x=-x

      diff.append(x)

    for i in range(len(diff)):

     if(i<len(diff)-1):

      if(diff[i+1]>diff[i]):

       f=0

      else:

       f=1

       break

    if(f==1):

      return False

    else:

      return True
lst=list(map(int,input().split()))   
print(expanding(lst))