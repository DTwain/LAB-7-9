import unittest

from DOMAIN.event import event_class
from DOMAIN.person import person_class
from DOMAIN.person_event import person_event_class
from CONTROLLERS.report_controler import report_controler
from REPOSITORIES.repo_evenimente import repo_events
from REPOSITORIES.repo_persoane import repo_people

class test_report_controler(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.__event_repo = repo_events()
        cls.__person_repo = repo_people()
        cls.__shared_person_event_class = person_event_class()
        cls.__report_controler = report_controler(cls.__person_repo, cls.__event_repo, cls.__shared_person_event_class)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.__event_repo = None
        cls.__person_repo = None
        cls.__shared_person_event_class = None
        cls.__report_controler = None

    def setUp(self) -> None:
        self.__event_repo.add_event(event_class("1", "12/2/2020", "120", "Concertul lui travis Scott", self.__shared_person_event_class))
        self.__event_repo.add_event(event_class("2", "28/2/2022", "200", "Serbarea clasei a 3 - a", self.__shared_person_event_class))
        self.__event_repo.add_event(event_class("3", "12/2/2021", "300", "Balul Bobocilor", self.__shared_person_event_class))

        self.__person_repo.add_person_to_rep(person_class("1", "Popescu Niculae", "ROmania", "Tulcea", "Luminii", "122", self.__shared_person_event_class))
        self.__person_repo.add_person_to_rep(person_class("3", "Jonny Bravo", "Arizona", "Pheonix", "Van Buren", "14", self.__shared_person_event_class))
        self.__person_repo.add_person_to_rep(person_class("12AB", "Ungureanu Marian", "Romania", "Targu-Neamt", "Bulevardul Adormirea Marici Domnului", "11A", self.__shared_person_event_class))

    def tearDown(self) -> None:
        events_ids = self.__event_repo.get_all_ids()
        for event_id in events_ids:
            self.__event_repo.delete_event(event_id)

        people_ids = self.__person_repo.get_all_ids()
        for person_id in people_ids:
            self.__person_repo.remove_person(person_id)

    def test_first_report(self):
        person_1 = self.__person_repo.get_person_through_id("1")
        person_1.add_person_to_event("1")
        person_1.add_person_to_event("3")

        person_2 = self.__person_repo.get_person_through_id("3")
        person_2.add_person_to_event("3")

        person_3 = self.__person_repo.get_person_through_id("12AB")
        person_3.add_person_to_event("1")
        person_3.add_person_to_event("2")


        list_of_sorted_events = self.__report_controler.first_report("1")
        self.assertEqual(len(list_of_sorted_events), 2)
        self.assertEqual(list_of_sorted_events[0], event_class("3", "12/2/2021", "300", "Balul Bobocilor", person_event_class))
        self.assertEqual(list_of_sorted_events[1], event_class("1", "12/2/2020", "120", "Concertul lui travis Scott", person_event_class))

    def test_second_report(self):
        person_1 = self.__person_repo.get_person_through_id("1")
        person_1.add_person_to_event("1")
        person_1.add_person_to_event("3")

        person_2 = self.__person_repo.get_person_through_id("3")
        person_2.add_person_to_event("3")

        person_3 = self.__person_repo.get_person_through_id("12AB")
        person_3.add_person_to_event("1")
        person_3.add_person_to_event("2")


        list_of_people_with_max_number_of_events = self.__report_controler.second_report()
        self.assertEqual(len(list_of_people_with_max_number_of_events), 2)
        self.assertEqual(list_of_people_with_max_number_of_events[0], person_class("1", "Popescu Niculae", "ROmania", "Tulcea", "Luminii", "122", person_event_class()))
        self.assertEqual(list_of_people_with_max_number_of_events[1], person_class("12AB", "Ungureanu Marian", "Romania", "Targu-Neamt", "Bulevardul Adormirea Marici Domnului", "11A", person_event_class()))

        person_3 = self.__person_repo.get_person_through_id("12AB")
        person_3.add_person_to_event("3")
        self.__person_repo.update_person(person_3, "12AB")
        list_of_people_with_max_number_of_events = self.__report_controler.second_report()
        self.assertEqual(len(list_of_people_with_max_number_of_events), 1)
        self.assertEqual(list_of_people_with_max_number_of_events[0], person_class("12AB", "Ungureanu Marian", "Romania", "Targu-Neamt", "Bulevardul Adormirea Marici Domnului", "11A", person_event_class))

    def test_third_report(self):
        self.__person_repo.add_person_to_rep(person_class("3B", "Mario Gotze", "Germania", "Dortmund", "Borussia", "11", self.__shared_person_event_class))

        self.__event_repo.add_event(event_class("4", "3/4/2023", "55", "Concertul lui Drake", self.__shared_person_event_class))
        self.__event_repo.add_event(event_class("5", "23/9/2023", "70", "Concertul lui Kendrik Lamar", self.__shared_person_event_class))
        self.__event_repo.add_event(event_class("6", "9/1/2023", "110", "Concertul lui Post Malone", self.__shared_person_event_class))
        self.__event_repo.add_event(event_class("7", "18/2/2023", "120", "Concertul lui DaBaby", self.__shared_person_event_class))

        event_1 = self.__event_repo.get_event_through_id("1")
        event_1.add_person_to_event("1")
        event_1.add_person_to_event("3")

        event_2 = self.__event_repo.get_event_through_id("2")
        event_2.add_person_to_event("3B")
        event_2.add_person_to_event("12AB")

        event_3 = self.__event_repo.get_event_through_id("3")
        event_3.add_person_to_event("12AB")
        event_3.add_person_to_event("3B")

        event_4 = self.__event_repo.get_event_through_id("4")
        event_4.add_person_to_event("1")

        event_5 = self.__event_repo.get_event_through_id("5")
        event_5.add_person_to_event("12AB")
        event_5.add_person_to_event("3B")

        event_6 = self.__event_repo.get_event_through_id("6")
        event_6.add_person_to_event("1")
        event_6.add_person_to_event("3")

        event_7 = self.__event_repo.get_event_through_id("7")
        event_7.add_person_to_event("3B")
        event_7.add_person_to_event("1")


        list_of_twenty_percent_of_events = self.__report_controler.third_report()
        self.assertEqual(len(list_of_twenty_percent_of_events), 2)
        self.assertEqual(type(list_of_twenty_percent_of_events[0]), event_class)

