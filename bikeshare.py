import time
import pandas as pd
import numpy as np
import statistics as Stdd
import datetime


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
          
    while True:
        print("Please enter the city that you want to view?\n")
        print("Options: chicago,new york city,washington")
        city=input()
        if city!='chicago' and city!='new york city' and city!='washington':
                    print('\n Oops... Invalid city, please select Again')
        else:
            break
                                  
    # TO DO: get user input for month (all, january, february, ... , june)

    print('\n Enter month please')
    print('\n Options: all,january,february,march,april,may,june' )
        
        month=input()
        if month!='all' and month!='january' and month!='february'  and month!='march'  and month!='april'  and month!='may'  and month!='june':
                    print('\n Oops... Invalid month, please select Again')
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    print('\n Enter day you want to analyse')
    print('\n Options: all,monday,tuesday,wednesday,thursday,friday,saturday,sunday')
    
    day=input()
        if day!='all' and day!='monday' and day!='tuesday'  and day!='wednesday'  and day!='thursday'  and day!='friday'  and day!='saturday' and day!='sunday':
                    print('\n Oops... Invalid day, please select Again')
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

    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

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

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print("\nCalculating The Most Frequent Times of Travel...\n")
    start_time = time.time()

    # TO DO: display the most common month
    print("\n the most common month is")
    print(list(df['month'].mode()))

    # TO DO: display the most common day of week

    most_common_day = df['day_of_week'].value_counts().idxmax()
    print("\n the most common day is ")   
    print("The most common day of week is :", most_common_day_of_week)    
    
    # TO DO: display the most common start hour

    hour_mode=[]
    for i in range(24):
          hour_mode.append(0)
    for i in range(len(df)):
          ii=df['hour'][i]
          hour_mode[ii]+=df['Trip Duration'][i]
    
    print("\n the most common start hour is ")   
    print(hour_mode.index(max(hour_mode))+1)
 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    print('\n Most commonly used (start station) ')
    print(df['Start Station'].mode())
    
    # TO DO: display most commonly used end station

    print('\n Most commonly used (end station) ')
    print(df['End Station'].mode())

    # TO DO: display most frequent combination of start station and end station trip

    trip=[]
    for i in range(len(df)):
    trip.append((df['Start Station'][i],df['End Station'][i]))
    print('\n frequent combination of start-End station ')
    print(max(trip,key=trip.count))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
   
    total_travel = df['Trip Duration'].sum()
    print("Total travel time :", total_travel)
    
    # TO DO: display mean travel time
    print('\n mean travel time: ')
    print(Stdd.mean(df['Trip Duration']))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\n counts of user types: ')
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    print('\n counts of gender: ')
    print(df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    print("\n earliest year of birth")
    print(max(df['Birth Year']))
 
    print("\n most recent year of birth")
    print(min(df['Birth Year']))     
 
    print("\n most common year of birth")
    print(df['Birth Year'].mode())  

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

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
# this is an example of the change you could do so try it!

    
