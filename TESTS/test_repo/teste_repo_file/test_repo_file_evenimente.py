import unittest
import shutil
from REPOSITORIES.repo_evenimente import repo_events
from REPOSITORIES.repo_file_evenimente import repo_file_event
from DOMAIN.event import event_class
from DOMAIN.person_event import person_event_class

class test_repo_file_event(unittest.TestCase):
    def setUp(self):
        shutil.copyfile("TESTS/test_repo/teste_repo_file/test_repo_file_events_backup.txt", "TESTS/test_repo/teste_repo_file/test_repo_file_events.txt")
        self.__repo = repo_file_event("TESTS/test_repo/teste_repo_file/test_repo_file_events.txt")

    def tearDown(self):
        for event_id in self.__repo.get_all_ids():
            self.__repo.delete_event(event_id)
        self.__repo = None
    
    def test_load_from_file(self):
        self.assertEqual(len(self.__repo), 3)
        self.assertEqual(self.__repo.get_event_through_id("1").get_event_date(), "12/2/2020")
        self.assertEqual(self.__repo.get_event_through_id("1").get_event_duration(), "120")
        self.assertEqual(self.__repo.get_event_through_id("1").get_event_description(), "Concertul lui travis Scott")
        self.assertEqual(self.__repo.get_event_through_id("1").get_number_of_people_joined_to_event(), 0)

        self.assertEqual(self.__repo.get_event_through_id("2").get_event_date(), "28/2/2022")
        self.assertEqual(self.__repo.get_event_through_id("2").get_event_duration(), "200")
        self.assertEqual(self.__repo.get_event_through_id("2").get_event_description(), "Serbarea clasei a 3 - a")
        self.assertEqual(self.__repo.get_event_through_id("2").get_number_of_people_joined_to_event(), 3)

        self.assertEqual(self.__repo.get_event_through_id("3").get_event_date(), "12/2/2021")
        self.assertEqual(self.__repo.get_event_through_id("3").get_event_duration(), "300")
        self.assertEqual(self.__repo.get_event_through_id("3").get_event_description(), "Balul Bobocilor")
        self.assertEqual(self.__repo.get_event_through_id("3").get_number_of_people_joined_to_event(), 1)

    def test_store_to_file(self):
        with open("TESTS/test_repo/teste_repo_file/test_repo_file_events.txt", "r") as file:
            lines = file.readlines()
            self.assertEqual(len(lines), 3)
            self.assertEqual(lines[2], "3;12/2/2021;300;Balul Bobocilor;3")
        
        self.__repo.delete_event("2")
        with open("TESTS/test_repo/teste_repo_file/test_repo_file_events.txt", "r") as file:
            lines = file.readlines()
            self.assertEqual(len(lines), 2)

    def test_add_event(self):
        self.__repo.add_event(event_class("4", "14/1/2021", "80", "Meci de fotbal", person_event_class()))
        self.assertEqual(len(self.__repo), 4)
        self.assertEqual(self.__repo.get_event_through_id("4"), event_class("4", "14/1/2021", "80", "Meci de fotbal", person_event_class))
        
        with self.assertRaises(Exception):
            self.__repo.add_event(event_class("4", "14/1/2021", "80", "Meci de fotbal", person_event_class()))
            self.__repo.add_event(event_class("5", "14/1/2021", "", "Meci de fotbal", person_event_class()))
            self.__repo.add_event(event_class("6", "14/1/2021", "80", "", person_event_class()))
            self.__repo.add_event(event_class("7", "29/2/2022", "80", "Meci de fotbal", person_event_class()))
            self.__repo.add_event(event_class("8", "", "80", "Meci de fotbal", person_event_class()))
            self.__repo.add_event(event_class("9", "", "", "", person_event_class()))
    
    def test_remove_event(self):
        self.__repo.delete_event("2")
        self.assertEqual(len(self.__repo), 2)
        
        self.assertEqual(self.__repo.get_event_through_id("1").get_event_id(), "1")
        self.assertEqual(self.__repo.get_event_through_id("1").get_event_date(), "12/2/2020")
        self.assertEqual(self.__repo.get_event_through_id("1").get_event_duration(), "120")
        self.assertEqual(self.__repo.get_event_through_id("1").get_event_description(), "Concertul lui travis Scott")
        self.assertEqual(self.__repo.get_event_through_id("1").get_number_of_people_joined_to_event(), 0)

        self.assertEqual(self.__repo.get_event_through_id("3").get_event_id(), "3")
        self.assertEqual(self.__repo.get_event_through_id("3").get_event_date(), "12/2/2021")
        self.assertEqual(self.__repo.get_event_through_id("3").get_event_duration(), "300")
        self.assertEqual(self.__repo.get_event_through_id("3").get_event_description(), "Balul Bobocilor")
        self.assertEqual(self.__repo.get_event_through_id("3").get_number_of_people_joined_to_event(), 1)

        with self.assertRaises(Exception):
            self.__repo.delete_event("2")
            self.__repo.delete_event("5")

    def test_update_event(self):
        self.__repo.update_event(event_class("2", "15/7/2023", "150", "Serbarea clasei a 2 - a", self.__repo.get_shared_person_event_class()), "2")
        self.assertEqual(self.__repo.get_event_through_id("2").get_event_id(), "2")
        self.assertEqual(self.__repo.get_event_through_id("2").get_event_date(), "15/7/2023")
        self.assertEqual(self.__repo.get_event_through_id("2").get_event_duration(), "150")
        self.assertEqual(self.__repo.get_event_through_id("2").get_event_description(), "Serbarea clasei a 2 - a")
        self.assertEqual(self.__repo.get_event_through_id("2").get_number_of_people_joined_to_event(), 3)

        with self.assertRaises(Exception):
            self.__repo.update_event(event_class("2", "", "150", "Serbarea clasei a 2 - a", person_event_class()), "5")
            self.__repo.update_event(event_class("5", "", "150", "Serbarea clasei a 2 - a", person_event_class()), "2")
            self.__repo.update_event(event_class("2", "", "150", "Serbarea clasei a 2 - a", person_event_class()), "2")

    def test_get_event_through_id(self):
        event = self.__repo.get_event_through_id("2")
        self.assertEqual(event.get_event_id(), "2")
        self.assertEqual(event.get_event_date(), "28/2/2022")
        self.assertEqual(event.get_event_duration(), "200")
        self.assertEqual(event.get_event_description(), "Serbarea clasei a 3 - a")
        self.assertEqual(event.get_number_of_people_joined_to_event(), 3)

        with self.assertRaises(Exception):
            self.__repo.get_event_through_id("5")
            self.__repo.get_event_through_id("")

    def test_get_events_that_corespond_to_id(self):
        events_id_list = ["1", "2"]

        events = self.__repo.get_events_that_corespond_to_id(events_id_list)
        self.assertEqual(len(events), 2)
        self.assertEqual(events[0].get_event_id(), "1")
        self.assertEqual(events[0].get_event_date(), "12/2/2020")
        self.assertEqual(events[0].get_event_duration(), "120")
        self.assertEqual(events[0].get_event_description(), "Concertul lui travis Scott")
        self.assertEqual(events[0].get_number_of_people_joined_to_event(), 0)

        self.assertEqual(events[1].get_event_id(), "2")
        self.assertEqual(events[1].get_event_date(), "28/2/2022")
        self.assertEqual(events[1].get_event_duration(), "200")
        self.assertEqual(events[1].get_event_description(), "Serbarea clasei a 3 - a")
        self.assertEqual(events[1].get_number_of_people_joined_to_event(), 3)

        with self.assertRaises(Exception):
            self.__repo.get_events_that_corespond_to_id(["1", "2", "5"])
            self.__repo.get_events_that_corespond_to_id(["1", "2", ""])

    def test_get_list_of_DTO_obj_for_third_report(self):
        list_of_DTO_obj = self.__repo.get_list_of_DTO_obj_for_third_report()
        self.assertEqual(len(list_of_DTO_obj), 3)
        self.assertEqual(list_of_DTO_obj[0].get_event_id(), "1")
        self.assertEqual(list_of_DTO_obj[0].get_number_of_people(), 0)

        self.assertEqual(list_of_DTO_obj[1].get_event_id(), "2")
        self.assertEqual(list_of_DTO_obj[1].get_number_of_people(), 3)

        self.assertEqual(list_of_DTO_obj[2].get_event_id(), "3")
        self.assertEqual(list_of_DTO_obj[2].get_number_of_people(), 1)

    def test_get_all_ids(self):
        self.assertEqual(self.__repo.get_all_ids(), ["1", "2", "3"])




        