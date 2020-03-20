import time
import pandas as pd
import numpy as np

#testin these files in my local environment
CITY_DATA = { 'chicago': 'C:/python_scripts/chicago.csv',
              'new york city': 'new_york_city.csv',
             'washington': 'C:/python_scripts/washington.csv' }
#CITY_DATA = { 'chicago': 'chicago.csv',
#              'new york city': 'new_york_city.csv',
#              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    #list to validate the input from user against these city names.
    city_list = ['chicago', 'new york city', 'washington'] 
    month_list = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    day_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday', 'all']
    
    #Used stack overflow to be able to validate user inputs 
    while True:
        city = input("Would you like to see data for Chicago, New York City or Washington? ").lower()
        if city not in city_list:
            print("This is not a valid city. Please enter: Chicago, New York City or Washington.")
        else:
            break
    
    while True:
        filter_mon_day = input("Would you like to filter the data by month, day or both.? ").lower()
        if filter_mon_day not in ('month', 'day', 'both'):
            print("This is not a valid filter. Please enter: month, day or both.")
        else:
            break
            
    # TO DO: get user input for month (all, january, february, ... , june)
      
    if filter_mon_day == "month":
        while True:
            month = input("Enter a valid month: January, February, March, April, May or June or all: ").lower()
            if month not in month_list:
                print("This is not a valid month. Please enter: January, February, March, April, May or June or all")  
            else:
                break
                
        day = "all"
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        
    if filter_mon_day == "day":
        month = "all"
        while True:
            day = input("Enter a valid day: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday or all: ").lower()
            if day not in day_list:
                print("This is not a valid day. Please enter: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday or all")
            else:
                break
                
        
    
    # TO DO: get user input for both month and day.   
        
    if filter_mon_day == "both":
        #month = input("Enter a valid month: January, February, March, April, May or June or all: ").lower()
        while True:
            month = input("Enter a valid month: January, February, March, April, May or June or all: ").lower()
            if month not in month_list:
                print("This is not a valid month. Please enter: January, February, March, April, May or June or all") 
            else:
                break
                
        while True:
            day = input("Enter a valid day: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday or all: ").lower()
            if day not in day_list:
                print("This is not a valid day. Please enter: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday or all")
            else:
                break        
                

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #Used the practice#3 from Project solution here to convert time columns to month and weekday_name
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        #print('this is the month', month)
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df
  


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    #Use practice#1 solution mode method to obtain popular month, day of week and hour
    df_common_month = df['month'].mode()[0]
    #use dictionary to loop through each month key to get the value/name to display
    months= {1:'january', 2:'february', 3:'march', 4:'april', 5:'may', 6:'june'}

    for num, name in months.items():
        if df_common_month == num:
            #print(months[num])
            print("The most common month is: {}".format(months[num].title()))
     
    # TO DO: display the most common day of week
    df_common_day = df['day_of_week'].mode()[0]
    print("The most common day of the week is: {}".format(df_common_day))
    
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("The most common start hour is: {}".format(popular_hour))
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is: ", start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print("The most commonly used end station is: ", end_station)
    
    #Consulted with mentor on how to get the most popular combination of start and end station
    # TO DO: display most frequent combination of start station and end station trip
    start_end_station = df.groupby(['Start Station', 'End Station']).count().sort_values('Start Time')
    print("The most frequent combination of start station and end station trip:")
    print('Count: ', start_end_station['Start Time'].iloc[-1])
    print(start_end_station.index.values[-1]) 
  
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print("Total Time traveled is: ", total_travel)

    # TO DO: display mean travel time
    avg_travel = df['Trip Duration'].mean()
    print("Average Time traveled is: ", avg_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    Users = df['User Type'].value_counts()
    print("What is the breakdown of Users:\n")
    print(Users)
    
    # TO DO: Display counts of gender
    print("\nWhat is the breakdown of Gender:\n")
    if 'Gender' in  df.columns:
        Gender = df['Gender'].value_counts()
        print(Gender)
    else:
        print("No gender data to share")
        
    # TO DO: Display earliest, most recent, and most common year of birth
    print("\nWhat is the oldest, youngest and most popular year of birth:\n")
    if 'Birth Year' in df.columns:
        Birth_max = int(df['Birth Year'].max())
        Birth_min = int(df['Birth Year'].min())
        Birth_common = int(df['Birth Year'].mode()[0])
        print("The oldest year of birth is: {}, the youngest is: {} and the most popular is: {}".format(Birth_min, Birth_max, Birth_common))
    else:
        print("No birth year data to share")
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
            
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        #initilize these values to print 5 records at a time
        a = 0
        b = 5
        #drop these columns, so we only display existing columns in the dataframe. Not the ones we use for filter.
        df.drop(['month', 'day_of_week', 'hour'], axis=1, inplace=True)
        
        #get user input to display data
        raw_data = input("\nWould you like to see the raw data? Enter yes or no.\n").lower()
        while raw_data != 'no':
       
            #print the 5 records
            #Consulted with mentor to use .to_dictto display records in dictionary format
            print(df.iloc[a:b].to_dict(orient = 'records'))
            a += 5 
            b += 5
            #ask again the user to display the next 5 records
            raw_data = input("\nWould you like to see the next 5 rows of data? Enter yes or no.\n")
            
               
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
