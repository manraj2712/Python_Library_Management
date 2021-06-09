def displayAllBooks():
    import pandas as pd

    df = pd.read_excel('stockDatabase.xlsx')
    print(df)

def displayBookByName():

    import pandas as pd

    bookName = input('Enter the book name to see records\n').lower()
    index = -1

    df = pd.read_excel('stockDatabase.xlsx')
    for i in range(len(df['book name'])):
        if df['book name'][i] == bookName:
            index = i
            break
    
    print(df.iloc[index])



