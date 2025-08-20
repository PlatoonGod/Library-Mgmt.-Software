"""
Module which contains functions used to ask the librarian for the ID of the book(s)
they wish to return and provide either an appropriate error message,
or a message letting them know they have returned the book(s) successfully.
"""
import bookCheckout
import datetime

logs = []


def book_return(return_id):
    """
    Function that handles the returning of books.

    return_id: the ID of the book being returned
    """
    logs = bookCheckout.retrieve_log_records()
    bookReturn = False

    log_file = open("logfile.txt", "r")
    log_list = log_file.readlines()
    x = 0
    for log in logs:
        if log[0] == return_id and log[3] != "" and log[4] == "":
            log[4] = str(datetime.date.today())
            updated_log = ":".join(log)
            log_list[x] = updated_log
            f = open("logfile.txt", "w")
            log_list = "".join(log_list)
            f.write(log_list)
            f.close()
            print("*" * 72)
            print("Book return was successful")
        x = x + 1
        log_file.close()
        bookReturn = True

    if not bookReturn:
        print("Book isn't checked out.")
