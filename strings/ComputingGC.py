# solution for http://rosalind.info/problems/gc/

import re

Strings = {}
index = "" 

f = open('fasta.txt', 'r')
for line in f:
  match = re.match(r">", line)
  #match = str(line).find(">")
  if match:
    index = line.strip()
    index = index[1:len(index)]
    Strings[index] = ""
  else:
    Strings[index] = Strings[index] + line.strip()

#print Strings

def percentage(part, whole):
  return 100 * float(part)/float(whole)

def countGC(str):
  cnt = 0
  for i in str:
    if i in 'CG':
      cnt = cnt + 1
  return cnt


resultIndex = ""
resultPcnt = 0
for s in Strings:
  pcnt = percentage( countGC(Strings[s]) , len(Strings[s]) )
  #print Strings[s],  countGC(Strings[s]) , len(Strings[s])  , pcnt
  if pcnt > resultPcnt:
    resultPcnt = pcnt
    resultIndex = s

print ''
print resultIndex
print resultPcnt





