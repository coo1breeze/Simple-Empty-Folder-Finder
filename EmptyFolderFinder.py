# by Paul Cooper, 2021

import os

if __name__ == '__main__':
    emptyDirectories = []
    emptyDirectoryCount = 0
    dirCount = 0
    directoryToUse = os.getcwd()
    choice = input("To search the current directory, press Enter, otherwise, enter a path and hit Enter. ")
    print("\n\n")
    if choice != "":
        directoryToUse = choice
    if not os.path.exists(directoryToUse):
        print("The path you chose either doesn't exist or was typed incorrectly.")
    else:
        for path, dirs, files in os.walk(directoryToUse):
            dirCount += 1
            if len(os.listdir(path)) == 0:
                if emptyDirectoryCount == 0:
                    print("Empty Directories\n- - - - -")
                emptyDirectoryCount += 1
                print(str(emptyDirectoryCount) + "   " + path)
        if emptyDirectoryCount == 0:
            print("No empty directories found!")
        print("- - - - -\n{0} directories found in total.\n{1} directories are empty.".format(str(dirCount),
                                                                                              str(emptyDirectoryCount)))
    input()
