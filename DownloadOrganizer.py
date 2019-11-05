import os
import shutil
import logging
import puremagic

# Changing the current directory to Downloads Folder.
os.chdir("C:\\Users\\VIREN\\Downloads")

current_dir = os.getcwd()

# Listing the contents in Directory.
dwnload_contents = os.listdir(current_dir)

# print(dwnload_contents)


def file_handler():

    # count = 0

    try:
        for files in dwnload_contents:

            # count += 1
            # print(f"{count}: {files}")

            # Check if the Content is File or a Folder.
            if os.path.isdir(files):
                logging.info("it's a Directory, skipping to next file.")

            else:
                # retrieving and storing the file type of files in kind variable.
                kind = puremagic.ext_from_filename(files)

                # Checks for the File type.
                if kind is None:
                    logging.info(
                        "File type not recognized moving to 'Other's' Folder")

                    # Checking if folder exists or not.
                    if os.path.exists(current_dir + "\\" + "others"):
                        logging.info(
                            "Folder already exists... moving into folder.")
                        shutil.move(files, current_dir + "\\" + "others")

                    else:
                        logging.info(
                            "The folder doesn't exist creating the folder ...")
                        os.mkdir(current_dir + "\\" + "others")
                        shutil.move(files, current_dir + "\\" + "others")

                else:
                    if os.path.exists(current_dir + "\\" + kind[1:]):
                        logging.info(
                            "Folder already exists... moving into folder.")
                        shutil.move(files, current_dir + "\\" + kind[1:])

                    else:
                        logging.info(
                            "Folder doesn't exist creating the folder...")
                        os.mkdir(current_dir + "\\" + kind[1:])
                        print("Folder created moving the file..")
                        shutil.move(files, current_dir + "\\" + kind[1:])

                    # print(f"\n{count}: {files} is of type: {kind}")

        # print(
        #     f"*************************************************************\nThe number of files in this Directory are: {count}")

    except puremagic.PureError:
        logging.error("Could not Find the File Type!!!")


if __name__ == "__main__":
    file_handler()
