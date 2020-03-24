
## Bike Share Use Data

### Description
The Bike Share project calculates statistics about usage patterns for three main cities: New York City, Chicago and Washington DC.
The data sets are provided by Motivate - a bike share system provider for major cities in the United States.
When the application is ran/executed, it asks the user for input about the city he/she wants to know more.
Once provided the city, it asks the user if he/she wants to filter the data by "month", "day" or "both: month-day" filter options.

Then the following statistics are calculated:

* The most frequent time of travel by month, day or both.

* The most popular stations and trips.

* The total and average trip duration.

* The number of user/subscribers.

* The breakdown of users by gender and birth year, but only these data items are available for Chicago and New York City.

After the statistics are displayed, the user is asked the following questions:
* Would you like to see raw - 5 rows at time, yes or no? If the users answers yes, then it displays the first 5 rows. Then the same question is asked for the next 5 rows until the user enters "no".
* Would you like to restart the application yes or no?.

### Code Summary
There are seven functions in the bikeshare.py file:

__main()__ which calls these other functions:

	1. __get_filters()__ which ask the user for input about the city, month, day or both (month, day) and returns these inputs.

	2. __load_data()__  which passes three arguments( city, month, day)
		and returns the data frame (df).

	3. __time_stats__  which passes the df as an argument and displays:
			* The common month
			* the common day
			* the common start hour

	4. __station_stats()__ whish passes the df as an argument
		and calculates:
			* The most commonly used start station
			* The most commonly used end station
			* The most frequent combination of start station and end station trip

	5. __trip_duration_stats()__ which passes the df as an argument and calculates:
			* The total time traveled
			* The average time traveled

	6. __user_stats()__ which passes the df as an argument and calculates:
			* The breakdown of users(customers/subscribers)
			* The breakdown of users by gender
			* The oldest, youngest and most popular year of birth

In the __main()__  function, after all these statistics are displayed, the user is asked to see raw data - 5 rows at a time. The user is asked to continue seeing row data or not and then is asked to restart the application or exit it.

### installation of application
`$ python bikeshare.py`

### Software installations
Install this software applications in your local machine to run the bikeshare.py application:

* Anaconda/Python 3.7 version. [Click here](https://www.anaconda.com/distribution/#windows).

### Files used
The CSV files contain usage data and the bikeshare.py contains the python code to execute the program.
* chicago.csv
* washington.csv
* new_york_city.csv
* bikeshare.py (contains the code to execute the statistics calculations)

### Credits
Some of the code to validate user input using the while loop was obtained from examples in Stack Overflow.
Other code to transform the dataframe was obtained from Python: Practice#3 lesson in Udacity.
Some help was obtained from mentor on a method to order/sort the values in a data frame.  :octocat:
