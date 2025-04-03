import pandas as pd



def main():

        #select csv files
        file1 = input("Submit the name of your CSV file (exclude file extension)")
        file2 = input("Submit the name of a second CSV file (exclude file extension)")
        #create data frames
        try:
            df = pd.read_csv(f'{file1}.csv')
        except FileNotFoundError:
            print(f"{file1}.csv was not found in this directory. Check spelling or try moving the file to the correct location.")
            print("Restarting...")
            main()
        except pd.errors.EmptyDataError:
            print(f"{file1}.csv is empty. Try another file.")
            print("Restarting...")
            main()
        try:
            df2 = pd.read_csv(f'{file2}.csv')
        except FileNotFoundError:
            print(f"{file2}.csv was not found in this directory. Check spelling or try moving the file to the correct location.")
            print("Restarting...")
            main()
        except pd.errors.EmptyDataError:
            print(f"{file2}.csv is empty. Try another file.")
            print("Restarting...")
            main()    
        #select key column
        key = input("Enter the title of a common column which both datasets will merge on.")
        #merge two data frames based on common key
        try:
            df3 = pd.merge(df,df2,on=key)
        except KeyError:
            print(f'{key} is not a column that exists in both files. Please try again.')
            key = input("Enter the title of a common column which both datasets will merge on.")
            try:
                df3 = pd.merge(df,df2,on=key)
            except KeyError:
                print(f'{key} is not a column that exists in both files.')
                print('Restarting...')
                main()
        def Columns():
            #contains a list of column names
            columnList = []
            #total number of columns
            cNum = 0
            a = input ("Would you like to keep all columns from both files? If not, please answer with 'no'.")
            if a == 'no':
                while cNum == 0:
                    try:
                        num = input("How many columns would you like to keep?")
                        cNum = int(num)
                    except ValueError:
                        print("Value must be an integer.")
                #collect column names
                for i in range (0,cNum,1):
                    x = input("Enter a column name")
                    columnList.append(x)
            return columnList
        columnList = Columns()  
        #if list is not empty
        if columnList != []:
            #create and print a new dataframe with just the columns from this list
            try:
                contacts = df3[columnList]
                print(f'{contacts.to_string()}')
            #unless if one or more columns could not be found
            except KeyError:
                print("One or more of these column names do not exist.")
                print("Restarting...")
                main()
        else:
            contacts = df3
            print(f'{contacts.to_string()}')

        def exportQ():
            export_question = input("Would you like to export this output to a csv file (recommended)? Please answer with 'yes' or 'no'.")
            if export_question != 'yes' and export_question != 'no':
                print("Invalid input. Please answer with 'yes' or 'no'.")
                exportQ()
            elif export_question == 'yes':
                #ask for file name
                name = input("What would you like to name this file?")
                #export to csv
                contacts.to_csv(f'{name}.csv')
                print(f'{name}.csv has been saved to this directory.')
                restart = input("Would you like to start over? Please answer with 'yes' or 'no'.")
                if restart != 'yes' and restart != 'no':
                    print("Invalid input. Please answer with 'yes' or 'no'.")
                    exportQ()
                elif restart == 'yes':
                    main()
                elif restart == 'no':
                    print("Goodbye.")
                    main()
                    exit()
                    
            elif export_question == 'no':
                restart = input("Would you like to start over? Please answer with 'yes' or 'no'.")
                if restart != 'yes' and restart != 'no':
                    print("Invalid input. Please answer with 'yes' or 'no'.")
                    exportQ()
                elif restart == 'yes':
                    main()
                elif restart == 'no':
                    print("Goodbye.")
                    exit()
        exportQ()
main()
