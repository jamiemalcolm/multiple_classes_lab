import unittest
from src.person import Person
from src.bus import *
from src.bus_stop import *


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person = Person("Guido van Rossum", 64, "blablabla")

    @unittest.skip("Delete this line to run the test")
    def test_person_has_name(self):
        self.assertEqual("Guido van Rossum", self.person.name)

    @unittest.skip("Delete this line to run the test")
    def test_person_has_age(self):
        self.assertEqual(64, self.person.age)

    def test_is_the_right_bus__true(self):
        person_1 = Person("Jock", 25, "Ocean Terminal")
        person_2 = Person("Ann", 45, "Leith Links")
        bus = Bus(22, "Ocean Terminal")
        bus_stop = BusStop("Albert str")
        bus_stop.add_to_queue(person_1)
        bus_stop.add_to_queue(person_2)
        self.person.pick_right_bus(bus, bus_stop)
        self.assertEqual(1, bus.passenger_count())
