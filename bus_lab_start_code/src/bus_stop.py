class BusStop:
    def __init__(self, name):
        self.name = name
        self.queue = []

    def add_to_queue(self, person_1):
        self.queue.append(person_1)
