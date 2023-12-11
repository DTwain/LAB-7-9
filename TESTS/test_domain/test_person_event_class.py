import unittest
from DOMAIN.person_event import person_event_class

class test_person_event_class(unittest.TestCase):
    def setUp(self):
        self.person_event = person_event_class()

    def tearDown(self):
        self.person_event = None

    def test_add_person_to_event(self):
        self.person_event.add_person_to_event("1", "1")
        self.assertEqual(self.person_event.get_number_of_people_joined_to_event("1"), 1)
        self.assertEqual(self.person_event.get_number_of_events_person_joined("1"), 1)

        self.person_event.add_person_to_event("1", "2")
        self.assertEqual(self.person_event.get_number_of_people_joined_to_event("2"), 1)
        self.assertEqual(self.person_event.get_number_of_events_person_joined("1"), 2)

        self.person_event.add_person_to_event("2", "1")
        self.assertEqual(self.person_event.get_number_of_people_joined_to_event("1"), 2)
        self.assertEqual(self.person_event.get_number_of_events_person_joined("2"), 1)

    def test_remove_person_id_from_all_lists(self):
        self.person_event.add_person_to_event("1", "1")
        self.person_event.add_person_to_event("1", "2")
        self.person_event.add_person_to_event("2", "1")

        self.person_event.remove_person_id_from_all_lists("1")
        self.assertEqual(self.person_event.get_number_of_people_joined_to_event("1"), 1)
        self.assertEqual(self.person_event.get_number_of_events_person_joined("1"), 0)
        self.assertEqual(self.person_event.get_number_of_events_person_joined("2"), 1)

        self.person_event.remove_person_id_from_all_lists("2")
        self.assertEqual(self.person_event.get_number_of_people_joined_to_event("1"), 0)
        self.assertEqual(self.person_event.get_number_of_events_person_joined("2"), 0)

    def test_remove_event_id_from_all_lists(self):
        self.person_event.add_person_to_event("1", "1")
        self.person_event.add_person_to_event("1", "2")
        self.person_event.add_person_to_event("2", "1")

        self.person_event.remove_event_id_from_all_lists("1")
        self.assertEqual(self.person_event.get_number_of_people_joined_to_event("1"), 0)
        self.assertEqual(self.person_event.get_number_of_events_person_joined("1"), 1)
        self.assertEqual(self.person_event.get_number_of_events_person_joined("2"), 0)

        self.person_event.remove_event_id_from_all_lists("2")
        self.assertEqual(self.person_event.get_number_of_events_person_joined("1"), 0)

    def test_get_number_of_people_joined_to_event(self):
        self.assertEqual(self.person_event.get_number_of_people_joined_to_event("1"), 0)

        self.person_event.add_person_to_event("1", "1")
        self.assertEqual(self.person_event.get_number_of_people_joined_to_event("1"), 1)

        self.person_event.add_person_to_event("2", "1")
        self.assertEqual(self.person_event.get_number_of_people_joined_to_event("1"), 2)

    def test_get_number_of_events_person_joined(self):
        self.assertEqual(self.person_event.get_number_of_events_person_joined("1"), 0)

        self.person_event.add_person_to_event("1", "1")
        self.assertEqual(self.person_event.get_number_of_events_person_joined("1"), 1)

        self.person_event.add_person_to_event("1", "2")
        self.assertEqual(self.person_event.get_number_of_events_person_joined("1"), 2)

    def test_get_event_ids_that_corespond_to_person_id(self):
        self.person_event.add_person_to_event("1", "1")
        self.person_event.add_person_to_event("1", "2")
        self.person_event.add_person_to_event("2", "1")

        self.assertEqual(self.person_event.get_event_ids_that_corespond_to_person_id("1"), ["1", "2"])
        self.assertEqual(self.person_event.get_event_ids_that_corespond_to_person_id("2"), ["1"])

    def test_get_list_of_people_ids_that_joined_event(self):
        self.person_event.add_person_to_event("1", "1")
        self.person_event.add_person_to_event("2", "1")
        self.person_event.add_person_to_event("3", "1")

        self.assertEqual(self.person_event.get_list_of_people_ids_that_joined_event("1"), "1, 2, 3")

    def test_get_list_of_events_ids_that_person_joined(self):
        self.person_event.add_person_to_event("1", "1")
        self.person_event.add_person_to_event("1", "2")
        self.person_event.add_person_to_event("1", "3")

        self.assertEqual(self.person_event.get_list_of_events_ids_that_person_joined("1"), "1, 2, 3")
