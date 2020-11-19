from datetime import date,datetime,timedelta
import time


lamp = False
buttonReset = True

startTime = datetime.now()

def TimerAdvanceDays(numDays):
    """
    Returns midnight of numDays ahead of current time.
    """
    return datetime.combine(date.today() + timedelta(days=numDays), datetime.min.time())


def CheckExternalInput():
    """
    Check if any buttons have been pressed.
    """
    if buttonReset:
        lamp = False
        countdown = TimerAdvanceDays(7)

# Midnight of 7 days ahead
countdown = TimerAdvanceDays(7)



for counter in range(5):
    timeNow = datetime.now()
    timeLeftTimerOne = countdown - timeNow
    print(timeLeftTimerOne)
    if countdown <= timeNow:
        lamp = True
        print(lamp)
        continue

    CheckExternalInput()

    time.sleep(3)

