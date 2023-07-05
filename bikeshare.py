import datetime
import time

import numpy as np
import pandas as pd

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Choose a city. (type Chicago/C, New York City/N, Washington/W):").upper()
        if city == "CHICAGO" or city == "C":
            city = "chicago"
            break
        elif city == "NEW YORK CITY" or city == "N":
            city = "new york city"
            break
        elif city == "WASHINGTON" or city == "W":
            city = "washington"
            break
        else:
            print("Please choose a valid city!")
    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Choose a month. (type January/Jan, February/Feb, March/Mar, April/Apr, May, "
                      "June or all/a for no filter):").upper()
        if month == "JANUARY" or month == "JAN":
            month = "January"
            break
        elif month == "FEBRUARY" or month == "FEB":
            month = "February"
            break
        elif month == "MARCH" or month == "MAR":
            month = "March"
            break
        elif month == "APRIL" or month == "APR":
            month = "April"
            break
        elif month == "MAY":
            month = "May"
            break
        elif month == "JUNE":
            month = "June"
            break
        elif month == "ALL" or month == "A":
            month = "all"
            break
        else:
            print("Please choose a valid month!")
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Choose a day. (type Monday/Mo, Tuesday/Tu, Wednesday/We, Thursday/Th, "
                    "Friday/Fr, Saturday/Sa, Sunday/Su or all/a for no filter):").upper()
        if day == "MONDAY" or day == "MO":
            day = "Monday"
            break
        elif day == "TUESDAY" or day == "TU":
            day = "Tuesday"
            break
        elif day == "WEDNESDAY" or day == "WE":
            day = "Wednesday"
            break
        elif day == "THURSDAY" or day == "TH":
            day = "Thursday"
            break
        elif day == "FRIDAY" or day == "FR":
            day = "Friday"
            break
        elif day == "SATURDAY " or day == "SA":
            day = "Saturday"
            break
        elif day == "SUNDAY" or day == "SU":
            day = "Sunday"
            break
        elif day == "ALL" or day == "A":
            day = "all"
            break
        else:
            print("Please choose a valid day!")
    print("Selected city: {}".format(city.title()))
    print("Selected month: {}".format(month))
    print("Selected day: {}".format(day))
    print('-' * 40)
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
    df['day'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    df['month'] = df['Start Time'].dt.month_name()
    # find the most common month
    month = df['month'].mode()[0]
    print('Most common start month:', month)

    # display the most common day of week
    # extract day of week from the Start Time column to create a day column
    df['day'] = df['Start Time'].dt.day_name()
    # find the most common day
    day = df['day'].mode()[0]
    print('Most common start day:', day)

    # display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # find the most common hour (from 0 to 23)
    hour = df['hour'].mode()[0]
    print('Most common start hour:', hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df["Start Station"].mode()[0]
    print('Most common start station:', start_station)

    # display most commonly used end station
    end_station = df["End Station"].mode()[0]
    print('Most common end station:', end_station)

    # display most frequent combination of start station and end station trip
    start_end_station = (df["Start Station"] + ' --- ' + df["End Station"]).mode()[0]
    print('Most frequent combination of start station and end station:', start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = df["Trip Duration"].sum()
    print('Total travel time:', str(datetime.timedelta(seconds=float(total_travel))))
    # display average travel time
    mean_travel = df["Trip Duration"].mean()
    print('Average travel time:', str(datetime.timedelta(seconds=float(mean_travel))))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print(gender)
    else:
        print('Gender data is not available in dataset.')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth = df['Birth Year'].min()
        print('Earliest year of birth:', int(earliest_birth))
        most_recent_birth = df['Birth Year'].max()
        print('Most recent year of birth:', int(most_recent_birth))
        common_birth = df['Birth Year'].mode()[0]
        print('Most common year of birth:', int(common_birth))
    else:
        print('Birth Year data is not available in dataset.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def print_raw_data(df):
    """Printing raw data"""
    answer = input("Do you want to see 5 lines of raw data? Enter yes or no.")
    if answer.lower() != 'yes':
        return
    for idx, row in enumerate(df.itertuples(index=False)):
        # print("--- START row {} data ---".format(idx))
        # print(df.iloc[idx])
        # print("--- END of row {} data ---".format(idx))
        print(row)
        if ((idx + 1) % 5) == 0:
            answer = input("Do you want to see the next 5 lines of raw data, starting from row {}? "
                           "Enter yes or no.".format(idx + 1))
            if answer.lower() != 'yes':
                break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        print_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()