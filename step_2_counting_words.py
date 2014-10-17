#Caroline Ball
#Oct. 16th 2014
#GIS 501
#Lab 3

#Step 2- script for counting the number of words in GIS_is_the_best text file

Lab_3_text = open("I:\\GIS-501\\Lab_3\\GIS_is_the_best.txt")
file_list = Lab_3_text.read()     #read text file

system_count, science_count, total_words = 0,0,0    # words to be counted

for word in file_list.split(' '):    #loop for separating spaces btw words
    if word.lower() == 'systems':    #making all words in the list lower-cased
        system_count = system_count + 1  #counting all system words (they start at 0)

    elif word.lower() == 'science':      #making all "science" words lower case
        science_count = science_count + 1    #counting all science words  (they start at 0)

    else:
        total_words = total_words + 1       #or else, count total words not including system or science

total_words = total_words + science_count + system_count  #combining all words for grand total count

print total_words   #show the toal word count

print system_count    #show the total system word count

print science_count   #show the total science word count 

Lab_3_text.close()


#run operation and complete 

                  
