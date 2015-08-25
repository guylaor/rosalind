# solution for http://rosalind.info/problems/cons/

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
length = len(Strings[index])


def keywithmaxval(d):
	v=list(d.values())
	k=list(d.keys())
	return k[v.index(max(v))]


Profiles = { "A": "", "C": "", "G": "", "T": "" }
Result = ""

for l in range(length):
	temp = { "A": 0, "C": 0, "G": 0, "T": 0 }
	for i, v in enumerate(Strings):
		letter = Strings[v][l]
		if letter == "A":
			temp["A"] += 1
		elif letter == "C":
			temp["C"] += 1
		elif letter == "G":
			temp["G"] += 1
		elif letter == "T":
			temp["T"] += 1
	Profiles["A"] += str(temp["A"]) + " "
	Profiles["C"] += str(temp["C"]) + " "
	Profiles["G"] += str(temp["G"]) + " "
	Profiles["T"] += str(temp["T"]) + " "
	Result += keywithmaxval(temp)

print Result			
print "A: " + Profiles["A"]
print "C: " + Profiles["C"]
print "G: " + Profiles["G"]
print "T: " + Profiles["T"]
		
