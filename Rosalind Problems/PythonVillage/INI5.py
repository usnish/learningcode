#PYTHON VILLAGE PROBLEM #5: Reading and Writing Files
#Given: A file containing at most 1000 lines.
#Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.

inputfile = open('input.txt','r')
outputfile = open('output.txt','w')

count = 0

for line in inputfile:
	if count%2 != 0:
		outputfile.write(str(line))
	count = count + 1

inputfile.close()
outputfile.close()




