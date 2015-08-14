# solution for problem in http://rosalind.info/problems/hamm/


f = open('data.txt', 'r')

line1 = f.readline().strip()
line2 = f.readline().strip()

count = 0

for i in range(len(line1)):
  print line1[i] + " - " + line2[i]
  if line1[i] != line2[i]:
    count = count + 1

print count
