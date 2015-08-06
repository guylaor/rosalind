print "solution for problem in http://rosalind.info/problems/fibd/"

cycles = 89
birth_rate = 1
mortality = 19

bunnies = [1]


def reproduce():
	global bunnies
	born_bunnies = sum(bunnies[1:]) * birth_rate
	bunnies.insert(0, born_bunnies)

def grow():
	global bunnies
	if len(bunnies) > mortality:
		bunnies.pop(-1)


def cycle():
  reproduce()
  grow()


for t in range(cycles):
  total = sum(bunnies)
  print (t+1), 'cycle-', bunnies, total
  cycle()


print "total:", total
