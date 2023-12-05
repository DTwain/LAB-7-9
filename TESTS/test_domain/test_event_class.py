import unittest
from DOMAIN.event import event_class

class test_event(unittest.TestCase):
    def setUp(self) -> None:
        self.event_1 = event_class("1", "12/2/2020", "120", "Kylie Jenner s-a despartit de Travis Scott")
        self.event_2 = event_class("2", "28/2/2022", "200", "Serbarea clasei a 3 - a")
    
    def tearDown(self) -> None:
        self.event_1 = None
        self.event_2 = None
    
    def test_getters(self):
        self.assertEqual(self.event_1.get_event_id(), "1")
        self.assertEqual(self.event_1.get_event_date(), "12/2/2020")
        self.assertEqual(self.event_1.get_event_duration(), "120")
        self.assertEqual(self.event_1.get_event_description(), "Kylie Jenner s-a despartit de Travis Scott")
        self.assertEqual(self.event_1.get_number_of_people_joined(), 0)
        self.event_1.inc_number_of_participants()
        self.assertEqual(self.event_1.get_number_of_people_joined(), 1)

    def test_setters(self):
        self.event_1.set_event_date("12/2/2021")
        self.event_1.set_event_duration("300")
        self.event_1.set_event_description("Balul Bobocilor")
        self.assertEqual(self.event_1.get_event_date(), "12/2/2021")
        self.assertEqual(self.event_1.get_event_duration(), "300")
        self.assertEqual(self.event_1.get_event_description(), "Balul Bobocilor")

    def test_str(self):
        self.assertEqual(str(self.event_1), "ID:          1\nData:        12/2/2020\nDurata:      120 minute\nDescriere:   Kylie Jenner s-a despartit de Travis Scott\nNr. persoane inscrise:    0")
        self.assertEqual(str(self.event_2), "ID:          2\nData:        28/2/2022\nDurata:      200 minute\nDescriere:   Serbarea clasei a 3 - a\nNr. persoane inscrise:    0")