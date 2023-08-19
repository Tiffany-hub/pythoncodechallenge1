def convert_to_24_hour (time_str):
    parts = time_str.split()
    time_parts = parts[0].split(':')
    hour = int(time_parts[0])
    minute = int(time_parts[1])
    period = parts[1]

    if period == "pm" and hour != 12:
        hour += 12
    elif period == "am" and hour == 12:
        hour = 0

    time_24_hour = f"{hour:02d}{minute:02d}"
    return time_24_hour

time_str = "8:30 am"
time_24_hour = convert_to_24_hour(time_str)
print(time_24_hour)
