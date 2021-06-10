import add
import display
import issue
import deleteBook
import returnBook

option = 1
while(option):
    print("\t\t\t\t----------Welcome to TMU Central Library----------")
    print('''\n\n\n\t\t\t\tChoose from the following options to start\n
    1. To add a new Book to Stock\n
    2. To display the records of all Books in Stock\n
    3. To display the records of a specific Book in Stock by ISBN\n
    4. To Return a book using ISBN and Student Id\n
    5. To issue a book using Student Id and ISBN Code\n
    6. To calculate fine on Student ID\n
    7. To Delete a book record from stock database\n
    0. To exit out of the ''')

    option = int(input())

    if(option == 0):
        break
    elif(option == 1):
        add.addBook()
    elif(option == 2):
        display.displayAllBooks()
    elif(option == 3):
        display.displayBookByISBN()
    elif(option == 4):
        returnBook.returnBookByIsbn()
    elif(option == 5):
        issue.issueBook()
    elif(option == 6):
        returnBook.fineByStudentId()
    elif(option == 7):
        deleteBook.deleteBookByIsbn()
    else:
        print('Enter a valid option!')
        break
    
