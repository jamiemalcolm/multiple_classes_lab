class Person:
    def __init__(self, name, age, destination):
        self.name = name
        self.age = age
        self.destination = destination

    def pick_right_bus(self, bus, bus_stop):
        # make sure destination matches passenger
        # update the queue
        # update the buss passenger count
        for passenger in bus_stop.queue:
            if bus.destination == passenger.destination:
                bus_stop.queue.remove(passenger)
                bus.passengers.append(passenger)
