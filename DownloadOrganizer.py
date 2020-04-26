import os
import platform
import shutil
import logging
import puremagic
import pdb

# Changing the current directory to Downloads Folder.


# determining which os system is installed and retrieving the home path.
user_os = platform.system()

if user_os == 'Linux':
    downloads_path = os.getenv('HOME')+'/Downloads/'
elif user_os == 'Windows':
    downloads_path = os.getenv('USERPROFILE')+'/Downloads/'


print(f'found the user\'s download path -- {downloads_path}')

# Listing the contents in Directory.
download_folder_contents = os.listdir(downloads_path)

# print(download_folder_contents)


def file_handler():

    count = 0

    try:
        for files in download_folder_contents:
            count += 1
            print(f"{count}: {files}")

            # Check if the Content is File or a Folder.
            if os.path.isdir(os.path.join(downloads_path, files)):
                print(f"{files} is a Directory!")

            else:
                # retrieving and storing the file type of files in kind variable.
                kind = puremagic.ext_from_filename(files)
                print(f'file extension is - {kind}')

                # Checks for the File type.
                if kind is None or ' ':
                    print(
                        "File type not recognized moving to 'Other's' Folder")

                    # Checking if folder exists or not.
                    if os.path.exists(os.path.join(downloads_path, "others")):
                        print(
                            "Folder already exists... moving into folder.")
                        shutil.move(downloads_path + files,
                                    downloads_path + "others")

                    else:
                        print(
                            "The folder doesn't exist creating the folder ...")
                        os.mkdir(downloads_path + "others")
                        shutil.move(downloads_path + files,
                                    downloads_path + "others")

                else:
                    if os.path.exists(os.path.join(downloads_path, kind[1:])):
                        print(
                            "Folder already exists... moving into folder.")
                        shutil.move(downloads_path + files,
                                    downloads_path + kind[1:])

                    else:
                        print(
                            "Folder doesn't exist creating the folder...")
                        os.mkdir(downloads_path + kind[1:])
                        print("Folder created moving the file..")
                        shutil.move(downloads_path + files,
                                    downloads_path + kind[1:])

                    print(f"\n{count}: {files} is of type: {kind}")

        print(
            f"*************************************************************\nThe number of files in this Directory are: {count}")

    except puremagic.PureError:
        print("Could not Find the File Type!!!")


file_handler()
