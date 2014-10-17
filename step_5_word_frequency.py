#Caroline Ball
#Oct. 16th 2014
#GIS 501
#Lab 3

#Step 5- word frequency



import operator

file_path = "I:\\GIS-501\\Lab_3\\shunned_house.txt"
Lovecraft = open(file_path)
word_list = Lovecraft.read()

def clean_list():
    clean_list = word_list.lower().split()
    words_list = []
    for word in clean_list:
        symbols = "1234567890!@#$%^&*()_+{}|:\"<>?-=[]\;\',./"
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            words_list.append(word)
    build_dictionary(words_list)
    
def build_dictionary(words_list):
    word_count = {}
    for word in words_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
            
    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print(key, value)

clean_list()


                         

