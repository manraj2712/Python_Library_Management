def deleteBookByIsbn():

    import openpyxl
    import pandas

    isbn = input('\nEnter the ISBN Code of the book of which you want to delete record from Stock Database\n').lower()
    option = ''
    wb = openpyxl.load_workbook('stockDatabase.xlsx')
    df = pandas.read_excel('stockDatabase.xlsx')
    sheet = wb.active

    for i in range(len(df['isbn'])):
        
        if df['isbn'][i] == isbn:
            print(df.iloc[i])
            print('\nDo you want to delete this book record?\n')
            option = input('''\nEnter 'Y' to confirm and 'N' to Exit\n''').lower()
            if(option == 'y'):
                sheet.delete_rows(i+2)
                print(f'\nBook with ISBN Code {isbn} Successfully deleted from Stock!')
                break
            else:
                break
        

    wb.save('stockDatabase.xlsx')
