# solution for http://rosalind.info/problems/grph/

import re

Strings = {}
Prefixes = {}
Suffixes = {}
index = "" 

f = open('fasta.txt', 'r')
for line in f:
  match = re.match(r">", line)
  #match = str(line).find(">")
  if match:
    index = line.strip()
    index = index[1:len(index)]
    Strings[index] = ""
    Prefixes[index] = ""
    Suffixes[index] = ""
  else:
    Strings[index] = Strings[index] + line.strip()
    Prefixes[index] = Strings[index][:3]
    Suffixes[index] = Strings[index][-3:]

for v, i  in enumerate(Strings):
	for v2, i2 in enumerate(Strings):
		if Prefixes[i] == Suffixes[i2]:
			if i != i2:
				print i2, i



