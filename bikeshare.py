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


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("Most common month is '",df['month'].value_counts().idxmax(),"'")

    # TO DO: display the most common day of week
    print("Most common day of week is '",df['day_of_week'].value_counts().idxmax(),"'")

    # TO DO: display the most common start hour
    print("Most common start hour is '",df['Start Time'].dt.hour.value_counts().idxmax(),"'")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("most commonly used start station is", df['Start Station'].value_counts().idxmax())

    # TO DO: display most commonly used end station
    print("most commonly used end station is", df['End Station'].value_counts().idxmax())

    # TO DO: display most frequent combination of start station and end station trip
    print("Most frequent combination of start station and end station trip is", (df['Start Station']+df['End Station']).value_counts().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    if 'Trip Duration' in df.columns:
        # TO DO: display total travel time
        print("Total travel time is- ", df['Trip Duration'].sum())

        # TO DO: display mean travel time
        print("Mean travel time is- ", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if 'User Type' in df.columns:
        print("Count of User types", pd.DataFrame(df['User Type'].value_counts()))
    
    print("")

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print("Count of Gender types", pd.DataFrame(df['Gender'].value_counts()))
        print("")
        # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print("most earliest year of birth is ", int(df['Birth Year'].head(1).values[0]) )
        print("")
        print("most recent year of birth is ", int(df['Birth Year'].tail(1).values[0]) )
        print("")
        print("Most common year of birth is ", int(df['Birth Year'].value_counts().idxmax()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    while True:
        usr_inpt = input("Would you like to display Raw Data (please type 'yes' or 'no' )\n").lower()
        if usr_inpt == 'yes':
            r1 = 0
            r2 = 5
            print(df.iloc[r1:r2,:])
            while True:
                check_inpt = input("would you like to see 5 more rows(type 'yes' or 'no')\n ").lower()
                if check_inpt == 'yes':
                    r1+=5
                    r2+=5
                    print(df.iloc[r1:r2,:])
                    continue
                elif check_inpt == 'no':
                    break
                else:
                    print("please enter a valid input\n")
                    continue
                break
            break
        elif usr_inpt == 'no':
            break
        else:
            print("Please enter a valid input \n")
            continue


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
