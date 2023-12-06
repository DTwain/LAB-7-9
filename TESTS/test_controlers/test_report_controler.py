import unittest

from DOMAIN.event import event_class
from DOMAIN.person import person_class
from DOMAIN.DTO import DTO_for_second_report, DTO_for_third_report
from CONTROLLERS.report_controler import report_controler
from REPOSITORIES.repo_evenimente import repo_events
from REPOSITORIES.repo_persoane import repo_people
from DOMAIN.VALIDARI.validare_persoana import valid_person
from DOMAIN.VALIDARI.validare_event import valid_event
from MY_CUSTOM_EXCEPTIONS.validation_exceptions import person_validation_exception, event_validation_exception
from MY_CUSTOM_EXCEPTIONS.repo_custom_exception import repo_custom_exception

class test_report_controler(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.__event_validator = valid_event()
        cls.__event_repo = repo_events()
        cls.__person_validator = valid_person()
        cls.__person_repo = repo_people()
        cls.__report_controler = report_controler(cls.__person_repo, cls.__event_repo)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.__event_validator = None
        cls.__event_repo = None 
        cls.__person_validator = None
        cls.__person_repo = None
        cls.__report_controler = None

    def setUp(self) -> None:
        self.__event_repo.add_event(event_class("1", "12/2/2020", "120", "Concertul lui travis Scott"))
        self.__event_repo.add_event(event_class("2", "28/2/2022", "200", "Serbarea clasei a 3 - a"))
        self.__event_repo.add_event(event_class("3", "12/2/2021", "300", "Balul Bobocilor"))

        self.__person_repo.add_person_to_rep(person_class("1", "Popescu Niculae", "ROmania", "Tulcea", "Luminii", "122"))
        self.__person_repo.add_person_to_rep(person_class("3", "Jonny Bravo", "Arizona", "Pheonix", "Van Buren", "14"))
        self.__person_repo.add_person_to_rep(person_class("12AB", "Ungureanu Marian", "Romania", "Targu-Neamt", "Bulevardul Adormirea Marici Domnului", "11A"))

    def tearDown(self) -> None:
        events_ids = self.__event_repo.get_all_ids()
        for event_id in events_ids:
            self.__event_repo.delete_event(event_id)

        people_ids = self.__person_repo.get_all_ids()
        for person_id in people_ids:
            self.__person_repo.remove_person(person_id)

    def test_first_report(self):
        person_1 = self.__person_repo.get_person_through_id("1")
        person_1.add_event_to_person("1")
        person_1.add_event_to_person("3")

        person_2 = self.__person_repo.get_person_through_id("3")
        person_2.add_event_to_person("3")

        person_3 = self.__person_repo.get_person_through_id("12AB")
        person_3.add_event_to_person("1")
        person_3.add_event_to_person("2")

        self.__person_repo.update_person(person_1, "1")
        self.__person_repo.update_person(person_2, "3")
        self.__person_repo.update_person(person_3, "12AB")

        list_of_sorted_events = self.__report_controler.first_report("1")
        self.assertEqual(len(list_of_sorted_events), 2)
        self.assertEqual(list_of_sorted_events[0], event_class("3", "12/2/2021", "300", "Balul Bobocilor"))
        self.assertEqual(list_of_sorted_events[1], event_class("1", "12/2/2020", "120", "Concertul lui travis Scott"))

    def test_second_report(self):
        person_1 = self.__person_repo.get_person_through_id("1")
        person_1.add_event_to_person("1")
        person_1.add_event_to_person("3")

        person_2 = self.__person_repo.get_person_through_id("3")
        person_2.add_event_to_person("3")

        person_3 = self.__person_repo.get_person_through_id("12AB")
        person_3.add_event_to_person("1")
        person_3.add_event_to_person("2")

        self.__person_repo.update_person(person_1, "1")
        self.__person_repo.update_person(person_2, "3")
        self.__person_repo.update_person(person_3, "12AB")

        list_of_people_with_max_number_of_events = self.__report_controler.second_report()
        self.assertEqual(len(list_of_people_with_max_number_of_events), 2)
        self.assertEqual(list_of_people_with_max_number_of_events[0], person_class("1", "Popescu Niculae", "ROmania", "Tulcea", "Luminii", "122"))
        self.assertEqual(list_of_people_with_max_number_of_events[1], person_class("12AB", "Ungureanu Marian", "Romania", "Targu-Neamt", "Bulevardul Adormirea Marici Domnului", "11A"))

        person_3 = self.__person_repo.get_person_through_id("12AB")
        person_3.add_event_to_person("3")
        self.__person_repo.update_person(person_3, "12AB")
        list_of_people_with_max_number_of_events = self.__report_controler.second_report()
        self.assertEqual(len(list_of_people_with_max_number_of_events), 1)
        self.assertEqual(list_of_people_with_max_number_of_events[0], person_class("12AB", "Ungureanu Marian", "Romania", "Targu-Neamt", "Bulevardul Adormirea Marici Domnului", "11A"))

    def test_third_report(self):
        self.__person_repo.add_person_to_rep(person_class("3B", "Mario Gotze", "Germania", "Dortmund", "Borussia", "11"))

        self.__event_repo.add_event(event_class("4", "3/4/2023", "55", "Concertul lui Drake"))
        self.__event_repo.add_event(event_class("5", "23/9/2023", "70", "Concertul lui Kendrik Lamar"))
        self.__event_repo.add_event(event_class("6", "9/1/2023", "110", "Concertul lui Post Malone"))
        self.__event_repo.add_event(event_class("7", "18/2/2023", "120", "Concertul lui DaBaby"))

        person_1 = self.__person_repo.get_person_through_id("1")
        person_1.add_event_to_person("1")
        person_1.add_event_to_person("3")
        person_1.add_event_to_person("7")

        person_2 = self.__person_repo.get_person_through_id("3")
        person_2.add_event_to_person("3")
        person_2.add_event_to_person("5")
        person_2.add_event_to_person("6")

        person_3 = self.__person_repo.get_person_through_id("12AB")
        person_3.add_event_to_person("1")
        person_3.add_event_to_person("2")

        person_4 = self.__person_repo.get_person_through_id("3B")
        person_3.add_event_to_person("2")
        person_4.add_event_to_person("5")
        person_4.add_event_to_person("6")
        person_4.add_event_to_person("7")

        self.__person_repo.update_person(person_1, "1")
        self.__person_repo.update_person(person_2, "3")
        self.__person_repo.update_person(person_3, "12AB")
        self.__person_repo.update_person(person_4, "3B")

        list_of_twenty_percent_of_events = self.__report_controler.third_report()
        self.assertEqual(len(list_of_twenty_percent_of_events), 2)
        self.assertEqual(type(list_of_twenty_percent_of_events[0]), event_class)
        """
        evenimentul 1 are 2 participanti
        evenimentul 2 are 2 participanti
        evenimentul 3 are 2 participanti
        evenimentul 4 are 0 participanti
        evenimentul 5 are 2 participanti
        evenimentul 6 are 2 participanti
        evenimentul 7 are 2 participanti
        """

