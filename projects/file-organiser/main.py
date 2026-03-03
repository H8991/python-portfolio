import os
import shutil

#Welcome
print("==== Hello, welcome to File Organiser. ====")

#Get path of junk folder
junk_folder = input("Please paste the path of the folder you would like to organise:").strip().replace('"', '')

#Check if folder is a directory
while not os.path.isdir(junk_folder):
    print("Folder not found. Please try again.")
    junk_folder = input("What is the file path?").strip().replace('"', '')

#Confirm folder has been found
print("Thank you. Folder found.")


