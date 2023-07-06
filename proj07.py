##############################################################
    #  Computer Project #7
    #
    #  Open file function
    #   Takes input for what file
    #       Try/ except to see if file opens with adding csv
    #           returns file and returns cities
    #  Read file function
    #   Iterate through cities
    #       Use try except to see if varible is in file, if not assign to None
    #       Create tuple
    #   Append tuple to list
    #   return list
    #  Get data in range function
    #   Define all varibles
    #   Use for loop to iterate through data 
    #       for loop to iterate through ach line 
    #           Appends date to list
    #   return dates in between start and end date
    #  Find max function
    #   If the number is greater than the max in the column
    #       return max and city name in a list
    #  Find min function
    #   If the number is smaller than the min in the column
    #       return min and city name in a list
    #  Find average function
    #   define varibles and count
    #   If the number is greater than the max in the column
    #       Define average by adding up items in list the divide by count   
    #   return average and city name in a list
    #  Get modes function
    #   Define list
    #   Use for loop to iterate through data
    #       Iterate through list of cities created
    #           Calculate/find N1 and N2 values
    #       Iterate through modes list created
    #           append correct values to list
    #   return list
    #  High low averages function
    #   Iterate through categories given
    #       If the category is listed
    #           Use get average function 
    #           Find the high and low averages
    #       else
    #           Append nothing to the list
    #   Return list of tuples
    #  Display stats function
    #   Iterate through data
    #       define all previous functions 
    #       create print statements to display data correctly
    #  Main function
    #   Define menu options 
    #   If statement for error message
    #       print error statement and menu options
    #   Intiate while loop for when the option is not 7
    #       Initiate if loop for every option
    #           Call necessay functions to the main function in each option
    #           Print statemnets for options
    #           Print menu options 
    #    Display closing message
##############################################################

import csv
from datetime import datetime
from operator import itemgetter

COLUMNS = ["date",  "average temp", "high temp", "low temp", "precipitation", \
           "snow", "snow depth"]

TOL = 0.02

BANNER = 'This program will take in csv files with weather data and compare \
the sets.\nThe data is available for high, low, and average temperatures,\
\nprecipitation, and snow and snow depth.'    

MENU = '''
        Menu Options:
        1. Highest value for a specific column for all cities
        2. Lowest value for a specific column for all cities
        3. Average value for a specific column for all cities
        4. Modes for a specific column for all cities
        5. Summary Statistics for a specific column for a specific city
        6. High and low averages for each category across all data
        7. Quit
        Menu Choice: '''
        
def open_files():
    """
    Opens the file and has error checking

    Returns
    -------
    list_strings : List
        The list of cities.
    fp_list : List
        The file pointer.

    """
    cities = input("Enter cities names: ")
    cities_l = cities.split(",")
    fp_list = []
    list_strings = []
    for city in cities_l:
        #Add csv to city name to search for city
        #Use try/except, if not found print error message
        file = city + ".csv"
        try:    
            fp= open(file, "r", encoding="utf-8")
            fp_list.append(fp)
            list_strings.append(city)
        except:    
            print("\nError: File {} is not found".format(file))
    return list_strings, fp_list
    
def read_files(cities_fp):
    """
    Reads the file and assigns a value to a varible

    Parameters
    ----------
    cities_fp : List
        List of cities provided.

    Returns
    -------
    list_of_list_tuples : List
        A list that contains tuples of each varible with value.

    """
    list_of_list_tuples = []
    for fp in cities_fp:
        reader = csv.reader(fp)
        next(reader)
        next(reader)
        list_tuple =[]
        #Try/except to see if varible can be converted to given type, if not assigned to None
        for line in reader:
            try:
                date = str(line[0])
            except:
                date = None
            try:
                tavg = float(line[1])
            except:
                tavg = None
            try:
                tmax = float(line[2])
            except:
                tmax = None
            try:
                tmin = float(line[3])
            except:
                tmin = None
            try:
                prcp = float(line[4])
            except:
                prcp = None
            try:
                snow = float(line[5])
            except:
                snow = None
            try:
                snwd = float(line[6])
            except:
                snwd = None
            #Create tuple of varibles and append it to list
            tuplex = (date,tavg,tmax,tmin,prcp,snow,snwd)
            list_tuple.append(tuplex)
        list_of_list_tuples.append(list_tuple)
    return list_of_list_tuples           
    
