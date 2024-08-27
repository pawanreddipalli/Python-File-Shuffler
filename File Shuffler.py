# File Shuffler
# @author Yesho Reddipalli

import os, time, random
from win32_setctime import setctime

def display(path):
    # To display the contents of the files
    x,c=filesindir(path)
    for i in x:
        print("File Name: "+i)
        print("Creation time: "+time.ctime(os.stat(path+'/'+i).st_ctime))
        print("Modified time: "+time.ctime(os.stat(path+'/'+i).st_mtime))
        print("Access time: "+time.ctime(os.stat(path+'/'+i).st_atime))


def filesindir(path):
    count=0 # to count the number of files in directory 
    files=[]
    # Iterate directory
    for x in os.listdir(path):
        # check if current path is a file
        if os.path.isfile(os.path.join(path, x)):
            # appends the files to the files list
            files.append(x)
            # if path is a file then increase the count
            count+=1
    return files,count

def rename(dir):
    # To change to name of the files temporarily
    temp_files,count=filesindir(dir)
    temp = 10000000
    for src in temp_files:
        ext=os.path.splitext(src)[1]
        temp+=1
        os.rename(dir+'/'+src,dir+'/'+str(temp)+ext)

    files,count=filesindir(dir)
    newname = []
    for i in range(1,count+1):
        newname.append(str(i))
    random.shuffle(newname) #creating new shuffled numbers for naming the files
    for src, dest in zip(files, newname):
        ext=os.path.splitext(src)[1] # To find the extention of the files
        os.rename(dir+'/'+src,dir+'/'+dest+ext) # renaming the files
    
def timemod(dir):
    # Removing 10 days from the current time
    # 10 days = 864000 seconds
    time_stamp=time.time()-864000  
    x,c=filesindir(dir)
    for i in x:
        setctime(dir+'/'+i, time_stamp) # To set the file creation time
        os.utime(dir+'/'+i, (time_stamp, time_stamp)) # To set the file modification time and access time

def run_automation():
    # folder paths
    left_dir  = r'data/left'
    right_dir = r'data/right'
    display(left_dir) 
    display(right_dir)
    rename(left_dir)
    rename(right_dir)
    print('Files are renamed in the directories')
    timemod(left_dir)
    timemod(right_dir)
    print('Files dates have been modified')
    display(left_dir)
    display(right_dir)



print("Press 1 for the code to run every 30 seconds")
print("press 2 for the code to run every 1 week")
rep=int(input())
match rep:
    case 1:
         while(True): # For the code to run indefinitely
            run_automation()
            time.sleep(30) # sleeps for 30 seconds
            print("30 seconds are done")
            print("Running the code again\n")
    case 2:
        while(True): # For the code to run indefinitely
            run_automation()
            time.sleep(604800) # sleeps for 1 week or 604800 seconds
            print("1 week is done")
            print("Running the code again\n")
    case _:
        print("invalid key press again")
