import unittest
# from DOMAIN.person import person_class
# from DOMAIN.event import event_class
# from DOMAIN.DTO import DTO_for_second_report, DTO_for_third_report
# from REPOSITORIES.repo_persoane import repo_people
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
        self.__event_controler.remove_event("1")
        self.__event_controler.remove_event("2")
        self.__event_controler.remove_event("3")
    
    def test_add_event(self):
        self.__event_controler.add_event("4", "14/1/2021", "80", "Meci de fotbal")
        with self.assertRaises(event_validation_exception):
            self.__event_controler.add_event("5", "12/2/2020", "", "Concertul lui travis Scott")
            self.__event_controler.add_event("6", "12/2/2020", "60", "")
            self.__event_controler.add_event("7", "29/2/2022", "60", "Concertul lui travis Scott")
            self.__event_controler.add_event("8", "", "60", "Concertul lui travis Scott")
            self.__event_controler.add_event("9", "", "", "")
        self.__event_controler.remove_event("4")

    def test_remove_event(self): 
        self.__event_controler.remove_event("3")
        with self.assertRaises(inexistent_id_exception):
            self.__event_controler.remove_event("3")
            self.__event_controler.remove_event("4")
            self.__event_controler.remove_event("5")
            self.__event_controler.remove_event("6")
            self.__event_controler.remove_event("7")
            self.__event_controler.remove_event("8")
            self.__event_controler.remove_event("9")
        
