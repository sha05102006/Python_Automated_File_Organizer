#Importing the necessary Modules
import os
import shutil
import time

path = input("Enter Path: ") #Get the File path from the user


#"While" loop is used to keep the program running in the background
while True:
    files = os.listdir(path) #List out the directories
    for file in files:
        full_path = os.path.join(path,file)

        #Skip folders present in the directory
        if os.path.isdir(full_path):
            continue

        filename,extension = os.path.splitext(file)

        #Skip files that does not have an extension
        if extension == "":
            continue
        extension=extension[1:]

        #Check for appropriate folder to sort in or create a new one
        target_folder = os.path.join(path,extension)
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)

        #Move the file into the appropriate folder
        destination = os.path.join(target_folder,file)
        if not os.path.exists(destination):
            shutil.move(full_path,destination)

    time.sleep(5) #Pause the program for 5 sec to not waste CPU resources