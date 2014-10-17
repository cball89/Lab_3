#Caroline Ball
#Oct. 16th 2014
#GIS 501
#Lab 3

#step 3- replacing words in a text document

Lab_3_text = open('I:\\GIS-501\\Lab_3\\GIS_is_the_best.txt')  #opening file path

infile = open ('I:\\GIS-501\\Lab_3\\GIS_is_the_best.txt')

outfile = open ('I:\\GIS-501\\Lab_3\\output_text.txt', 'w')

replacements = {'Science':'Systems', 'science':'systems'}

for line in infile:
    for src, target in replacements.iteritems():
        line = line.replace(src, target)
    outfile.write(line)

infile.close()

outfile.close()





