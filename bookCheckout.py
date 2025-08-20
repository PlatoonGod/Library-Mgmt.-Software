"""
Module which contains functions used to ask the librarian for borrower’s member-ID and
the ID of the book(s) to be checked out.

After performing the validity checks the program returns a message letting the librarian know
whether they have checked out the book(s) successfully.
"""
from datetime import date

logs = []


def retrieve_log_records():
    """
    Automatically grabs the log info and puts each info piece into a list.
    """
    f = open("logfile.txt", "r")
    for line in f:
        s = line.strip()
        log = s.split(":")
        logs.append(log)
    f.close()
    return logs


def checkout():
    """
    This function handles the checkout and reservation process of a book.
    """
    while True:
        try:
            member_id = int(input("Please enter your 4 digit member ID:\n"))
            print("*" * 72)
            if 999 < member_id < 10000:
                break
            else:
                print("Sorry, you member ID is invalid. Please try again.")
                print("*" * 72)
        except ValueError:  # If the member_id entry format is invalid, this error message is displayed.
            print("Sorry, incorrect format. Please try again with your 4 digit member id.")
            print("*" * 72)

    function = input("What would you like to do?\nEnter 'c' to checkout a book.\nEnter 'r' to reserve a book.\n")

    if function == "r":
        logs = retrieve_log_records()
        print("*" * 72)
        reserve_book_id = input("What book would you like to reserve?\n(Enter the book ID and NOT its title)\n")
        for log in logs:
            if log[0] == reserve_book_id and log[3] != "" and log[4] == "":
                f = open("logfile.txt", "a")
                f.write("%s:%s:%s:%s::%s" % (reserve_book_id, member_id, "reserved", log[3], log[5]))
                print("Your book has been reserved.")
                f.close()
                break
            elif log[0] == reserve_book_id and log[3] != "" and log[4] == "" and log[2] == "":
                print("Sorry, the book you are trying has already been reserved.")
                print("*" * 72)

    elif function == "c":
        print("*" * 72)
        checkout_book_id = input("What book would you like to checkout?\n(Enter the book ID and NOT its title)\n")
        logs = retrieve_log_records()
        for log in logs:
            if log[0] == checkout_book_id and log[3] == "":
                log[5] = str(int(log[5]) + 1)
                f = open("logfile.txt", "a")
                f.write("%s:%s::%s::%s" % (checkout_book_id, member_id, date.today(), log[5]))
                f.close()
                print("Your book was checked out successfully.")
                break

            elif log[0] == checkout_book_id and log[3] != "" and log[4] == "":
                print("Sorry, the book you have requested has already been checked out. Try again later.")
                break

            elif log[0] == checkout_book_id and log[3] != "" and log[4] != "" and log[1] != member_id:
                log[5] = str(int(log[5]) + 1)
                f = open("logfile.txt", "a")
                f.write("%s:%s::%s::%s\n" % (checkout_book_id, member_id, date.today(), log[5]))
                f.close()
                print("Your book was checked out successfully.")
                break

            elif log[0] == checkout_book_id and log[1] == member_id:
                print("It appears you have already checked out this book.")
