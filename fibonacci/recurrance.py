print "solution for problem in http://rosalind.info/problems/fib/"

cycles = 33
birth_rate = 5

mature_bunnies = 0
new_bunnies = 1
born_bunnies = 0


def traverse():
	global mature_bunnies, new_bunnies, born_bunnies
	born_bunnies = mature_bunnies * birth_rate

def grow():
	global mature_bunnies, new_bunnies, born_bunnies
	mature_bunnies = mature_bunnies + new_bunnies
	new_bunnies = born_bunnies


def cycle():
  traverse()
  grow()


for t in range(cycles):
  print (t), 'cycle-', mature_bunnies, new_bunnies, born_bunnies
  cycle()
  
print mature_bunnies
