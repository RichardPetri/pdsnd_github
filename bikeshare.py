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
    
    #Show available cities to the user (values from global dict)
    print('Available Cities to analyze:')
    for key in CITY_DATA:
        print(' {}'.format(key).title())

    #Get the input for the city, repeat if there is no match
    while True:
        city = str(input('Enter the City to analyze: ')).lower()
        if city not in CITY_DATA:
            print('\nPlease enter one of the available cities from the list above!\n')
            continue
        else:
            break
    print('Analyzing {}...'.format(city).title())
    
    # TO DO: get user input for month (all, january, february, ... , june)
    #create a list for the month filter
    month_list = ['all','january','february','march','april','may','june']

    #Show available month filters to the user (values from list)
    print('Want to filter by month? These options are available:')
    for m in month_list:
        print(' {}'.format(m).title())

    #Get the input for the month, repeat if there is no match
    while True:
        month = str(input('Enter the filter option for the month: ')).lower()
        if month not in month_list:
            print('\nPlease enter one of the available options from the list above!\n')
            continue
        else:
            break
    print('\nFiltering by {}...\n'.format(month).title())

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    #create a list for the day of week filter
    day_list = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']

    #Show available day of week filters to the user (values from list)
    print('Want to filter by the day of the week? These options are available:')
    for d in day_list:
        print(' {}'.format(d).title())

    #Get the input for the day, repeat if there is no match
    while True:
        day = str(input('Enter the filter option for the day: ')).lower()
        if day not in day_list:
            print('\nPlease enter one of the available options from the list above!\n')
            continue
        else:
            break

    #show the choice of filter
    print('\nFiltering by {}...\n'.format(day).title())

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
    # extract month, hour and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['hour'] = df['Start Time'].dt.hour
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
    """Displays statistics on the most frequent times of travel (Month, day of the week and starting hour)."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # translate Month number to Name from the list
    month_list = ['january','february','march','april','may','june']
    popular_month = df['month'].mode()[0]
    print('\nThe most popular month to travel was {}.\n'.format(month_list[popular_month - 1].title()))

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('\nThe most popular day to travel was {}.\n'.format(popular_day))

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('\nThe most popular starting hour to travel was {}:00.\n'.format(popular_hour))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    print('\nThe most popular Start Station was {}.\n'.format(popular_start))

    # TO DO: display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    print('\nThe most popular End Station was {}.\n'.format(popular_end))

    # TO DO: display most frequent combination of start station and end station trip
    df['Route'] = df['Start Station'] + '-' + df['End Station']
    popular_route = df['Route'].mode()[0]
    print('\nThe most popular Route was {}.\n'.format(popular_route))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum()
    print('\nIn total the travel time was {} seconds.\n'.format(total_duration))

    # TO DO: display mean travel time
    mean_duration = df['Trip Duration'].mean()
    print('\nThe mean travel time was {} seconds.\n'.format(mean_duration))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_subscribers = df['User Type'].value_counts()['Subscriber']
    user_customers = df['User Type'].value_counts()['Customer']
    print('\nUser Types:\n\nSubscribers: {}\nCustomers: {}'.format(user_subscribers, user_customers))

    # TO DO: Display counts of gender
    male = df['Gender'].value_counts()['Male']
    female = df['Gender'].value_counts()['Female']
    
    print('\nCount of subscribers by gender:\nMale: {}\nFemale: {}'.format(male, female))

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_birthyear = int(df['Birth Year'].min())
    recent_birthyear = int(df['Birth Year'].max())
    common_birthyear = int(df['Birth Year'].mode()[0])
    
    print('\nEarliest year of birth: {}\nMost recent year of birth: {}\nMost common year of birth: {}'.format(earliest_birthyear, recent_birthyear, common_birthyear))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    '''Asks the user if they want to see the raw data and shows it in increments of 5 rows'''
    #create a row counter starting from 0
    count = 0
    #ask for user input
    raw_data_start = input('\nWould you like to see the raw data? yes/no: ').lower()
    #loop to either show the first 5 rows or not
    while True:    
        if raw_data_start == 'yes':
            print(df.head())
            count += 5
            break
        elif raw_data_start == 'no':
            break
        #handle anything that's not yes or no
        else:
            raw_data_start = input('\nPlease type "yes" or "no"!').lower()
    #if user wants raw data: loop to either show 5 more and ask again or not        
    while raw_data_start == 'yes':
        raw_data_cont = input('\n5 more? yes/no:').lower()
        if raw_data_cont == 'yes':
            print(df[count:count + 5])
            count += 5
            continue
        elif raw_data_cont == 'no':
            break
        #handle anything that's not yes or no
        else:
            print('\nPlease type "yes" or "no"!')
            continue
            
            

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
