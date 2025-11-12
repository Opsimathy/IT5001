
from pprint import pprint


print("Part 3")
NODinAMonth = (31,28,31,30,31,30,31,31,30,31,30,31)

def doy(month,day):
    return 0

print(doy(12,30))

travelDates = (('Amy',2,14), ('Bill',2,24),('Cid',1,2),('David',2,27),
               ('Ed',1,31),('Frank',3,28),('Gary',3,11),('Ian',1,31))

def listLOA(rd,month,day):
    return []


def firstBestMeetingDate(rd,month):
    n = 0
    date = 0
    return (date,n)
    
print(listLOA(travelDates,2,26))
print(listLOA(travelDates,2,27))    
print(listLOA(travelDates,2,28))
print(listLOA(travelDates,3,1))

print(firstBestMeetingDate(travelDates,1))
print(firstBestMeetingDate(travelDates,2))
print(firstBestMeetingDate(travelDates,3))
