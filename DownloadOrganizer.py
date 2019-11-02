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

    for files in dwnload_contents:
        count += 1
        print(f"{count}: {files}")

    print(
        f"*************************************************************\nThe number of files in this Directory are: {count}")


if __name__ == "__main__":
    main()
