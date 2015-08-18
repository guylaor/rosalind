# solution for http://rosalind.info/problems/prot/

codon_string = """UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G"""

codon_list = codon_string.split()

dna = codon_list[::2] # gets every second element 
prots = codon_list[1::2] # gets every second element but starts from 1

codons = dict( zip(dna, prots) )

f = open('data.txt', 'r')
sample = f.read()
sample_len = len( sample )

protein_result = ""

for i in xrange(0, sample_len, 3):
	sample_codon = sample[i:i+3]
	protein = codons[ sample_codon ]
	if protein != "Stop":
		protein_result = protein_result + protein
	else:
		break

print protein_result

