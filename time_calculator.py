def add_time(start_time, duration, weekday = None):
    #Assume that the start times are valid times
    weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    start_hour = int(start_time.split(" ")[0].split(":")[0])
    start_minute = int(start_time.split(" ")[0].split(":")[1])
    am_pm = str(start_time.split(" ")[1]).lower()
    # convert 12-hour clock format into 24-hour clock
    if am_pm == "pm":
        start_hour += 12 
    duration_hour = int(duration.split(":")[0])
    duration_minute = int(duration.split(":")[1])
    if duration_minute < 0 or duration_minute > 60:
        return "Error: duration time not valid"

    total_minutes = start_minute + duration_minute
    total_hours = start_hour + duration_hour + int(total_minutes / 60)
    final_hour = total_hours % 24
    final_minutes = int(total_minutes % 60)
    if final_minutes < 10:
        final_minutes = f"0{final_minutes}"

    days_passed = int(total_hours / 24)

    am_or_pm = ""
    if final_hour >= 12:
        am_or_pm = "PM"
        final_hour -= 12
    else:
        am_or_pm = "AM"
    
    if final_hour == 0:
        final_hour = 12

    new_time = f"{final_hour}:{final_minutes} {am_or_pm}"

    if weekday is not None:
        index = weekdays.index(weekday.lower())
        if weekday.lower() not in weekdays:
            return "Error: weekday not valid"
        else: 
            final_weekday = weekdays[((days_passed + index) % 7)]
            new_time += f", {final_weekday.capitalize()}"
    if days_passed == 1:
        new_time += " (next day)"
    elif days_passed > 1:
        new_time += f" ({days_passed} days later)"
   
    return new_time