def get_data_in_range(data, start_date_str, end_date_str):
    """
    Gets the dates in between the start and end date

    Parameters
    ----------
    data : List
        The data list to extract from.
    start_date_str : str
        The start date.
    end_date_str : str
        The end date.

    Returns
    -------
    filtered_data : List
        A list of list of tuples that returns the dates.

    """
    #Initializes start and end date
    start_date = datetime.strptime(start_date_str, "%m/%d/%Y").date()
    end_date = datetime.strptime(end_date_str, "%m/%d/%Y").date()
    filtered_data = []
    for line in data:
        #Checks to see if date is in between start and end date 
        date = []
        for item in line:
            item_date = datetime.strptime(item[0], "%m/%d/%Y").date()
            if start_date <= item_date <= end_date:
                date.append(item)
        filtered_data.append(date)
    return filtered_data


def get_min(col, data, cities): 
    """
    Gets the minumum value of data from respective column

    Parameters
    ----------
    col : int
        The column number that is inputted.
    data : list
        The data list to extract from.
    cities : list
        The cities the user wants to see.

    Returns
    -------
    city_list : list
        A list with city and minimum value asscoiated.

    """
    #Create a counter for indexing cities
    #Loops to search through data and respective column provided
    #Find the minimum value and city and append to list
    c=0
    city_list=[]
    for list1 in data:
        min_val = 99999999
        for tuples in list1:
            for city in cities:
                if tuples[col] != None and tuples[col] < min_val:
                    min_val = tuples[col]
                city_tuple = (cities[c], min_val)
        c+=1
        city_list.append(city_tuple)
    return city_list
            
def get_max(col, data, cities): 
    """
    Gets the maximum value of data from respective column

    Parameters
    ----------
    col : int
        The column number that is inputted.
    data : list
        The data list to extract from.
    cities : list
        The cities the user wants to see.

    Returns
    -------
    city_list : list
        A list with city and maximum value asscoiated.

    """
    #Create a counter for indexing cities
    #Loops to search through data and respective column provided
    #Find the max value and city and append to list
    c=0
    city_list=[]
    for list1 in data:
        max_val = 0
        for tuples in list1:
            for city in cities:
                if tuples[col] != None and tuples[col] > max_val:
                    max_val = tuples[col]
                city_tuple = (cities[c], max_val)
        c+=1
        city_list.append(city_tuple)
    return city_list

def get_average(col, data, cities): 
    """
    Gets the average value of data from respective column

    Parameters
    ----------
    col : int
        The column number that is inputted.
    data : list
        The data list to extract from.
    cities : list
        The cities the user wants to see.

    Returns
    -------
    city_list_avg : list
        A list with city and average value asscoiated.

    """
    #Create a counter for indexing cities
    #Loops to search through data and respective column provided
    #Find the average value and city and append to list
    c=0
    city_list_avg =[]
    for list1 in data:
        total = 0
        count = 0
        for tuples in list1:
            for city in cities:
                if tuples[col] != None:
                    total += tuples[col]
                    count +=1
                    avg = total/count
                city_tuple = (cities[c], round(avg, 2))
        c+=1
        city_list_avg.append(city_tuple)
    return city_list_avg

def get_modes(col, data, cities): 
    """
    Gets the modes, occurences, asscoiated with each city

    Parameters
    ----------
    col : int
        The column number that is inputted.
    data : list
        The data list to extract from.
    cities : list
        The cities the user wants to see.

    Returns
    -------
    master_list : List
        A list of tuples that contains the city, a list with the modes, and occurences.

    """
    master_list = []
    for city_index, city_data in enumerate(data):
        city_list = []
        for row in city_data:
            if row[col] is not None:
                city_list.append(row[col])
        city_list.sort()
        modes = []
        count = 1
        N1 = city_list[0]
        for val in city_list[1:]:
            if N1 == 0:
                N1 = val
                continue
            N2 = val
            if abs((N1 - N2) / N1) <= TOL:
                count += 1
            else:
                modes.append((N1, count))
                N1 = N2
                count = 1
        if (N1, count) not in modes:
            modes.append((N1, count))
        modes = sorted(modes, key=itemgetter(1), reverse=True)
        mode = modes[0][1]
        mode_list = []
        for elem in modes:
            if elem[1] == mode:
                mode_list.append(elem[0])
        if mode == 1:
            master_list.append((cities[city_index], [], 1))
        else:
            master_list.append((cities[city_index], mode_list, mode))
    return master_list
          
