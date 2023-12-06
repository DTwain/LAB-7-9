import unittest

from DOMAIN.VALIDARI.validare_persoana import valid_person
from DOMAIN.person import person_class
from MY_CUSTOM_EXCEPTIONS.validation_exceptions import vid_person_id_exception, vid_name_exception, vid_country_exception, vid_city_exception, vid_street_exception, vid_house_number_exception
from MY_CUSTOM_EXCEPTIONS.validation_exceptions import person_validation_exception
class test_validare_persoana(unittest.TestCase):
    def test_person_validation(self):
        person_1 = person_class("1", "John Doe", "USA", "New York", "Broadway", "123")
        valid_person.person_validation(person_1)
        with self.assertRaises(person_validation_exception):
            person_2 = person_class("", "John Doe", "USA", "New York", "Broadway", "123")
            valid_person.person_validation(person_2)
            person_3 = person_class("1", "", "USA", "New York", "Broadway", "123")
            valid_person.person_validation(person_3)
            person_4 = person_class("1", "John Doe", "", "New York", "Broadway", "123")
            valid_person.person_validation(person_4)
            person_5 = person_class("1", "John Doe", "USA", "", "Broadway", "123")
            valid_person.person_validation(person_5)
            person_6 = person_class("1", "John Doe", "USA", "New York", "", "123")
            valid_person.person_validation(person_6)
            person_7 = person_class("1", "John Doe", "USA", "New York", "Broadway", "")
            valid_person.person_validation(person_7)

    def test_person_validation_for_update(self):
        person_1 = person_class("1", "John Doe", "", "New York", "", "123")
        valid_person.person_validation_for_update(person_1)
        person_2 = person_class("", "Jane Smith", "UK", "London", "Baker Street", "221B")
        with self.assertRaises(person_validation_exception):
            valid_person.person_validation_for_update(person_2)

    def test_person_id_validation(self):
        person_id = ""
        
        with self.assertRaises(vid_person_id_exception):
            valid_person.person_id_validation(person_id)
            
    def test_person_name_validation(self):
        person_name = ""
        choosed_option_ADD_or_UPDATE = "ADD"
        
        with self.assertRaises(vid_name_exception):
            valid_person.person_name_validation(person_name, choosed_option_ADD_or_UPDATE)
            
    def test_person_country_validation(self):
        person_country = ""
        choosed_option_ADD_or_UPDATE = "ADD"
        
        with self.assertRaises(vid_country_exception):
            valid_person.person_country_validation(person_country, choosed_option_ADD_or_UPDATE)
            
    def test_person_city_validation(self):
        person_city = ""
        choosed_option_ADD_or_UPDATE = "ADD"
        
        with self.assertRaises(vid_city_exception):
            valid_person.person_city_validation(person_city, choosed_option_ADD_or_UPDATE)
            
    def test_person_street_validation(self):
        person_street = ""
        choosed_option_ADD_or_UPDATE = "ADD"
        
        with self.assertRaises(vid_street_exception):
            valid_person.person_street_validation(person_street, choosed_option_ADD_or_UPDATE)
            
    def test_person_house_number_validation(self):
        person_house_number = ""
        choosed_option_ADD_or_UPDATE = "ADD"
        
        with self.assertRaises(vid_house_number_exception):
            valid_person.person_house_number_validation(person_house_number, choosed_option_ADD_or_UPDATE)
