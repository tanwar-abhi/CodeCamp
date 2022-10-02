

    

def add_time(startTime, duration, startingDay = ""):
    
    weekDays = ("MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY")
    startTime.upper()
    startingDay = startingDay.upper()

    if (startingDay != ""):
        dayCounter = weekDays.index(startingDay)

    sTime, timePeriod = startTime.split()

    # Starting time in hours and starting time in minutes
    stHours, stMinutes = sTime.split(":")

    # Duration in hours and minutes
    dHours, dMinutes = duration.split(":")

    totalHours = int(stHours) + int(dHours)
    if (int(dHours) > 12):
        dHours = dHours//12
    
    
        
        
    totalHours = int(stHours) + int(dHours)
    totalMinutes = int(stMinutes) + int(dMinutes)

    if (totalMinutes > 59):
        totalMinutes -= 60
        totalHours += 1


    if (totalHours > 12):
        if (timePeriod == "AM"):
            timePeriod == "PM"
        else:
            timePeriod = "PM"

    elif (totalHours > 12 and startingDay != ""):
        
        
    elif (timePeriod == "PM" and totalHours > 12):
        dayCounter += 1
        totalHours -= 12
        if (startingDay == ""):
            nextDay = True
        
        
        
            

    result = str(totalHours) + ":" + str(totalMinutes) + " " + timePeriod

    if (nextDay):
        result += " (next day)"
    else:
        result += 
        

        
        
        
    
    
    
    
    


if __name__ == "__main__":
    add_time("3:00 PM", "3:10")    