def high_low_averages(data, cities, categories): 
    """
    A function that finds the high and low averages in each colum for respecrive cities

    Parameters
    ----------
    data : List
        The data list to extract from.
    cities : List
        The cities the user wants to see.
    categories : str
        The category the user wants to look at.

    Returns
    -------
    list_of_lists_of_tuples : List
        A list of lists of tuples that has respective cities and associated high and low averages.

    """
    list_of_lists_of_tuples = []
    for category in categories:
        category = category.lower()
        list_tuples = []
        if category in COLUMNS:
            v = COLUMNS.index(category)
            avg_l = get_average(v, data, cities)
            L_avg = 99999
            H_avg = 0
            for tuplex in avg_l:
                if tuplex[1] > H_avg:
                    H_avg_name = tuplex[0]
                    H_avg = tuplex[1]
                if tuplex[1] < L_avg:
                    L_avg_name = tuplex[0]
                    L_avg = tuplex[1]
            if L_avg is not None:
                L_avg_tuple = (L_avg_name, L_avg)
            if H_avg is not None:
                H_avg_tuple = (H_avg_name, H_avg)
                list_tuples.append(L_avg_tuple)
                list_tuples.append(H_avg_tuple)
                list_of_lists_of_tuples.append(list_tuples)
        else:
            list_of_lists_of_tuples.append(None)
    return list_of_lists_of_tuples

def display_statistics(col, data, cities): 
    """
    Displays the data from a city.

    Parameters
    ----------
    col : int
        The column number that is inputted.
    data : list
        The data list to extract from.
    cities : list
        The cities the user wants to see.

    Returns
    -------
    None.

    """
    c = 0
    for List in data:
        maximum = get_max(col, data, cities)
        minimum = get_min(col, data, cities)
        average = get_average(col, data, cities)
        modes = get_modes(col, data, cities)
        print("\t{}: ".format(cities[c]))
        print("\tMin: {:.2f} Max: {:.2f} Avg: {:.2f}".format(minimum[c][1], maximum[c][1], average[c][1]))
        if modes[c][2] == 1:
            print("\tNo modes.")
        if modes[c][2] != 1:
            codes = (map(str, modes[c][1]))
            print("\tMost common repeated values ({:d} occurrences): {:s}\n".format(modes[c][2], ",".join(codes)))
        c += 1
             
