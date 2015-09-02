# optimized solution for http://rosalind.info/problems/lcsm/
# This run in ~0.6 seconds on 100 records of 1kb each

import re
import time
start = time.time()

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


def chunkString( _str, _len ):
	#print "chunking", _str, _len
	chunks = {}
	for i in range(len(_str)):
		chunk = _str[ i: i + _len ]
		if len(chunk) == _len:
			if chunk in chunks:
				chunks[chunk] += 1
			else:
				chunks[chunk] = 1
	return chunks 

def findSharedChunks( _str, _chunks ):
	#print "findShared", _str
	_common = {}
	for i, v in enumerate(_chunks):
		#print _str.find(v), v
		if _str.find(v) > -1:
			if v in _common:
				_common[v] += 1
			else:
				_common[v] = 1
	return _common

def optimizeRuns( totalItems, chunkLen ):
	if chunkLen < 2:
		return totalItems
	else:
		return totalItems / chunkLen

	
chunkSize = 2
initIndex = index
ResultsChunks = {}

def run( chunkSize, initIndex ):
	global Strings, ResultsChunks
	chunksArr = chunkString( Strings[ initIndex ] , chunkSize )
	for i, v in enumerate(Strings):
		if v != initIndex:
			chunksArr = findSharedChunks( Strings[ v ] , chunksArr )
		if i > optimizeRuns( len(Strings), len(chunksArr) ):
			break
	if len(chunksArr) > 0:
		ResultsChunks = chunksArr
		chunkSize += 1
		run( chunkSize, initIndex )

	

run( chunkSize, initIndex )

print "RESULTS: "

for r in ResultsChunks:
	print r	

print "==========================="
end = time.time()

print "Running took "+ str(float(end - start)) + " seconds."
