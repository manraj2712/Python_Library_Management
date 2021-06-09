def deleteBookByIsbn():

    import openpyxl
    import pandas

    isbn = input('Enter the ISBN Code of the book of which you want to delete record from Stock Database\n').lower()
    option = ''
    wb = openpyxl.load_workbook('C:\\Users\\Manraj\\Desktop\\python project lib management\\stockDatabase.xlsx')
    df = pandas.read_excel('C:\\Users\\Manraj\\Desktop\\python project lib management\\stockDatabase.xlsx')
    sheet = wb.active

    for i in range(len(df['isbn'])):
        
        if df['isbn'][i] == isbn:
            print(df.iloc[i])
            print('Do you want to delete this book record?')
            option = input('''Enter 'Y' to confirm and 'N' to Exit''').lower()
            if(option == 'y'):
                sheet.delete_rows(i+2)
                break
            else:
                break
        

    wb.save('stockDatabase.xlsx')
