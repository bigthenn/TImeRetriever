import datetime

# Prompt the user for the date and time to calculate the elapsed time from
day = input("Enter the day: ")
month = input("Enter the month: ")
year = input("Enter the year: ")
hour = input("Enter the hour: ")
minute = input("Enter the minute: ")
second = input("Enter the second: ")

# Parse the date and time string into a datetime object
date = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute), int(second))

# Get the current time
now = datetime.datetime.now()

# Calculate the elapsed time
elapsed = now - date

# Prompt the user for the unit of time to display the elapsed time in
unit = input("Enter the unit of time to display the elapsed time in (seconds, minutes, hours, days, weeks, months, years): ")

# Print the elapsed time in the specified unit
if unit == "seconds":
    print(f"{elapsed.total_seconds()} seconds")
elif unit == "minutes":
    print(f"{elapsed.total_seconds() / 60} minutes")
elif unit == "hours":
    print(f"{elapsed.total_seconds() / 3600} hours")
elif unit == "days":
    print(f"{elapsed.total_seconds() / 86400} days")
elif unit == "weeks":
    print(f"{elapsed.total_seconds() / 604800} weeks")
elif unit == "months":
    print(f"{elapsed.total_seconds() / 2629746} months")
elif unit == "years":
    print(f"{elapsed.total_seconds() / 31556952} years")
else:
    print("Invalid unit of time")
