import sys,os
from string import *
from binascii import *
from chardet import *
import re
arr=[]
ar=[]
st=""
url=""
lines=[]

def removenonascii(s):

    l=""
    for i in s:
        if(ord(i)==46 or ord(i)==47 or ord(i)==72 or ord(i) in range(97,97+26) or ord(i) in range(65,65+26)):
            l=l+i
    lines=l.split('\n')


    for line in lines:
        if line.startswith("http"):
            print (line.split("URL")[0])

infile =open("Path to history","r")
for line in infile:
    arr=line.split("Cho")

for s in arr:
    removenonascii(s)
    print (s)