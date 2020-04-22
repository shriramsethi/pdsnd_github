import time
import pandas as pd
import numpy as np

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
        city = input("Would you like to see data for Chicago, New York City, or Wasington?\n").lower()
        if city not in CITY_DATA:
            print("enter a valid CITY")
            continue
        else:
            break
    # return city
    while True:
        data = input("Would you like to filter the data by month, day? type 'none' for no time filter\n ")
        if data == 'month':
            # TO DO: get user input for month (all, january, february, ... , june)
            months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
            while True:
                month = input("enter month: (all, january, february, march, april, may, june) ").lower()
                if month not in months:
                    print("enter a valid month or type 'all' \n")
                    continue
                else:
                    day = 'none'
                    break
        elif data == 'day':
            # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
            days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'firday', 'saturday', 'sunday']
            while True:
                day = input("enter day: ((all, monday, tuesday, ... sunday) \n").lower()
                if day not in days:
                    print("enter a valid day or type 'all' \n")
                    continue
                else:
                    month = 'none'
                    break
        elif data == 'none':
            month = 'none'
            day = 'none'
        else:
            print("please enter a valid input:\n")
            continue
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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'none' and day == 'none':
    # filter by month if applicable
        if month != 'all':
            # # use the index of the months list to get the corresponding int
            # months = ['january', 'february', 'march', 'april', 'may', 'june']
            # month = months.index(month) + 1

            # filter by month to create the new dataframe
            df = df[df['month'] == month.title()]
    if month == 'none' and day != 'none':
        # filter by day of week if applicable
        if day != 'all':
            # filter by day of week to create the new dataframe
            df = df[df['day_of_week'] == day.title()]

    return df.dropna().reset_index(drop=True)
    # return df.fillna("Not Available", inplace = True)





def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
