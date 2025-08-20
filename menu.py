"""
Main program which provides the required menu options
to the librarian for the program functionalities.
"""
import bookReturn
import bookSearch
import database
import bookCheckout
import bookSelect
import datetime

logs = []


def line_break():
    """
    Creates a line break using '*' symbols.
    """
    print("*" * 72)


def line():
    """
        Creates a line break
        """
    print("\n")


def menu():
    """
    This function prints out the menu selection screen and runs the functions
    associated with each menu option.
    """
    line_break()
    print("**                                Menu                                **")
    line_break()
    print("Enter 's' (search) to search for a particular book")
    print("Enter 'b' (browse) to browse the full book collection")
    print("Enter 'o' (checkout) to checkout a book")
    print("Enter 'i' (checkin) to checkin a book")
    print("Enter 'p' (purchase) to display book purchase recommendations")
    print("Enter 'log' (log file) to display the book logs")
    print("Enter 'q' (quit) to exit")
    line_break()
    feature = input(">")

    if feature == "s":
        line_break()
        bookSearch.retrieve_book_records()
        book = input("What book are you looking for?\n>")
        line_break()
        print(bookSearch.book_search(search_terms=book))
        line()
        menu()

    elif feature == "b":
        line_break()
        print("Our current catalogue:\n")
        database.lister()
        line()
        menu()

    elif feature == "o":
        line_break()
        bookCheckout.checkout()
        line()
        menu()

    elif feature == "i":
        line_break()
        return_book_id = input("What book are you trying to return?\n(Please use the book ID and NOT it's title)\n>")
        bookReturn.book_return(return_id=return_book_id)
        line()
        menu()

    elif feature == "p":
        bookSelect.weeding()
        line()
        menu()

    elif feature == "q":
        quit()

    elif feature == "log":
        line_break()
        print("The log file structure is as follows:\nID - member ID - reservation - checkout date - checkin date - # "
              "of times checked out\n")
        f = open("logfile.txt", "r")
        for record in f:
            s = record.strip()
            log = s.split(":")
            logs.append(log)
            print(log[0] + " - " + log[1] + " - " + log[2] + " - " + log[3] + " - " + log[4] + " - " + log[5])
        f.close()
        line()
        menu()

    else:
        print("\nSorry, you typed an invalid command.\nPlease try again.")
        line()
        menu()


menu()
