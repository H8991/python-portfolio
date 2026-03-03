import os
import shutil

#Welcome
print("=====================================")
print("= Hello, welcome to File Organiser. =")
print("=====================================")

#Get path of junk folder
junk_folder = input("Please paste the path of the folder you would like to organise:").strip().replace('"', '')

#Check if folder is a directory
while not os.path.isdir(junk_folder):
    print("Folder not found. Please try again.")
    junk_folder = input("What is the file path?").strip().replace('"', '')

#Confirm folder has been found
print("Thank you. Folder found.")

#List files found in folder
files = os.listdir(junk_folder)
print("These are the files in that folder:\n")
for file in files:
    print(file)

#Define sorting categories
sorting_categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".docx", ".doc", ".pdf", ".txt"],
    "Audio": [".mp3", ".mp4", ".wav"]
}

#Sort files into categories
#split name from extension
for file in files:
    name, extension = os.path.splitext(file)
    extension = extension.lower()

    #check each category to see if extension is suitable
    for filetype, ext_list in sorting_categories.items():
        if extension in ext_list:
            target_folder = os.path.join(junk_folder, filetype)

            #Create folder if not created yet
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)

            #Move the file
            source = os.path.join(junk_folder, file)
            destination = os.path.join(target_folder, file)
            #Use shutil to move
            shutil.move(source, destination)
            print(f"Moved {file} to {target_folder} folder.")

#Completion message
print("All files in this folder have been organised.")

