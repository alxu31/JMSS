#Sets the data export location.
with open("CasesPrev.csv", 'w') as outFile:
    nCases = 7769783
    #Change the a value to get a result of 12741386 cases.
    a = 0.01782170171
    for i in range(28):
        nCases += a*nCases
    isolation = 0
    print(nCases)
    #Finds the number of cases every day between 8/6/2020 and 31/12/2020 and exports them to an excel spreadsheet.
    nCases = 7769783
    print(f"0, {int(nCases)}", file = outFile)
    for i in range(206):
        nCases += a*nCases - isolation*nCases
        print(f"{i+1}, {int(nCases)}", file = outFile)
        isolation += 0.0002
    #Prints the number of cases at the end of the year.
    print(nCases)

    #Finds how many days after 8/6/2020 it takes to reach 0 cases.
    nCases = 7769783
    isolation = 0
    for i in range(9999):
        nCases += a*nCases - isolation*nCases
    
        isolation += 0.0002
        if nCases <= 0:
            print(f"At {i} days there are 0 Cases")
            break
