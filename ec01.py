##################
#CS 532 EC 0.1 Programming Task: friend counting with Comma Separated Values Parsing
#Prof. Poursardar
#January 8th 2023
##################
#
#
#############################################################################################START###
#import comma separated value, urllib, requests, and os modules/libraries
import csv, urllib.request, os
#create string data type with the absolute URL / HTTPS link
absoluteUrl = "https://raw.githubusercontent.com/odu-cs432-websci/public/main/fall21/getting-started/friend-count.csv"
#
requestResponse = urllib.request.urlopen(absoluteUrl)
#
lines = [l.decode('utf-8') for l in requestResponse.readlines()]
#
content = csv.reader(lines)
#####################
#for row in content:#
#    #print(row)    #
#    dataSet = row  #- - - - - - > testing stuff out
#    print(dataSet) #
#####################
#convert list to dictionary
dataSetDictionaryConversion = dict(filter(None, csv.reader(lines)))
#remove user and friendcount elements from dictionary
del dataSetDictionaryConversion['USER']
print(dataSetDictionaryConversion)
print("#")
print("#")
#need to figure out the sort process and output alphabetically with for statement
sortedDict = sorted(dataSetDictionaryConversion.items(), key=lambda x:x[1])
print(sortedDict)
###################################################################################END###
