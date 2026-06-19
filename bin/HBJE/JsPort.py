def P1(repeats):
    i = 0
    for i in range(1, repeats):
        print(str(i) + ". =^.^=")


def P2():
    SecInMin = 60
    MinInHour = 60
    SecInHour = SecInMin * MinInHour
    HourInDay = 24
    SecInDay = SecInHour * HourInDay
    MinInDay = MinInHour * HourInDay
    DayInWeek = 7
    SecInWeek = SecInDay * DayInWeek
    MinInWeek = MinInDay * DayInWeek
    HourInWeek = HourInDay * DayInWeek
    DayInYear = 365
    SecInYear = SecInDay * DayInYear
    MinInYear = MinInDay * DayInYear
    HourInYear = HourInDay * DayInYear
    currentYear = 2026.5
    print("There are " + str(SecInMin) + " seconds in a minute")
    print("There are " + str(MinInHour) + " minutes in an hour")
    print("There are " + str(SecInHour) + " seconds in an hour")
    print("There are " + str(HourInDay) + " hours in a day")
    print("There are " + str(SecInDay) + " seconds in a day")
    print("There are " + str(MinInDay) + " minutes in a day")
    print("There are " + str(DayInWeek) + " days in a week")
    print("There are " + str(SecInWeek) + " seconds in a week")
    print("There are " + str(MinInWeek) + " minutes in a week")
    print("There are " + str(HourInWeek) + " hours in a week")
    print("There are " + str(DayInYear) + " days in a year")
    print("There are " + str(SecInYear) + " seconds in a year")
    print("There are " + str(MinInYear) + " minutes in a year")
    print("There are " + str(HourInYear) + " hours in a year")
    print("I am aproximately " + str(((currentYear - 2014.8) * SecInYear)) + " seconds old")


def OP1():
    print("Hello world")


def P3():
    HighFives = 0
    print(HighFives + 1)
    print(HighFives + 2)
    print(HighFives + 1)
    print("Delayed:")
    print(HighFives)
    print(HighFives + 1)
    print(HighFives + 2)
    print(HighFives + 1)
