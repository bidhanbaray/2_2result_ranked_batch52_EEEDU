from geojson import Point, Feature, FeatureCollection, dump
import json
import ssl
import PyPDF2
import re


pdfFileObj = open('result.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

numPages = pdfReader.numPages
print(numPages)

page = 0
# contentList = list()
rank = dict()
while page<numPages:
    pageObj = pdfReader.getPage(page)
    content = pageObj.extractText()
    contentList = content.split('\n')
    #print(contentList)
    length = 0
    #print(length)
    while length<len(contentList):
        try:
            x = float(contentList[length])
            if x<5:
                rank[contentList[length+3]] = contentList[length+1]
                length = length+1
            #print(x)
        except:
            length = length+1
            continue

        length = length+1
    page = page+1
pdfFileObj.close()
print(len(rank))

#ranks_sorted = sorted(rank.items(),reverse = True)
ranks_sorted = sorted(rank,key = rank.get,reverse = True)
#print(ranks_sorted)
i=0
# for cg,roll in ranks_sorted.items():
#     print(i,roll,cg)
#     i=i+1;
newf = open("rank.txt", "a")

while i<len(rank):
    print(i+1,ranks_sorted[i],rank[ranks_sorted[i]])
    newLine = str(i+1)+' '+str(ranks_sorted[i])+ ' '+ str(rank[ranks_sorted[i]])+'\n'
    newf.write(newLine)
    i = i+1
newf.close()
