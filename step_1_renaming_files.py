#Caroline Ball
#Oct. 16th 2014
#GIS 501
#Lab 3

#Step 1- remaming files with Python

import os

path = ("I:\\GIS-501\\Lab_3\\text_files\\")
newpath = ("I:\\GIS-501\\Lab_3\\text_files_new\\")

if not os.path.isdir(newpath):
    os.makedirs(newpath)


for root, dirs, files in os.walk(path):
    for fil in files:
        fil = fil.lower()
        filsec = fil.split('.')

        if filsec [1] == "txt":

            os.rename(path + fil, newpath + "file_" + fil + ".txt")

        else:

            os.rename(path + fil, newpath + "file_" + filsec [0] + ".txt")

            
