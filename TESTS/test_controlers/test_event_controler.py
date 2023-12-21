import unittest

from DOMAIN.VALIDARI.validare_event import valid_event
from DOMAIN.person_event import person_event_class
from DOMAIN.person import person_class
from REPOSITORIES.repo_evenimente import repo_events
from REPOSITORIES.repo_persoane import repo_people
from CONTROLLERS.event_controler import event_controler

from MY_CUSTOM_EXCEPTIONS.validation_exceptions import event_validation_exception
from MY_CUSTOM_EXCEPTIONS.repo_custom_exception import repo_custom_exception, dublicated_id_exception, inexistent_event_id_exception, person_added_twice_to_event

class test_event_controler(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.__event_repository = repo_events()
        cls.__people_repo = repo_people()
        cls.__event_validator = valid_event()
        cls.__shared_person_event_class = person_event_class()
        cls.__event_controler = event_controler(cls.__event_repository, cls.__event_validator, cls.__people_repo, cls.__shared_person_event_class)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.__event_repository = None
        cls.__people_repo = None
        cls.__event_validator = None
        cls.shared_person_event_class = None
        cls.__event_controler = None

    def setUp(self) -> None:
        self.__event_controler.add_event("1", "12/2/2020", "120", "Concertul lui travis Scott")
        self.__event_controler.add_event("2", "28/2/2022", "200", "Serbarea clasei a 3 - a")
        self.__event_controler.add_event("3", "12/2/2021", "300", "Balul Bobocilor")
        self.__people_repo.add_person_to_rep(person_class("1", "Popescu Niculae", "Rmania", "Tulcea", "Luminii", "122", self.__shared_person_event_class))
        self.__people_repo.add_person_to_rep(person_class("3", "Jonny Bravo", "Arizona", "Pheonix", "Van Buren", "14", self.__shared_person_event_class))

    def tearDown(self) -> None:
        events_ids = self.__event_repository.get_all_ids()
        for event_id in events_ids:
            self.__event_repository.delete_event(event_id)
        
        people_ids = self.__people_repo.get_all_ids()
        for person_id in people_ids:
            self.__people_repo.remove_person(person_id)
    
    def test_add_event(self):
        self.__event_controler.add_event("4", "14/1/2021", "80", "Meci de fotbal")
        with self.assertRaises((event_validation_exception, repo_custom_exception)):
            self.__event_controler.add_event("4", "12/2/2020", "60", "Concertul lui travis Scott")
            self.__event_controler.add_event("5", "12/2/2020", "", "Concertul lui travis Scott")
            self.__event_controler.add_event("6", "12/2/2020", "60", "")
            self.__event_controler.add_event("7", "29/2/2022", "60", "Concertul lui travis Scott")
            self.__event_controler.add_event("8", "", "60", "Concertul lui travis Scott")
            self.__event_controler.add_event("9", "", "", "")

    def test_remove_event(self): 
        self.__event_controler.remove_event("3")
        with self.assertRaises(inexistent_event_id_exception):
            self.__event_controler.remove_event("3")
            self.__event_controler.remove_event("4")
            self.__event_controler.remove_event("5")
            self.__event_controler.remove_event("6")
            self.__event_controler.remove_event("7")

    def test_find_event_by_id(self):
        event = self.__event_controler.find_event_by_id("3")
        self.assertEqual(event.get_event_id(), "3")
        self.assertEqual(event.get_event_date(), "12/2/2021")
        self.assertEqual(event.get_event_duration(), "300")
        self.assertEqual(event.get_event_description(), "Balul Bobocilor")
        with self.assertRaises(inexistent_event_id_exception):
            self.__event_controler.find_event_by_id("4")
            self.__event_controler.find_event_by_id("5")
            self.__event_controler.find_event_by_id("6")
            self.__event_controler.find_event_by_id("7")

    def test_update_event(self):
        self.__event_controler.update_event("3", "12/2/2021", "100", "Balul Bobocilor, clasa a 9 - a RA")
        updated_event = self.__event_controler.find_event_by_id("3")
        self.assertEqual(updated_event.get_event_id(), "3")
        self.assertEqual(updated_event.get_event_date(), "12/2/2021")
        self.assertEqual(updated_event.get_event_duration(), "100")
        self.assertEqual(updated_event.get_event_description(), "Balul Bobocilor, clasa a 9 - a RA")
        with self.assertRaises((event_validation_exception, repo_custom_exception)):
            self.__event_controler.update_event("3", "12/2/2021", "-11", "Balul Bobocilor")
            self.__event_controler.update_event("3", "12/13/2021", "300", "")
            self.__event_controler.update_event("3", "31/5/", "300", "Balul Bobocilor")
            self.__event_controler.update_event("3", "12/2/2021", "300", "Balul Bobocilor")

        self.__event_controler.update_event("3", "", "", "")

    def test_find_events_using_key_words(self):
        list_of_key_words = ["Travis", "bal"]
        generator = self.__event_controler.find_events_using_key_words(list_of_key_words)
        self.assertEqual(next(generator), self.__event_controler.find_event_by_id("1"))
        self.assertEqual(next(generator), self.__event_controler.find_event_by_id("3"))
        self.assertRaises(StopIteration, next, generator)

        list_of_key_words = []
        generator = self.__event_controler.find_events_using_key_words(list_of_key_words)
        self.assertRaises(StopIteration, next, generator)

        list_of_key_words = ["12/2/", "Scott"]
        generator = self.__event_controler.find_events_using_key_words(list_of_key_words)
        self.assertEqual(next(generator), self.__event_controler.find_event_by_id("1"))
        self.assertEqual(next(generator), self.__event_controler.find_event_by_id("3"))
        self.assertRaises(StopIteration, next, generator)

    def test_controler_add_person_to_event(self):
        person_id = "1"
        event_id = "1"
        self.__event_controler.controler_add_person_to_event(person_id, event_id)
        event = self.__event_controler.find_event_by_id(event_id)
        person = self.__people_repo.get_person_through_id(person_id)
        self.assertEqual(event_id, event.get_event_id())
        self.assertEqual(person_id, person.get_person_id())

        self.assertEqual(person.get_number_of_events_person_joined(), 1)
        self.assertEqual(event.get_number_of_people_joined_to_event(), 1)

        with self.assertRaises(person_added_twice_to_event):
            self.__event_controler.controler_add_person_to_event(person_id, event_id)

    def test_add_x_random_event(self):
        self.__event_controler.add_events_with_random_data(10)
        self.assertEqual(len(self.__event_controler), 13)



    






    


        
