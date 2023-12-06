import unittest

from CONTROLLERS.person_controler import person_controler
from DOMAIN.VALIDARI.validare_persoana import valid_person
from DOMAIN.VALIDARI.validare_event import valid_event
from REPOSITORIES.repo_persoane import repo_people
from REPOSITORIES.repo_evenimente import repo_events
from CONTROLLERS.event_controler import event_controler
from MY_CUSTOM_EXCEPTIONS.validation_exceptions import person_validation_exception
from MY_CUSTOM_EXCEPTIONS.repo_custom_exception import repo_custom_exception

class test_person_controler(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.__event_validator = valid_event()
        cls.__event_repo = repo_events()
        cls.__event_controler = event_controler(cls.__event_repo, cls.__event_validator)

        cls.__person_validator = valid_person()
        cls.__person_repo = repo_people()
        cls.__person_controler = person_controler(cls.__person_repo, cls.__person_validator, cls.__event_controler)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.__event_validator = None
        cls.__event_repo = None
        cls.__event_controler = None

        cls.__person_validator = None
        cls.__person_repo = None
        cls.__person_controler = None

    def setUp(self) -> None:
        self.__event_controler.add_event("1", "12/2/2020", "120", "Concertul lui travis Scott")
        self.__event_controler.add_event("2", "28/2/2022", "200", "Serbarea clasei a 3 - a")
        self.__event_controler.add_event("3", "12/2/2021", "300", "Balul Bobocilor")

        self.__person_controler.add_person("1", "Popescu Niculae", "ROmania", "Tulcea", "Luminii", "122")
        self.__person_controler.add_person("3", "Jonny Bravo", "Arizona", "Pheonix", "Van Buren", "14")
        self.__person_controler.add_person("12AB", "Ungureanu Marian", "Romania", "Targu-Neamt", "Bulevardul Adormirea Marici Domnului", "11A")

    def tearDown(self) -> None:
        events_ids = self.__event_repo.get_all_ids()
        for event_id in events_ids:
            self.__event_repo.delete_event(event_id)

        people_ids = self.__person_repo.get_all_ids()
        for person_id in people_ids:
            self.__person_repo.remove_person(person_id)

    def test_add_person(self):
        self.__person_controler.add_person("4", "Popescu Niculae", "ROmania", "Tulcea", "Luminii", "122")
        with self.assertRaises((person_validation_exception, repo_custom_exception)):
            self.__person_controler.add_person("4", "Popescu Niculae", "ROmania", "Tulcea", "Luminii", "122")
            self.__person_controler.add_person("5", "Popescu Niculae", "ROmania", "Tulcea", "Luminii", "")
            self.__person_controler.add_person("6", "Popescu Niculae", "ROmania", "Tulcea", "", "122")
            self.__person_controler.add_person("7", "Popescu Niculae", "ROmania", "", "Luminii", "122")
            self.__person_controler.add_person("8", "Popescu Niculae", "", "Tulcea", "Luminii", "122")
            self.__person_controler.add_person("9", "", "ROmania", "Tulcea", "Luminii", "122")
            self.__person_controler.add_person("10", "", "", "", "", "")

        person_1 = self.__person_controler.find_person_by_id("3")
        self.assertEqual(person_1.get_person_id(), "3")
        self.assertEqual(person_1.get_person_name(), "Jonny Bravo")
        self.assertEqual(person_1.get_country(), "Arizona")
        self.assertEqual(person_1.get_city(), "Pheonix")
        self.assertEqual(person_1.get_street(), "Van Buren")
        self.assertEqual(person_1.get_number_of_the_house(), "14")
        self.assertEqual(person_1.get_events_id(), [])

    def test_remove_person(self):
        self.__person_controler.remove_person("3")
        with self.assertRaises(repo_custom_exception):
            self.__person_controler.remove_person("3")
            self.__person_controler.remove_person("4")
            self.__person_controler.remove_person("5")
        
    def test_find_person_by_id(self):
        person = self.__person_controler.find_person_by_id("3")
        self.assertEqual(person.get_person_id(), "3")
        self.assertEqual(person.get_person_name(), "Jonny Bravo")
        self.assertEqual(person.get_country(), "Arizona")
        self.assertEqual(person.get_city(), "Pheonix")
        self.assertEqual(person.get_street(), "Van Buren")
        self.assertEqual(person.get_number_of_the_house(), "14")
        self.assertEqual(person.get_events_id(), [])
        with self.assertRaises(repo_custom_exception):
            self.__person_controler.find_person_by_id("4")
            self.__person_controler.find_person_by_id("5")
            self.__person_controler.find_person_by_id("6")

    def test_update_person(self):
        self.__person_controler.update_person("3", "Jonny Bravo", "", "Pheonix", "Van Buren", "")
        updated_person = self.__person_controler.find_person_by_id("3")
        self.assertEqual(updated_person.get_person_id(), "3")
        self.assertEqual(updated_person.get_person_name(), "Jonny Bravo")
        self.assertEqual(updated_person.get_country(), "Arizona")
        self.assertEqual(updated_person.get_city(), "Pheonix")
        self.assertEqual(updated_person.get_street(), "Van Buren")
        self.assertEqual(updated_person.get_number_of_the_house(), "14")
        self.assertEqual(updated_person.get_events_id(), [])
        with self.assertRaises(repo_custom_exception):
            self.__person_controler.update_person("4", "Luka Modric", "", "Pheonix", "Van Buren", "")
        self.__person_controler.update_person("3", "", "", "", "", "")


    def test_add_event_to_person(self):
        self.__person_controler.add_event_to_person("3", "1")
        person = self.__person_controler.find_person_by_id("3")
        self.assertEqual(person.get_events_id(), ["1"])
        self.__person_controler.add_event_to_person("3", "2")
        person = self.__person_controler.find_person_by_id("3")
        self.assertEqual(person.get_events_id(), ["1", "2"])
        self.__person_controler.add_event_to_person("3", "3")
        person = self.__person_controler.find_person_by_id("3")
        self.assertEqual(person.get_events_id(), ["1", "2", "3"])
        with self.assertRaises(repo_custom_exception):
            self.__person_controler.add_event_to_person("3", "4")
            self.__person_controler.add_event_to_person("3", "5")
            self.__person_controler.add_event_to_person("3", "6")
            self.__person_controler.add_event_to_person("3", "7")

    def test_find_people_using_key_words(self):
        list_of_key_words = ["Jonny", "Marian"]
        generator = self.__person_controler.find_people_using_key_words(list_of_key_words)
        self.assertEqual(next(generator), self.__person_controler.find_person_by_id("3"))
        self.assertEqual(next(generator), self.__person_controler.find_person_by_id("12AB"))
        self.assertRaises(StopIteration, next, generator)

        list_of_key_words = []
        generator = self.__person_controler.find_people_using_key_words(list_of_key_words)
        self.assertRaises(StopIteration, next, generator)

        list_of_key_words = ["Niculae", "Romania"]
        generator = self.__person_controler.find_people_using_key_words(list_of_key_words)
        self.assertEqual(next(generator), self.__person_controler.find_person_by_id("1"))
        self.assertEqual(next(generator), self.__person_controler.find_person_by_id("12AB"))
        self.assertRaises(StopIteration, next, generator)
    


