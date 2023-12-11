import unittest
from DOMAIN.VALIDARI.validare_event import valid_event
from DOMAIN.person_event import person_event_class
from DOMAIN.event import event_class
from MY_CUSTOM_EXCEPTIONS.validation_exceptions import event_validation_exception
from MY_CUSTOM_EXCEPTIONS.validation_exceptions import invalid_date_character, invalid_day, invalid_month, invalid_year, multiple_dots_in_event_duration, invalid_event_duration_character, comma_not_supported_in_float_values, date_incomplete, vid_event_id_exception, vid_date_of_event, vid_duration_of_event, vid_description_of_event
from UTILS.generators import id_generator, date_generator, event_duration_generator, string_generator
import random
class test_validare_event(unittest.TestCase):
    def setUp(self) -> None:
        self.__shared_person_event_class = person_event_class()
        self.__event_validator = valid_event()

    def tearDown(self) -> None:
        self.__shared_person_event_class = None
        self.__event_validator = None

    def test_validare_event_for_add(self):
        event = event_class("6", "9/1/2023", "110", "Concertul lui Post Malone", self.__shared_person_event_class)
        self.__event_validator.event_validation(event)
        with self.assertRaises(event_validation_exception):
            event = event_class("", "12/2/2020", "60", "Concertul lui travis Scott", self.__shared_person_event_class)
            self.__event_validator.event_validation(event)
            event = event_class("7", "", "60", "Concertul lui travis Scott", self.__shared_person_event_class)
            self.__event_validator.event_validation(event)
            event = event_class("8", "12/2/2020", "", "Concertul lui travis Scott", self.__shared_person_event_class)
            self.__event_validator.event_validation(event)
            event = event_class("9", "29/2/2022", "60", "Concertul lui travis Scott", self.__shared_person_event_class)
            self.__event_validator.event_validation(event)
            event = event_class("10", "", "60", "Concertul lui travis Scott", self.__shared_person_event_class)
            self.__event_validator.event_validation(event)
            event = event_class("11", "", "", "")
            self.__event_validator.event_validation(event)

    def test_validare_event_for_update(self):
        event = event_class("6", "9/1/2023", "110", "Concertul lui Post Malone", self.__shared_person_event_class)
        self.__event_validator.event_validation_for_update(event)
        event = event_class("", "9/1/2023", "110", "Concertul lui Post Malone", self.__shared_person_event_class)
        with self.assertRaises(event_validation_exception):
            self.__event_validator.event_validation_for_update(event)

    def test_validare_event_id(self):
        event_id = ""
        with self.assertRaises(vid_event_id_exception):
            self.__event_validator.event_id_validation(event_id)

    def test_validare_event_date(self):
        event_date = "12/2/2020"
        self.__event_validator.event_date_validation(event_date, "ADD")

        event_date = "12.2:2020"
        self.__event_validator.event_date_validation(event_date, "ADD")

        self.assertRaises(invalid_day, self.__event_validator.event_date_validation, "29/2:2022", "ADD")
        self.assertRaises(invalid_day, self.__event_validator.event_date_validation, "32/5/2020", "ADD")
        self.assertRaises(invalid_month, self.__event_validator.event_date_validation, "12/13/2020", "ADD")
        self.assertRaises(invalid_month, self.__event_validator.event_date_validation, "12/0/2020", "ADD")
        self.assertRaises(invalid_year, self.__event_validator.event_date_validation, "12/5/0", "ADD")
        self.assertRaises(invalid_date_character, self.__event_validator.event_date_validation, "12/5/-1", "ADD")
        self.assertRaises(date_incomplete, self.__event_validator.event_date_validation, "12//2020", "ADD")
        self.assertRaises(date_incomplete, self.__event_validator.event_date_validation, "12/5/", "ADD")
        self.assertRaises(date_incomplete, self.__event_validator.event_date_validation, "/5/2020", "ADD")
        self.assertRaises(date_incomplete, self.__event_validator.event_date_validation, "12/5/2020/5", "ADD")
        self.assertRaises(invalid_date_character, self.__event_validator.event_date_validation, "12/5#/2020", "ADD")

    def test_validare_event_duration(self):
        event_duration = "60"
        self.__event_validator.event_duration_validation(event_duration, "ADD")

        event_duration = "60.5"
        self.__event_validator.event_duration_validation(event_duration, "ADD")

        self.assertRaises(multiple_dots_in_event_duration, self.__event_validator.event_duration_validation, "60.5.5", "ADD")
        self.assertRaises(invalid_event_duration_character, self.__event_validator.event_duration_validation, "60.5#", "ADD")
        self.assertRaises(comma_not_supported_in_float_values, self.__event_validator.event_duration_validation, "60,5", "ADD")

    def test_validare_event_with_random_generated_cases(self):
        random.seed(10)

        event = event_class(id_generator(), date_generator(), event_duration_generator(), string_generator(), self.__shared_person_event_class)
        self.assertRaises(event_validation_exception, self.__event_validator.event_validation, event)

        event = event_class(id_generator(), date_generator(), event_duration_generator(), string_generator(), self.__shared_person_event_class)
        self.assertRaises(event_validation_exception, self.__event_validator.event_validation, event)
        
        event = event_class(id_generator(), date_generator(), event_duration_generator(), string_generator(), self.__shared_person_event_class)
        self.__event_validator.event_validation(event)

        event = event_class(id_generator(), date_generator(), event_duration_generator(), string_generator(), self.__shared_person_event_class)
        self.assertRaises(event_validation_exception, self.__event_validator.event_validation, event)

        event = event_class(id_generator(), date_generator(), event_duration_generator(), string_generator(), self.__shared_person_event_class)
        self.__event_validator.event_validation(event)





