### Date created
This  README file was created on March 20, 2020 by Wendy Rivadeneira

### Project Title
## Bike Share Use Data

### Description
> The Bike Share project calculates statistics about usage patterns for three main cities: New York City, Chicago and Washington DC.
> The data sets are provided by Motivate - a bike share system provider for major cities in the United States.
> The project asks the user for input about the city that the user wants to know.
> Also, it asks the user if they want to filter the data by "month", "day" or "both: month-day" filter option.

The statistics calculations are the following:

	* The most frequent time of travel by month, day or both	
    * The most popular stations and trips
    * The total and average trip duration
	* The number of user/subscribers
	* The breakdown of users by gender and birth year, but only these data items are available for Chicago and New York City.

### Code Summary
> There are seven functions in the bikeshare.py file:
* __main()__ which calls other functions:
	1. __get_filters()__ which ask the user for input about the city, month, day or both (month, day) and returns these inputs
	2. __load_data()__  which passes three arguments( city, month, day) and returns the data frame (df).
	3. __time_stats__  which passes the df as an argument and calculates:
		* The common month
		* the common day 
		* the common start hour
	4. __station_stats()__ whish passes the df as an argument and calculates:
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

	* In the __main()__  function, after all these statistics are displayed, the user is asked to see raw data - 5 rows at a time.
	* The user chooses to continue with the calculations or if prefers to exist the application

### Software installations
These software applications were installed in my local machine to execute the Bike Share application.
* Python version 3.7.7
* Anaconda/Spyder version 3.3.6

### Files used
The CSV files contain usage data and the bikeshare.py contains the code to execute the program.
* chicago.csv
* washington.csv
* new_york_city.csv
* bikeshare.py (contains the code to execute the statistics calculations)

### Credits
> Some of the code to validate user input using the while loop was obtained from examples in Stack Overflow.
> Other code to transform the dataframe was obtained from Python: Practice#3 lesson in Udacity.
> Some help was obtained from mentor on a method to order/sort the values in a data frame.
