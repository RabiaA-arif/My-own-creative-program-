#time.strftime(): This function is used to format the time tuple into a string representation according to the specified format. In this case, %H:%M is the format string, where %H represents the hour (24-hour format) and %M represents the minute#




import time

def morning_prayer_reminder():
    while True:
        current_time = time.strftime("%H:%M", time.localtime())
        if current_time == "05:30":
            print("It's time for your morning prayer.")
            break
            
#time: Refers to the time module we imported earlier.

#sleep(): This function pauses the execution of the program for the specified number of seconds. In this case, 60 is passed as the argument, which means the program will sleep for 60 seconds.            
            
        else:
            time.sleep(60) 
             # Check the time every minute

morning_prayer_reminder()
