import unittest

from DOMAIN.VALIDARI.validare_persoana import valid_person
from DOMAIN.person import person_class
from DOMAIN.person_event import person_event_class
from MY_CUSTOM_EXCEPTIONS.validation_exceptions import vid_person_id_exception, vid_name_exception, vid_country_exception, vid_city_exception, vid_street_exception, vid_house_number_exception
from MY_CUSTOM_EXCEPTIONS.validation_exceptions import person_validation_exception

from UTILS.generators import id_generator, string_generator, person_number_of_the_house_generator
import random
class test_validare_persoana(unittest.TestCase):
    def setUp(self) -> None:
            self.__shared_person_event_class = person_event_class()
            self.__event_validator = valid_person()
        
    def tearDown(self) -> None:
        self.__shared_person_event_class = None
        self.__valid_person = None

    def test_person_validation(self):
        person_1 = person_class("1", "John Doe", "USA", "New York", "Broadway", "123", self.__shared_person_event_class)
        self.__event_validator.person_validation(person_1)
        with self.assertRaises(person_validation_exception):
            person_2 = person_class("", "John Doe", "USA", "New York", "Broadway", "123", self.__shared_person_event_class)
            self.__event_validator.person_validation(person_2)
            person_3 = person_class("1", "", "USA", "New York", "Broadway", "123", self.__shared_person_event_class)
            self.__event_validator.person_validation(person_3)
            person_4 = person_class("1", "John Doe", "", "New York", "Broadway", "123", self.__shared_person_event_class)
            self.__event_validator.person_validation(person_4)
            person_5 = person_class("1", "John Doe", "USA", "", "Broadway", "123", self.__shared_person_event_class)
            self.__event_validator.person_validation(person_5)
            person_6 = person_class("1", "John Doe", "USA", "New York", "", "123", self.__shared_person_event_class)
            self.__event_validator.person_validation(person_6)
            person_7 = person_class("1", "John Doe", "USA", "New York", "Broadway", "", self.__shared_person_event_class)
            self.__event_validator.person_validation(person_7)

    def test_person_validation_for_update(self):
        person_1 = person_class("1", "John Doe", "", "New York", "", "123", self.__shared_person_event_class)
        self.__event_validator.person_validation_for_update(person_1)
        person_2 = person_class("", "Jane Smith", "UK", "London", "Baker Street", "221B", self.__shared_person_event_class)
        with self.assertRaises(person_validation_exception):
            self.__event_validator.person_validation_for_update(person_2)

    def test_person_id_validation(self):
        person_id = ""
        
        with self.assertRaises(vid_person_id_exception):
            self.__event_validator.person_id_validation(person_id)
            
    def test_person_name_validation(self):
        person_name = ""
        choosed_option_ADD_or_UPDATE = "ADD"
        
        with self.assertRaises(vid_name_exception):
            self.__event_validator.person_name_validation(person_name, choosed_option_ADD_or_UPDATE)
            
    def test_person_country_validation(self):
        person_country = ""
        choosed_option_ADD_or_UPDATE = "ADD"
        
        with self.assertRaises(vid_country_exception):
            self.__event_validator.person_country_validation(person_country, choosed_option_ADD_or_UPDATE)
            
    def test_person_city_validation(self):
        person_city = ""
        choosed_option_ADD_or_UPDATE = "ADD"
        
        with self.assertRaises(vid_city_exception):
            self.__event_validator.person_city_validation(person_city, choosed_option_ADD_or_UPDATE)
            
    def test_person_street_validation(self):
        person_street = ""
        choosed_option_ADD_or_UPDATE = "ADD"
        
        with self.assertRaises(vid_street_exception):
            self.__event_validator.person_street_validation(person_street, choosed_option_ADD_or_UPDATE)
            
    def test_person_house_number_validation(self):
        person_house_number = ""
        choosed_option_ADD_or_UPDATE = "ADD"
        
        with self.assertRaises(vid_house_number_exception):
            self.__event_validator.person_house_number_validation(person_house_number, choosed_option_ADD_or_UPDATE)

    def test_person_validation_with_random_generated_cases(self):
        random.seed(10)

        person = person_class(id_generator([]), string_generator(), string_generator(), string_generator(), string_generator(), person_number_of_the_house_generator(), self.__shared_person_event_class)
        self.assertRaises(person_validation_exception, self.__event_validator.person_validation, person)

        person = person_class(id_generator([8723]), string_generator(), string_generator(), string_generator(), string_generator(), person_number_of_the_house_generator(), self.__shared_person_event_class)
        self.__event_validator.person_validation(person)

        person = person_class(id_generator([8723, -8933]), string_generator(), string_generator(), string_generator(), string_generator(), person_number_of_the_house_generator(), self.__shared_person_event_class)
        self.__event_validator.person_validation(person)

        person = person_class(id_generator([8723, -8933, 4053]), string_generator(), string_generator(), string_generator(), string_generator(), person_number_of_the_house_generator(), self.__shared_person_event_class)
        self.assertRaises(person_validation_exception, self.__event_validator.person_validation, person)

        person = person_class(id_generator([8723, -8933, 4053, 5812]), string_generator(), string_generator(), string_generator(), string_generator(), person_number_of_the_house_generator(), self.__shared_person_event_class)
        self.assertRaises(person_validation_exception, self.__event_validator.person_validation, person)
