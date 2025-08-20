This code was written using the latest version of PyCharm.

The code is intended to be run in IDLE (or any other compatible compilers) and from the menu.py file.

The code functions under certain assumptions:
1. The program assumes all books haver been checked out and checked in at least once (hence the log file entries for all books).
2. The program assumes a book cannot be checked out and returned on the same day.
3. The program asumes it is closed until it is needed (i.e. the user must quit the program after each entry into the logfile to save the changes)


I'm particularly proud of the reservation feature. The feature allows the user to enter their ID and reserve a book that has been checked out but not checked in (returned) yet. Once a reservation has been requested, the program checks the conditions that would allow the book to be reserved. If the specific user has already checked out that specific book then the program informs the user. Otherwise a new line in the log file is created with the date of reservation and the member ID of the person who reserved the book. The member ID system is also something I'm proud of. It uses the "try...except" statement type to check if the ID input is valid before returning a potential error.
