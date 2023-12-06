import unittest

from DOMAIN.event import event_class
from REPOSITORIES.repo_evenimente import repo_events
from MY_CUSTOM_EXCEPTIONS.repo_custom_exception import inexistent_id_exception, dublicated_id_exception

class test_repo_events(unittest.TestCase):
    def setUp(self):
        self.repo = repo_events()

    def tearDown(self):
        self.repo = None

    def test_add_event_class(self):
        event1 = event_class("1", "12/2/2020", "120", "Concertul lui travis Scott")
        self.repo.add_event(event1)
        self.assertEqual(len(self.repo), 1)
        self.assertEqual(self.repo.get_event_through_id("1"), event1)

        event2 = event_class("1", "28/2/2022", "200", "Serbarea clasei a 3 - a")
        with self.assertRaises(dublicated_id_exception):
            self.repo.add_event(event2)

    def test_delete_event_class(self):
        event1 = event_class("1", "12/2/2020", "120", "Concertul lui travis Scott")
        self.repo.add_event(event1)
        self.assertEqual(len(self.repo), 1)

        deleted_event = self.repo.delete_event("1")
        self.assertEqual(len(self.repo), 0)
        self.assertEqual(deleted_event, event1)

        with self.assertRaises(inexistent_id_exception):
            self.repo.delete_event("1")

    def test_update_event_class(self):
        event1 = event_class("1", "12/2/2020", "120", "Concertul lui travis Scott")
        self.repo.add_event(event1)

        updated_event = event_class("1", "28/2/2022", "", "Serbarea clasei a 3 - a")
        old_event = self.repo.update_event(updated_event, "1")
        self.assertEqual(self.repo.get_event_through_id("1"), event_class("1", "28/2/2022", "120", "Serbarea clasei a 3 - a"))
        self.assertEqual(old_event, event1)

        with self.assertRaises(inexistent_id_exception):
            self.repo.update_event(updated_event, "2")

    def test_get_event_through_id(self):
        event1 = event_class("1", "12/2/2020", "120", "Concertul lui travis Scott")
        self.repo.add_event(event1)

        retrieved_event = self.repo.get_event_through_id("1")
        self.assertEqual(retrieved_event, event1)

        with self.assertRaises(inexistent_id_exception):
            self.repo.get_event_through_id("2")

    def test_get_events_that_corespond_to_id(self):
        event1 = event_class("1", "12/2/2020", "120", "Concertul lui travis Scott")
        event2 = event_class("2", "28/2/2022", "200", "Serbarea clasei a 3 - a")
        self.repo.add_event(event1)
        self.repo.add_event(event2)

        id_list = ["1", "2"]
        events = self.repo.get_events_that_corespond_to_id(id_list)
        self.assertEqual(events, [event1, event2])

    def test_get_list_of_DTO_obj_for_third_report(self):
        event1 = event_class("1", "12/2/2020", "120", "Concertul lui travis Scott")
        event2 = event_class("2", "28/2/2022", "200", "Serbarea clasei a 3 - a")
        self.repo.add_event(event1)
        self.repo.add_event(event2)

        DTO_list = self.repo.get_list_of_DTO_obj_for_third_report()
        self.assertEqual(len(DTO_list), 2)
        self.assertEqual(DTO_list[0].get_event_id(), "1")
        self.assertEqual(DTO_list[0].get_number_of_people(), 0)
        self.assertEqual(DTO_list[1].get_event_id(), "2")
        self.assertEqual(DTO_list[1].get_number_of_people(), 0)

    def test_get_all(self):
        event1 = event_class("1", "12/2/2020", "120", "Concertul lui travis Scott")
        event2 = event_class("2", "28/2/2022", "200", "Serbarea clasei a 3 - a")
        self.repo.add_event(event1)
        self.repo.add_event(event2)

        all_events = self.repo.get_all()
        self.assertEqual(all_events, [event1, event2])

    def test_get_all_ids(self):
        event1 = event_class("1", "12/2/2020", "120", "Concertul lui travis Scott")
        event2 = event_class("2", "28/2/2022", "200", "Serbarea clasei a 3 - a")
        self.repo.add_event(event1)
        self.repo.add_event(event2)

        all_ids = self.repo.get_all_ids()
        self.assertEqual(all_ids, ["1", "2"])

