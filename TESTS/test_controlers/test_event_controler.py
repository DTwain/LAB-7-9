import unittest

from DOMAIN.VALIDARI.validare_event import valid_event
from REPOSITORIES.repo_evenimente import repo_events
from CONTROLLERS.event_controler import event_controler

from MY_CUSTOM_EXCEPTIONS.validation_exceptions import event_validation_exception
from MY_CUSTOM_EXCEPTIONS.repo_custom_exception import repo_custom_exception, dublicated_id_exception, inexistent_id_exception

class test_event_controler(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.__event_repository = repo_events()
        cls.__event_validator = valid_event()
        cls.__event_controler = event_controler(cls.__event_repository, cls.__event_validator)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.__event_repository = None
        cls.__event_validator = None
        cls.__event_controler = None

    def setUp(self) -> None:
        self.__event_controler.add_event("1", "12/2/2020", "120", "Concertul lui travis Scott")
        self.__event_controler.add_event("2", "28/2/2022", "200", "Serbarea clasei a 3 - a")
        self.__event_controler.add_event("3", "12/2/2021", "300", "Balul Bobocilor")

    def tearDown(self) -> None:
        events_ids = self.__event_repository.get_all_ids()
        for event_id in events_ids:
            self.__event_repository.delete_event(event_id)
    
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
        with self.assertRaises(inexistent_id_exception):
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
        with self.assertRaises(inexistent_id_exception):
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

    def test_inc_number_of_people_joined_to_event(self):
        event_1 = self.__event_controler.find_event_by_id("1")
        event_1.inc_number_of_participants()
        self.assertEqual(event_1.get_number_of_people_joined(), 1)
        event_1.inc_number_of_participants()
        self.assertEqual(event_1.get_number_of_people_joined(), 2)



    






    


        