def main():
    """
    The user imputs option and prints respective option    

    Returns
    -------
    None.

    """
    #Call open file and read file
    print(BANNER)
    list_strings, fp_list = open_files()
    option = input(MENU)
    codes = ("1","2","3","4","5","6","7")
    list_of_list_tuples = read_files(fp_list)
    #while loop if option is not 7
    while option != "7":
        #Error checking to see if option is not a vaild option
        if option not in codes:
            print("Invalid menu option!!! Please try again!")
            print(MENU)
            option = input("")
        if option == "1":
            #Intialize necessary imputs
            #Call get data in range and get max
            #Reprompt for option
            starting_date = input("\nEnter a starting date (in mm/dd/yyyy format): ")
            ending_date = input("\nEnter an ending date (in mm/dd/yyyy format): ")
            catagory = input("\nEnter desired category: ")
            catagory = catagory.lower()
            filtered_data = get_data_in_range(list_of_list_tuples, starting_date, ending_date)
            #Error checking if the category does not exist
            while catagory not in COLUMNS:
                print("\n\t{} category is not found.")
                catagory = input("\nEnter desired category: ")
            col = COLUMNS.index(catagory)
            city_list = get_max(col, filtered_data, list_strings)
            print("\n\t{}: ".format(catagory))
            for tuplex in city_list:
                print("\tMax for {:s}: {:.2f}".format(tuplex[0], tuplex[1]))
            option = input(MENU)
        if option == "2":
            #Intialize necessary imputs
            #Call get data in range and get min
            #Reprompt for option
            starting_date = input("\nEnter a starting date (in mm/dd/yyyy format): ")
            ending_date = input("\nEnter an ending date (in mm/dd/yyyy format): ")
            catagory = input("\nEnter desired category: ")
            catagory = catagory.lower()
            filtered_data = get_data_in_range(list_of_list_tuples, starting_date, ending_date)
            while catagory not in COLUMNS:
                print("\n\t{} category is not found.")
                catagory = input("\nEnter desired category: ")
            col = COLUMNS.index(catagory)
            city_list = get_min(col, filtered_data, list_strings)
            print("\n\t{}: ".format(catagory))
            for tuplex in city_list:
                print("\tMin for {:s}: {:.2f}".format(tuplex[0], tuplex[1]))
            option = input(MENU)
        if option == "3":
            #Intialize necessary imputs
            #Call get data in range and get average
            #Reprompt for option
            starting_date = input("\nEnter a starting date (in mm/dd/yyyy format): ")
            ending_date = input("\nEnter an ending date (in mm/dd/yyyy format): ")
            catagory = input("\nEnter desired category: ")
            catagory = catagory.lower()
            filtered_data = get_data_in_range(list_of_list_tuples, starting_date, ending_date)
            while catagory not in COLUMNS:
                print("\n\t{} category is not found.")
                catagory = input("\nEnter desired category: ")
            col = COLUMNS.index(catagory)
            city_list = get_average(col, filtered_data, list_strings)
            print("\n\t{}: ".format(catagory))
            for tuplex in city_list:
                print("\tAverage for {:s}: {:.2f}".format(tuplex[0], tuplex[1]))
            option = input(MENU)
        if option == "4":
            #Intialize necessary imputs
            #Call get data in range and get modes
            #Reprompt for option
            starting_date = input("\nEnter a starting date (in mm/dd/yyyy format): ")
            ending_date = input("\nEnter an ending date (in mm/dd/yyyy format): ")
            catagory = input("\nEnter desired category: ")
            catagory = catagory.lower()
            filtered_data = get_data_in_range(list_of_list_tuples, starting_date, ending_date)
            while catagory not in COLUMNS:
                print("\n\t{} category is not found.")
                catagory = input("\nEnter desired category: ")
            col = COLUMNS.index(catagory)
            city_list = get_modes(col, filtered_data, list_strings)
            print("\n\t{}: ".format(catagory))
            #For loop to iterate through city list created, prints indexed strings
            for tuplex in city_list:
                code =map(str, tuplex[1])
                print("\tMost common repeated values for {:s} ({:d} occurrences): {:s}\n".format(tuplex[0],tuplex[2], ",".join(code)))
            option = input(MENU)
    
        if option == "5":
            #Intialize necessary imputs
            #Call get data in range and display stats
            #Reprompt for option
            starting_date = input("\nEnter a starting date (in mm/dd/yyyy format): ")
            ending_date = input("\nEnter an ending date (in mm/dd/yyyy format): ")
            catagory = input("\nEnter desired category: ")
            catagory = catagory.lower()
            filtered_data = get_data_in_range(list_of_list_tuples, starting_date, ending_date)
            while catagory not in COLUMNS:
                print("\n\t{} category is not found.".format(catagory))
                catagory = input("\nEnter desired category: ")
                catagory = catagory.lower()
            col = COLUMNS.index(catagory.lower())
            print("\n\t{}: ".format(catagory))
            #No print statements because already in function
            display_statistics(col, filtered_data, list_strings)
            option = input(MENU)
            
        if option == "6": 
            #Intialize necessary imputs
            #Call get data in range and high low averages
            #Reprompt for option
            #Create counter to index through cities 
            C = 0
            starting_date = input("\nEnter a starting date (in mm/dd/yyyy format): ")
            ending_date = input("\nEnter an ending date (in mm/dd/yyyy format): ")
            filtered_data = get_data_in_range(list_of_list_tuples, starting_date, ending_date)
            catagories = input("\nEnter desired categories seperated by comma: ")
            catagories = catagories.split(",")
            filtered_data = high_low_averages(filtered_data, list_strings, catagories)
            print("\nHigh and low averages for each category across all data.")
            #Iterate through high low averages
            #Create error checking if the lists exists
            for List in filtered_data:
                if List is None:
                    print("\n\t{} category is not found.".format(catagories[C].lower()))
                else:
                    print("\n\t{}: ".format(catagories[C].lower()))
                    print("\tLowest Average: {:s} = {:.2f} Highest Average: {:s} = {:.2f}".format(List[0][0], List[0][1], List[1][0], List[1][1]))
                C += 1
            option = input(MENU)
    #Print closing statement
    print("\nThank you using this program!") 

if __name__ == "__main__":
    main()