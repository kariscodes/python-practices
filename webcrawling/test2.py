import os

workingPath = os.getcwd()
print(workingPath)

keyword = 'WebCrawling'
resultPath = workingPath + '/' + keyword
print(resultPath)

# create folder
if os.path.exists(resultPath)==False:
    os.mkdir(resultPath)

f = open(resultPath + '/' + 'test2.txt', 'w')
f.close()

#for dirpath, dirname, filename in os.walk(os.getcwd()):
#    print(dirpath, dirname, filename)