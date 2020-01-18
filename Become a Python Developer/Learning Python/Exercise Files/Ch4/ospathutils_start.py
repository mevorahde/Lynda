#
# Example file for working with os.path module
#
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
    # Print the name of the OS
    # print(os.name)

    # Check for item existence and type
    # print("Item exists: {}".format(path.exists("textfile.txt")))
    # print("Item is a file: {}".format(path.isfile("textfile.txt")))
    # print("Item is a file: {}".format(path.isdir("textfile.txt")))

    # Work with file paths
    # print("Item path: {}".format(path.realpath("textfile.txt")))
    # print("Item path: {}".format(path.split(path.realpath("textfile.txt"))))

    # Get the modification time
    # t = time.ctime(path.getatime("textfile.txt"))
    # print(t)
    # print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))

    # Calculate how long ago the item was modified
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
    print("It has been {} since the file was modified.".format(td), "\nOr, {} seconds".format(td.total_seconds()))



if __name__ == "__main__":
    main()
