var P1 = function (repeats) {
    for (var i = 0; i < repeats; i++){
        console.log(i + ". =^.^=")
    }
}

var P2 = function (){
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
    var currentYear = 2026.5
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

var OP1 = function (){
    console.log("Hello world")
}

var P3 = function (){
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

console.log("HubBase-onJS 0.0.1.0.01 (default, May 18 2026, 18:50:26)")
P1(10)
P2()
P3()
console.log("Original programms:")
OP1()