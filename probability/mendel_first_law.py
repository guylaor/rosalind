# solution for http://rosalind.info/problems/iprb/

k = 2
m = 2
n = 2

hetro_prob = 0.75
hetro_prob_recs = 0.5

total = k + m + n

def k_prob(k, total):
	return float(k) / float(total)
	
def inital_m_prob(m, total):
	return float(m) / float(total)

def mk_prob(m, k, n, total):
	first = inital_m_prob(m, total)
	return first * k_prob(k, total-1)

def mm_prob(m, k, n, total):
	first = inital_m_prob(m, total)
	second = float(m-1) / float(total-1)
	return first * second * hetro_prob

def mn_prob(m, k, n, total):
	first = inital_m_prob(m, total)
	second = inital_n_prob(n, total-1)
	return first * second * hetro_prob_recs
	
def inital_n_prob(n, total):
	return float(n) / float(total)
	
def nk_prob(m, k, n, total):
	first = inital_n_prob(n, total)
	second = k_prob(k, total-1)
	return first * second

def nm_prob(m, k, n, total):
	first = inital_n_prob(n, total)
	second = inital_m_prob(m, total-1)
	return first * second * hetro_prob_recs

k_probability = k_prob(k, total)
mk_probability = mk_prob(m, k, n, total)
mm_probability = mm_prob(m, k, n, total)
mn_probability = mn_prob(m, k, n, total)
nk_probability = nk_prob(m, k, n, total)
nm_probability = nm_prob(m, k, n, total)

print "k prob", k_probability
print "mk_prob", mk_probability
print "mm_prob", mm_probability 
print "mn_prob", mn_probability
print "nk_prob", nk_probability
print "nm_prob", nm_probability

result = k_probability + mk_probability + mm_probability + mn_probability + nk_probability + nm_probability

print result
