import unittest
from DOMAIN.person import person_class

class test_person(unittest.TestCase):
    def setUp(self) -> None:
        self.person_1 = person_class("1", "Popescu Niculae", "ROmania", "Tulcea", "Zorilor", "122")
        self.person_2 = person_class("2", "Pescar Miruna", "Zimbabue", "NEW MAN", "LUMINII", "122A")

    def tearDown(self) -> None:
        self.person_1 = None
        self.person_2 = None

    def test_getters(self):
        self.assertEqual(self.person_1.get_person_id(), "1")
        self.assertEqual(self.person_1.get_person_name(), "Popescu Niculae")
        self.assertEqual(self.person_1.get_country(), "ROmania")
        self.assertEqual(self.person_1.get_city(), "Tulcea")
        self.assertEqual(self.person_1.get_street(), "Zorilor")
        self.assertEqual(self.person_1.get_number_of_the_house(), "122")
        self.assertEqual(self.person_1.get_events_id(), [])
        self.assertEqual(self.person_1.number_of_events_added(),  0)

    def test_setters(self):
        self.person_1.set_person_name("Popescu Marius")
        self.person_1.set_country("Germania")
        self.person_1.set_city("Berlin")
        self.person_1.set_street("Oderbergerstrasse")
        self.person_1.set_number_of_the_house("44")
        self.assertEqual(self.person_1.get_person_name(), "Popescu Marius")
        self.assertEqual(self.person_1.get_country(), "Germania")
        self.assertEqual(self.person_1.get_city(), "Berlin")
        self.assertEqual(self.person_1.get_street(), "Oderbergerstrasse")
        self.assertEqual(self.person_1.get_number_of_the_house(), "44")

    def test_add_event_to_person(self):
        self.person_1.add_event_to_person("1")
        self.person_1.add_event_to_person("2")
        self.person_1.add_event_to_person("3")
        self.assertEqual(self.person_1.number_of_events_added(),  3)
        self.assertEqual(self.person_1.get_events_id(), ["1", "2", "3"])
    
    def test_str(self):
        self.assertEqual(str(self.person_1), "ID:        1\nName:      Popescu Niculae\nTara:      ROmania\nOras:      Tulcea\nStrada:    Zorilor\nNumar:     122\nID - urile ev. la care participa: []")
        self.assertEqual(str(self.person_2), "ID:        2\nName:      Pescar Miruna\nTara:      Zimbabue\nOras:      NEW MAN\nStrada:    LUMINII\nNumar:     122A\nID - urile ev. la care participa: []")

        
