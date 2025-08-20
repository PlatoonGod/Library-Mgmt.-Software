"""
Module which contains common functions that the book search,
checkout, return and select modules use to interact with the data files.
"""

records = []
listed_info = []


def retrieve_book_records():
    """
    Automatically grabs the book info data and places each book info into a list.
    """
    f = open("Book_Info.txt", "r")
    for line in f:
        s = line.strip()
        record = s.split(":")
        records.append(record)
    f.close()


def lister():
    """
    Function that converts each book title and author from the Book_Info.txt file into lists.
    """
    f = open("Book_Info.txt", "r")
    for line in f:
        s = line.strip()
        info = s.split(":")
        listed_info.append(info)
        print("%s - %2s by %4s" % (info[0], info[2], info[3]))
    f.close()
