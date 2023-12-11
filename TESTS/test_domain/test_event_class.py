import unittest
from DOMAIN.event import event_class
from DOMAIN.person_event import person_event_class

class test_event_class(unittest.TestCase):
    def setUp(self):
        self.shared_person_event_class = person_event_class()
        self.event = event_class("1", "12/2/2020", "120", "Concertul lui travis Scott", self.shared_person_event_class)

    def tearDown(self):
        self.shared_person_event_class = None
        self.event = None

    def test_get_event_id(self):
        self.assertEqual(self.event.get_event_id(), "1")

    def test_get_event_date(self):
        self.assertEqual(self.event.get_event_date(), "12/2/2020")

    def test_get_event_duration(self):
        self.assertEqual(self.event.get_event_duration(), "120")

    def test_get_event_description(self):
        self.assertEqual(self.event.get_event_description(), "Concertul lui travis Scott")

    def test_set_event_date(self):
        self.event.set_event_date("14/1/2021")
        self.assertEqual(self.event.get_event_date(), "14/1/2021")

    def test_set_event_duration(self):
        self.event.set_event_duration("100")
        self.assertEqual(self.event.get_event_duration(), "100")

    def test_set_event_description(self):
        self.event.set_event_description("Balul Bobocilor, clasa a 9 - a RA")
        self.assertEqual(self.event.get_event_description(), "Balul Bobocilor, clasa a 9 - a RA")

    def test_add_person_to_event(self):
        self.event.add_person_to_event("1")
        self.assertEqual(self.event.get_number_of_people_joined_to_event(), 1)

    def test_remove_any_connections_with_event_id(self):
        self.event.add_person_to_event("1")
        self.event.remove_any_connections_with_event_id()
        self.assertEqual(self.event.get_number_of_people_joined_to_event(), 0)

    def test_get_number_of_people_joined_to_event(self):
        self.event.add_person_to_event("1")
        self.event.add_person_to_event("2")
        self.assertEqual(self.event.get_number_of_people_joined_to_event(), 2)

    def test_eq(self):
        event1 = event_class("1", "12/2/2020", "120", "Concertul lui travis Scott", self.shared_person_event_class)
        event2 = event_class("1", "12/2/2020", "120", "Concertul lui travis Scott", self.shared_person_event_class)
        event3 = event_class("2", "14/1/2021", "100", "Balul Bobocilor, clasa a 9 - a RA", self.shared_person_event_class)
        self.assertEqual(event1, event2)
        self.assertNotEqual(event1, event3)

    def test_str(self):
        expected_output = "ID:           1\nData:         12/2/2020\nDurata:       120 minute\nDescriere:    Concertul lui travis Scott\nNr. persoane: 0"
        self.assertEqual(str(self.event), expected_output)
