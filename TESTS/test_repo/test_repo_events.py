import unittest

from DOMAIN.event import event_class
from DOMAIN.person_event import person_event_class
from REPOSITORIES.repo_evenimente import repo_events
from MY_CUSTOM_EXCEPTIONS.repo_custom_exception import inexistent_event_id_exception, dublicated_id_exception

class test_repo_events(unittest.TestCase):
    def setUp(self):
        self.__shared_person_event_class = person_event_class()
        self.__repo = repo_events()

    def tearDown(self):
        self.__shared_person_event_class = None
        self.__repo = None

    def test_add_event_class(self):
        event1 = event_class("1", "12/2/2020", "120", "Concertul lui travis Scott", self.__shared_person_event_class)
        self.__repo.add_event(event1)
        self.assertEqual(len(self.__repo), 1)
        self.assertEqual(self.__repo.get_event_through_id("1"), event1)

        event2 = event_class("1", "28/2/2022", "200", "Serbarea clasei a 3 - a", self.__shared_person_event_class)
        with self.assertRaises(dublicated_id_exception):
            self.__repo.add_event(event2)

    def test_delete_event_class(self):
        event1 = event_class("1", "12/2/2020", "120", "Concertul lui travis Scott", self.__shared_person_event_class)
        self.__repo.add_event(event1)
        self.assertEqual(len(self.__repo), 1)

        deleted_event = self.__repo.delete_event("1")
        self.assertEqual(len(self.__repo), 0)
        self.assertEqual(deleted_event, event1)

        with self.assertRaises(inexistent_event_id_exception):
            self.__repo.delete_event("1")

    def test_update_event_class(self):
        event1 = event_class("1", "12/2/2020", "120", "Concertul lui travis Scott", self.__shared_person_event_class)
        self.__repo.add_event(event1)

        updated_event = event_class("1", "28/2/2022", "", "Serbarea clasei a 3 - a", self.__shared_person_event_class)
        old_event = self.__repo.update_event(updated_event, "1")
        self.assertEqual(self.__repo.get_event_through_id("1"), event_class("1", "28/2/2022", "120", "Serbarea clasei a 3 - a", person_event_class()))
        self.assertEqual(old_event, event1)

        with self.assertRaises(inexistent_event_id_exception):
            self.__repo.update_event(updated_event, "2")

    def test_get_event_through_id(self):
        event1 = event_class("1", "12/2/2020", "120", "Concertul lui travis Scott", self.__shared_person_event_class)
        self.__repo.add_event(event1)

        retrieved_event = self.__repo.get_event_through_id("1")
        self.assertEqual(retrieved_event, event1)

        with self.assertRaises(inexistent_event_id_exception):
            self.__repo.get_event_through_id("2")

    def test_get_events_that_corespond_to_id(self):
        event1 = event_class("1", "12/2/2020", "120", "Concertul lui travis Scott", self.__shared_person_event_class)
        event2 = event_class("2", "28/2/2022", "200", "Serbarea clasei a 3 - a", self.__shared_person_event_class)
        self.__repo.add_event(event1)
        self.__repo.add_event(event2)

        id_list = ["1", "2"]
        events = self.__repo.get_events_that_corespond_to_id(id_list)
        self.assertEqual(events, [event1, event2])

    def test_get_list_of_DTO_obj_for_third_report(self):
        event1 = event_class("1", "12/2/2020", "120", "Concertul lui travis Scott", self.__shared_person_event_class)
        event2 = event_class("2", "28/2/2022", "200", "Serbarea clasei a 3 - a", self.__shared_person_event_class)
        self.__repo.add_event(event1)
        self.__repo.add_event(event2)

        DTO_list = self.__repo.get_list_of_DTO_obj_for_third_report()
        self.assertEqual(len(DTO_list), 2)
        self.assertEqual(DTO_list[0].get_event_id(), "1")
        self.assertEqual(DTO_list[0].get_number_of_people(), 0)
        self.assertEqual(DTO_list[1].get_event_id(), "2")
        self.assertEqual(DTO_list[1].get_number_of_people(), 0)

    def test_get_all(self):
        event1 = event_class("1", "12/2/2020", "120", "Concertul lui travis Scott", self.__shared_person_event_class)
        event2 = event_class("2", "28/2/2022", "200", "Serbarea clasei a 3 - a", self.__shared_person_event_class)
        self.__repo.add_event(event1)
        self.__repo.add_event(event2)

        all_events = self.__repo.get_all()
        self.assertEqual(all_events, [event1, event2])

    def test_get_all_ids(self):
        event1 = event_class("1", "12/2/2020", "120", "Concertul lui travis Scott", self.__shared_person_event_class)
        event2 = event_class("2", "28/2/2022", "200", "Serbarea clasei a 3 - a", self.__shared_person_event_class)
        self.__repo.add_event(event1)
        self.__repo.add_event(event2)

        all_ids = self.__repo.get_all_ids()
        self.assertEqual(all_ids, ["1", "2"])

