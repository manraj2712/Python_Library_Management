def displayAllBooks():
    import pandas as pd

    df = pd.read_excel('stockDatabase.xlsx')
    print(df)

def displayBookByISBN():

    import pandas as pd

    isbn = input('\nEnter the book ISBN Code to see records\n').lower()

    df = pd.read_excel('stockDatabase.xlsx')
    for i in range(len(df['isbn'])):
        if df['isbn'][i] == isbn:
            print(df.iloc[i])
            break



