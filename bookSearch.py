"""
Module which contains functions used to allow librarian to
input search terms as strings, and returns a table of books matching the
search query.
"""

records = []


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


def book_search(search_terms):
    """
    This function handles the searching of book titles in the library.

    param search_terms: the search terms the user requests from the menu
    """
    for record in records:
        if record[2] == search_terms or record[3] == search_terms or record[0] == search_terms:
            return "Here is the book:\n%s by %s (A %s book)\nFor sale online for £%s\nBook ID --> %s\n" % (record[2], record[3], record[1], record[4], record[0])
    return "I'm sorry, it appears we couldn't find what you were searching for."
