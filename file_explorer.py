import sys
import os
import mimetypes    

#grabs the names of all the files in a given directory
listOfFiles = os.listdir(sys.argv[1]) 

for i in range(len(listOfFiles)):

    filePath=sys.argv[1]+listOfFiles[i]
    fileSize = os.stat(filePath).st_size
    fileMimeType = mimetypes.guess_type(filePath)
    fileCategory = "file"

    #sets wheather the element in the directory is file or another directory
    if(os.path.isdir(filePath)):
        fileCategory="dir"
        filePath+="/"

    #set the prefixe for the file/directory size e.g Bytes, MB, GB
    bytePrefixe="Bytes"
    if(fileSize/1000>=1):

        bytePrefixe="KB"
        fileSize/=1000

    elif(fileSize/1000000>=1):

        bytePrefixe="MB"
        fileSize/=1000000

    elif(fileSize/1000000000>=1):
        
        bytePrefixe="GB"
        fileSize/=1000000000

    print(filePath+"    ["+fileCategory+"]    "+str(fileSize)+bytePrefixe+"    "+str(fileMimeType[0]))
