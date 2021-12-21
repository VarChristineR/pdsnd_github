import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS_DATA = { 'january', 'february', 'march', 'april', 'may', 'june', 'all' }
DAYS_DATA = { 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all' }

"""Ask the user for their name."""
name = input("Enter your name: ")
"""Greet the user by their name"""
print("Hello there, {}!".format(name.title()))

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Let\'s explore some US bikeshare data!')

    city = input("Please specify a city to analyze, from Chicago, Washington or  New York City ").lower()
    while True:
        #Get city choice
        if city not in (CITY_DATA):
            print("You can only choose from between Chicago, Washington or New York City")
            city = input("Please specify a city to analyze, from Chicago, Washington or  New York City ").lower()
        else:
            print("You have selected {}!".format(city.title()))
            break

    month = input("Please select a month to analyze or alternativly enter all to select all months: ").lower()
    while True:
        #Get month choice
        if month not in (MONTHS_DATA):
            print("You can only choose from between January, February, March, April, May, June, or choose All to see data for all 6 months")
            month = input("Please select a month to analyze or alternativly enter all to select all months: ").lower()
        else:
            print("You have selected {}!".format(month.title()))
            break

    day = input("Please select a day to analyze or enter all to select all days: ").lower()
    while True:
        #Get day option
        if day not in (DAYS_DATA):
            print("You now need to select an individual day")
            print("You can choose from Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday. You can alternativly select All for data covering all 7 days")
            day = input("Please select a day to analyze or enter all to select all days: ").lower()
        else:
            print("You have selected {}!".format(day.title()))
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
    df['End Time'] = pd.to_datetime(df['End Time'])


    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name

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
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print("Most Frequent Start Month:", popular_month)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("Most Frequent Start Hour:", popular_hour)
    #df['Start Time'] = pd.to_datetime(df['Start Time'])

    # edisplay the most common day of the week
    df['day'] = df['Start Time'].dt.day
    popular_day = df['day'].mode()[0]
    print("Most Frequent Start Day:", popular_day)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print("\nCalculating The Most Popular Stations and Trip...\n")
    start_time = time.time()

    # display most commonly used start station
    popular_startstation = df['Start Station'].mode()[0]
    # display most commonly used end station
    popular_endstation = df['End Station'].mode()[0]
    # display most frequent combination of start station and end station trip
    popular_combo = df.groupby(['Start Station','End Station']).count()


    print("Most Frequent Start Station: ", popular_startstation)
    print('-'*40)

    print("Most Frequent End Station: ", popular_endstation)
    print('-'*40)

    print("Most Common Station Combination: ", popular_combo)
    print('-'*40)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print("\nCalculating Trip Duration...\n")
    start_time = time.time()

    # display total travel time
    total_travel = df['Trip Duration'].mode()[0]
    print("Total Travel Time: ", total_travel)


    # display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    print("Average Travel Time: ", avg_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print("\nCalculating User Stats...\n")
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()

    print("Count of User types:",user_types)
    print('-'*40)    # Display counts of gender

    #while city != 'Washington'
    if "Gender" in df.columns:
        gender_count = df['Gender'].value_counts()
        print("Count of Gender type:",gender_count)
        print('-'*40)
    else:
        print("Washington does not have any Gender data")
    # Display earliest, most recent, and most common year of birth
    #while city != 'Washington'
    if "Birth Year" in df.columns:
        earliest_birth_year = df['Birth Year'].min()
        print("Oldest Birth year: ",earliest_birth_year)
        print('-'*40)
    else:
        print("Washington does not have any Oldest birth year data")

    if "Birth Year" in df.columns:
        most_recent_birthyear = df['Birth Year'].max()
        print("Youngest Birth year: ",most_recent_birthyear)
        print('-'*40)
    else:
        print("Washington does not have any Youngest birth year data")

    if "Birth Year" in df.columns:
        most_common_birthyear = df['Birth Year'].mode()
        print("Most Common Birth year: ",most_common_birthyear)
        print('-'*40)
    else:
        print("Washington does not have any Common birth year data")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    rawdata = input("Would you like to see the raw data?. Please answer yes or no: ").lower()
    raw = 0
    while rawdata == 'yes' and raw+5<df.shape[0]:
        print (df.iloc[raw:raw+5])
        raw += 5
        rawdata = input("Would you like to see more raw data?. Please answer yes or no: ").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input("\nWould you like to restart? Enter yes or no.\n")
        if restart.lower() != 'yes':
            print("Thank you for playing")
            break


if __name__ == "__main__":
	    main()
