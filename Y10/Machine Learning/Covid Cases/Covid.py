#Sets the data export location.
with open("Cases.csv", 'w') as outFile:
    nCases = 7769783
    #Change the a value to get a result of 12741386 cases.
    a = 0.01782170171
    for i in range(28):
        nCases += a*nCases

    print(nCases)
    nCases = 7769783
    #Finds the number of cases every day between 8/6/2020 and 31/12/2020 and exports them to an excel spreadsheet.
    print(f"0, {int(nCases)}", file = outFile)
    for i in range(206):
        nCases += a*nCases
        print(f"{i+1}, {int(nCases)}", file = outFile)
    #Prints the number of cases at the end of the year.
    print(nCases)
    
    


