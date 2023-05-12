def add_time(start, duration, day=None):
    
    # Set up variables
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    start_time, meridian = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Convert to 24-hour format
    if meridian == 'PM':
        start_hour += 12

    # Add duration
    end_minute = (start_minute + duration_minute) % 60
    end_hour = (start_hour + duration_hour + (start_minute + duration_minute) // 60) % 24
    days_later = (start_hour + duration_hour + (start_minute + duration_minute) // 60) // 24

    # Convert back to 12-hour format
    if end_hour >= 12:
        end_meridian = 'PM'
        if end_hour > 12:
            end_hour -= 12
    else:

        end_meridian = 'AM'
        if end_hour == 0:
            end_hour = 12

    # Determine day of week
    if day:
        day = day.title()
        day_index = days_of_week.index(day)
        end_day_index = (day_index + days_later) % 7
        end_day = days_of_week[end_day_index]
        if days_later == 1:
            end_day = end_day + ' (next day)'
        elif days_later > 1:
            end_day = end_day + f' ({days_later} days later)'

    # Format output string
    if day:
        return f'{end_hour}:{end_minute:02} {end_meridian}, {end_day}'
    else:
        if days_later == 1:
            return f'{end_hour}:{end_minute:02} {end_meridian} (next day)'
        elif days_later > 1:
            return f'{end_hour}:{end_minute:02} {end_meridian} ({days_later} days later)'
        else:
            return f'{end_hour}:{end_minute:02} {end_meridian}'

print(add_time("3:00 PM", "3:10"))
# Returns: 6:10 PM

print(add_time("11:30 AM", "2:32", "Monday"))
# Returns: 2:02 PM, Monday

print(add_time("11:43 AM", "00:20"))
# Returns: 12:03 PM

print(add_time("10:10 PM", "3:30"))
# Returns: 1:40 AM (next day)

print(add_time("11:43 PM", "24:20", "tueSday"))
# Returns: 12:03 AM, Thursday (2 days later)

print(add_time("6:30 PM", "205:12"))
# Returns: 7:42 AM (9 days later)
