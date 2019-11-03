import os
import shutil
import puremagic

# Changing the current directory to Downloads Folder.
os.chdir('C:\\Users\\VIREN\\Downloads')

current_dir = os.getcwd()

# Listing the contents in Directory.
dwnload_contents = os.listdir(current_dir)

# print(dwnload_contents)


def main():
    count = 0
    try:
        for files in dwnload_contents:
            count += 1
            # print(f"{count}: {files}")

            # Check if the Content is File or a Folder.
            if os.path.isdir(files):
                print("it's a Directory, skipping to next file.")

            else:
                # retrieving and storing the file type of files in kind variable.
                kind = puremagic.ext_from_filename(files)

                # Checks for the File type.
                if kind is None:
                    print("File type not recognized moving to 'Other's' Folder")

                else:
                    print(f"\n{count}: {files} is of type: {kind}")

    except puremagic.PureError:
        print("Cannot identyfy the File!!!")

    # print(
    #     f"*************************************************************\nThe number of files in this Directory are: {count}")


if __name__ == "__main__":
    main()
