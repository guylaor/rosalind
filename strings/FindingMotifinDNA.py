# solution for http://rosalind.info/problems/subs/

f = open('data.txt', 'r')
sample = f.read()

pointer = 0

motif = "ATACTTAAT"
run = True
indecis = []

try:
	while run:
		index = sample.index(motif, pointer)
		index += 1
		indecis.append(str(index))
		pointer = index
except:
	print ' '.join(indecis)
	
	
