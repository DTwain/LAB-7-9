import unittest
from DOMAIN.person import person_class
from DOMAIN.person_event import person_event_class
from DOMAIN.person import person_class
from DOMAIN.person_event import person_event_class
from UTILS.generators import id_generator, string_generator
class test_person_class(unittest.TestCase):
    def setUp(self):
        self.__shared_person_event_class = person_event_class()
        self.__person = person_class("1", "John Doe", "USA", "New York", "Broadway", "123", self.__shared_person_event_class)

    def tearDown(self):
        self.__shared_person_event_class = None
        self.__person = None

    def test_get_person_id(self):
        self.assertEqual(self.__person.get_person_id(), "1")

    def test_get_person_name(self):
        self.assertEqual(self.__person.get_person_name(), "John Doe")

    def test_set_person_name(self):
        self.__person.set_person_name("Jane Doe")
        self.assertEqual(self.__person.get_person_name(), "Jane Doe")

    def test_add_person_to_event(self):
        self.__person.add_person_to_event("1")

    def test_remove_any_connections_with_person_id(self):
        self.__person.add_person_to_event("1")
        self.__person.remove_any_connections_with_person_id()

    def test_get_number_of_events_person_joined(self):
        self.__person.add_person_to_event("1")
        self.__person.add_person_to_event("2")
        self.assertEqual(self.__person.get_number_of_events_person_joined(), 2)

    def test_get_event_ids_that_corespond_to_person_id(self):
        self.__person.add_person_to_event("1")
        self.__person.add_person_to_event("2")
        self.assertEqual(self.__person.get_event_ids_that_corespond_to_person_id(), ["1", "2"])

    def test_eq(self):
        other_person = person_class("1", "John Doe", "USA", "New York", "Broadway", "123", person_event_class())
        self.assertEqual(self.__person, other_person)

    def test_str(self):
        expected_output = "ID:        1\nNume:      John Doe\nTara:      USA\nOras:      New York\nStrada:    Broadway\nNumar:     123\nNr. evenimente: 0"
        self.assertEqual(str(self.__person), expected_output)
