import os
import sys
import time
import hashlib

"""
Parameters:
files -- set of filenames to copy
destinations -- set of directories name to copy to
"""
def backup(files, destinations):
    #If no exist, create dir called backup in the current dir
    #Copy each files in the dir and add date to name

    #Create dirs 
    for dirname in destinations:
        try:
            os.mkdir(dirname)
        except FileExistsError:
            #print("[Error] Dir %s already exists" % dirname)
            pass

    #Copy files
    nbrOfDest = len(destinations)
    nbrOfFiles = len(files)

    if nbrOfDest == 0 or nbrOfFiles == 0:
        print("[Error] No files or dest provided.")
        return;

    if nbrOfDest == nbrOfFiles:
        for i in range(nbrOfDest):
            filename, dirname = files[i], destinations[i]
            newfilename = filename

            fileExt = os.path.splitext(newfilename)[1]
            #Check if file extension exists to add date to file
            if fileExt == "":
                #File has no extension
                newfilename += "_" + time.strftime("%Y_%b_%d_%Hh_%Mm_%Ss")
            else:
                extIndex = newfilename.index(fileExt)
                if extIndex == 0:
                    extIndex = newfilename[1:].index(fileExt) + 1
                #print("[Info] File %s extension at %d" % (filename, extIndex))
                newfilename = newfilename[:extIndex] + "_" + time.strftime("%Y_%b_%d_%Hh_%Mm_%Ss") + newfilename[extIndex:]
            
            copy(filename, dirname + "/" + newfilename)
    elif nbrOfDest == 1:
        dirname = destinations[0]
        for filename in files:
            copy(filename, dirname + "/" + filename)
    elif nbrOfDest > nbrOfFiles and nbrOfFiles == 1:
        filename = files[0]

        for dest in destinations:
            copy(filename, dest + "/" + filename)
    else:
        print("[Error] Can't copy files to destinations.")



def copy(filename, destination):
    destinationfile = open(destination, 'w')

    try:
        with open(filename, 'r') as sourcefile:
            for line in sourcefile:
                encryptedline = hashlib.sha512(line.encode()).hexdigest()
                destinationfile.write(encryptedline)
    except FileNotFoundError:
        print("[Error]: File %s to copy not found." % destination)