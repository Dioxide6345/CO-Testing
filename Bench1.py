import datetime

def dayOfTheWeek(day, month, year):
    date = datetime.date(year, month, day)
    weekday = date.weekday()
    day_dict = { 0 : "Monday", 1 : "Tuesday", 2 : "Wednesday", 3 : "Thursday", 4 : "Friday", 5 : "Sturday", 6 : "Sunday"}

    return day_dict[weekday]
    
year = int(input("Year: "))     
month = int(input("Month: "))       
day = int(input("Day: "))

dayOfTheWeek(day, month, year)
