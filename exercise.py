# Create a Location class with a name.

# Create a Trip class with a list of Location instances (called stops or destinations or something similar). Define a method that lets you add locations to the trip's list of destinations.

# Make several instances of Locations and add them to an instance of Trip.

# Define a method in the Trip class that iterates through the list of locations and prints something similar to the following:

# "Began trip."
# "Travelled from Toronto to Ottawa."
# "Travelled from Ottawa to Montreal."
# "Travelled from Montreal to Quebec City."
# "Travelled from Quebec City to Halifax."
# "Travelled from Halifax to St. John's."
# "Ended trip."

class Location:

    def __init__(self, cities):
        self.cities = cities
    


class Trip:
    def __init__(self):
        self.destinations = []
    
    def add_cities(self, cities):
        self.destinations.append(cities)
        
    def trip_list(self):
        i = 0
        print("Began trip.")
        for i in range(len(self.destinations) - 1):
            print("Travelled from {} to {}.".format(self.destinations[i], self.destinations[i + 1]))
        i =+ 1
        print("Ended trip.")



toronto = Location("Toronto")
ottawa = Location("Ottawa")
montreal = Location("Montreal")
quebec = Location("Quebec City")
halifax = Location("Halifax")
stjohns = Location("St. John's")
trip1 = Trip()
trip1.add_cities(toronto)
trip1.add_cities(ottawa)
trip1.add_cities(montreal)
trip1.add_cities(quebec)
trip1.add_cities(halifax)
trip1.add_cities(stjohns)
trip1.trip_list()





