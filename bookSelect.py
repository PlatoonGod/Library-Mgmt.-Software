"""
Module which contains functions used to list the recommended book genres
for the librarian and visualise the list by using the Matplotlib module.
"""
from datetime import datetime, timedelta


def weeding():
    """
    Takes the current date, and calculates the difference in months between
    the current date and the date the book was returned. Then, if the
    difference is greater than 1 year, the program recommends that book for
    removal
    """
    log = open("logfile.txt", "r")
    print("*" * 72)
    print("Book replacement suggestions:\n")
    for record in log:
        s = record.strip()
        info = s.split(":")
        returnDate = datetime.strptime(info[4], "%Y-%m-%d")
        currentDate = datetime.today()

        if returnDate != "":
            difference = currentDate - returnDate

            if difference.days > 365:
                print("Book with ID " + info[0] + " has not been checked out in more than 12 months. Consider changing "
                                                  "the book.")
            elif difference.days <= 365:
                print("Book with ID " + info[0] + " is still relevant. I would suggest keeping it in the library.")


def weedTest():
    """
    Tests the weeding file.
    """
    testInfo = []
    f = open("logfile.txt", "r")
    for i in f:
        s = i.strip()
        logInfo = s.split(",")
        testInfo.append(logInfo)
    print("Successfully returned info")
    f.close()
    return testInfo


if __name__ == "__main__":
    print("Testing file")
    Info = weedTest()
    print(Info)
