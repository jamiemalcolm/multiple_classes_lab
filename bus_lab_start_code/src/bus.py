class Bus:
    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passengers = []

    def drive(self):
        return "Brum brum"

    def passenger_count(self):
        return len(self.passengers)

    def pick_up(self, person_1):
        self.passengers.append(person_1)

    def drop_off(self, person_1):
        self.passengers.remove(person_1)

    def empty(self):
        self.passengers.clear()
        #  or self.passengers = []

    def pick_up_from_stop(self, bus_stop):
        # take all people from the queue and ad them to the bus passenger count
        for passenger in bus_stop.queue:
            self.passengers.append(passenger)
