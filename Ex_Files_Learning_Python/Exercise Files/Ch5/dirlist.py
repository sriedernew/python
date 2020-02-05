import os

dirList = os.listdir('./Ch5')
dirList.sort()

for sFile in dirList:
    if sFile.find('.mp3') == -1:
        dirList.remove(sFile)

for sFile in dirList:
    print(sFile)