import time
import pandas as pd
import numpy as np

CITY_DATA = {'Chicago': 'chicago.csv',
             'New York': 'new_york_city.csv',
             'Washington': 'washington.csv'}

citys = ['Chicago', 'New York', 'Washington']

months = ['January', 'February', 'March', 'April', 'May', 'June']

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']




def inputs():
    city = '-1'
    month = '-1'
    day = '-1'
    
    while True:
        city = input("Would you like to see data for Chicago, New York, or Washington?")
        city = city.lower().strip().title();
        if city not in citys:
            print("Wrong Input")
            continue

        ans = input("Would you like to filter the data by month, day,both or none?")
        ans = ans.lower().strip()

        if ans == "month":
            month = input("Which month - January, February, March, April, May, or June?");
            month = month.lower().strip().title()
            if month not in months:
                print("Wrong Input")
                continue

        elif ans == "day":
            day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?")
            day = day.lower().strip().title()
            if day not in days:
                print("Wrong Input")
                continue

        elif ans == "both":
            month = input("Which month - January, February, March, April, May, or June?");
            month = month.lower().strip().title()
            if month not in months:
                print("Wrong Input")
                continue

            day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?")
            day = day.lower().strip().title()
            if day not in days:
                print("Wrong Input")
                continue
        return city,month,day
        

def load_data(city, month, day):
    
    df = pd.read_csv(CITY_DATA[city])

    df["Start Time"] = pd.to_datetime(df["Start Time"])
                      

    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != '-1':
        Month = months.index(month) + 1
        df = df[df['month'] == Month]
    if day != '-1':
        df = df[df['day'] == day]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    print("the most common month : ", months[df['month'].mode()[0]-1])
    print("most common day of week : ", df['day'].mode()[0])
    print("the most common start hour : ", df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print("most commonly used start station : ", df['Start Station'].mode()[0])

    print("most commonly used end station : ", df['End Station'].mode()[0])

    df["start_to_end"] = df['Start Station'] + df['End Station']
    combination = df["start_to_end"].value_counts().head(1)
    #combination = df.groupby(['Start Station', 'End Station']).apply(sort_values(ascending=False))
    #combination = combination.sort_values().head(1)
    print("most frequent combination of start station and end station trip : ", combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    print("total travel time : ", df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print("mean travel time : ", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("counts of user types : ", df['User Type'].value_counts())

    if city != "Washington":
        # TO DO: Display counts of gender
        print("counts of user types : ", df['Gender'].value_counts())

        # TO DO: Display earliest, most recent, and most common year of birth
        df['Birth Year'] = pd.to_datetime(df['Start Time'])
        print("earliest year of birth : ", df['Birth Year'].min())
        print("most recent birth : ", df['Birth Year'].max())
        print("most common birth : ", df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)
def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while (view_data=="yes"):
      print(df.iloc[ start_loc : start_loc+5])
      start_loc += 5
      view_data = input("Do you wish to continue?: ").lower()
def main():
    while True:
        c,m,d = inputs()
        df = load_data(c,m,d)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,c)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()

