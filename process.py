log_file = open("um-server-01.txt") #Opens up a text file that is stored in a variable called log_file


def sales_reports(log_file): #Creates a function named sales reports that takes in one file parameter called log_file
    for line in log_file: #Creates a for loop that begins inside the log_file
        line = line.rstrip() #Removes all whitespace
        day = line[0:3] #Stores the first three characters in a string variable called day
        if day == "Mon": #If the three characters match the word "Mon"
            print(line) #print out the whole line


sales_reports(log_file) #Calls the function so that the above code runs
