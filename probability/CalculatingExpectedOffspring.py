# solution for http://rosalind.info/problems/iev/
# getting Expected value

input = "1 0 0 1 0 1"
couples = input.split(" ")

couples = map(float, couples)
prob = [1,1,1,0.75,0.5,0]

result = (couples[0] * prob[0]) + (couples[1] * prob[1]) + (couples[2] * prob[2]) + (couples[3] * prob[3]) + (couples[4] * prob[4]) + (couples[5] * prob[5])

# multiply by 2 as there are 2 offspring for each couple 
print result * 2
