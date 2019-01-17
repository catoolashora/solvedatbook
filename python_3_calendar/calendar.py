from _datetime import datetime

class event:
    def __init__(self, name, place, day, month, year, hour = 0, minute = 0, second = 0, microsecond = 0):
        self.name = name
        self.place = place
        self.datetime = datetime(year, month, day, hour, minute, second, microsecond)
     
    def print(self):
        print("name: ", self.name)
        print("place: ", self.place)
        print("date and time: ", self.datetime.ctime())

def add_event(name, place, day, month, year, hour = 0, minute = 0, second = 0, microsecond = 0):
    calendar.append(event(name, place, day, month, year, hour, minute, second, microsecond))

def cleanup():
    global calendar
    calendar = filter(lambda event: event.datetime > datetime.now(), calendar)

def print_events():
    cleanup()
    for event in calendar:
        event.print()



global calendar
calendar = []
add_event("doing good", "all ma wrld", 16, 1, 2019)
add_event("doing good", "all da wrld", 18, 1, 2019)
print_events()