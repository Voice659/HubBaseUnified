console.log("This is a dump for random code!")
console.log("Some early previews will be here!")

var PD1 = function (){
    console.log(99 * 123)
    console.log("Long string!".slice(0,4))
    console.log(true && false)
    console.log(12345 + 56789)
    console.log(22 + 33 + 44)
    console.log(1000 - 17)
    console.log(123 * 456)
    console.log(12345 / 250)
    console.log(1234 + 57 * 3 - 31 / 4)
    console.log(8 / 1 + 3)
    console.log("Fix:")
    console.log(8 / (1+3))
    console.log(15 + 9 * 2)
    console.log("Fix:")
    console.log((15+9) * 2)
    var nick;
    var age = 12;
    console.log(age)
    console.log(age = 13)
}

var SP1 = function (){
    var SecInMin = 60
    var MinInHour = 60
    var SecInHour = SecInMin * MinInHour
    var HourInDay = 24
    var SecInDay = SecInHour * HourInDay
    var MinInDay = MinInHour * HourInDay
    var DayInWeek = 7
    var SecInWeek = SecInDay * DayInWeek
    var MinInWeek = MinInDay * DayInWeek
    var HourInWeek = HourInDay * DayInWeek
    var DayInYear = 365
    var SecInYear = SecInDay * DayInYear
    var MinInYear = MinInDay * DayInYear
    var HourInYear = HourInDay * DayInYear
    var currentYear = 2026
    console.log("There are "+SecInMin+" seconds in a minute")
    console.log("There are "+MinInHour+" minutes in an hour")
    console.log("There are "+SecInHour+" seconds in an hour")
    console.log("There are "+HourInDay+" hours in a day")
    console.log("There are "+SecInDay+" seconds in a day")
    console.log("There are "+MinInDay+" minutes in a day")
    console.log("There are "+DayInWeek+" days in a week")
    console.log("There are "+SecInWeek+" seconds in a week")
    console.log("There are "+MinInWeek+" minutes in a week")
    console.log("There are "+HourInWeek+" hours in a week")
    console.log("There are "+DayInYear+" days in a year")
    console.log("There are "+SecInYear+" seconds in a year")
    console.log("There are "+MinInYear+" minutes in a year")
    console.log("There are "+HourInYear+" hours in a year")
    console.log("I am aproximately "+((currentYear-2014)*SecInYear)+" seconds old")
}

var SP2 = function (){
    var HighFives = 0
    console.log(++HighFives)
    console.log(++HighFives)
    console.log(--HighFives)
    console.log("Delayed:")
    console.log(HighFives++)
    console.log(HighFives++)
    console.log(HighFives--)
    console.log(HighFives)
}

var PD2 = function (){
    var x = 10
    console.log(x + 5)
    console.log("Better solution:")
    var x = 10
    console.log(x += 5)
}

PD1()
SP1()
SP2()
PD2()