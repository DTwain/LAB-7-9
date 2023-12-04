import unittest
from DOMAIN.DTO import DTO_for_second_report
from DOMAIN.DTO import DTO_for_third_report

class test_DTO_classes(unittest.TestCase):
    def setUp(self) -> None:
        self.DTO_1 = DTO_for_second_report("1", 3)
        self.DTO_2 = DTO_for_third_report("2", 5)

    def tearDown(self) -> None:
        self.DTO_1 = None
        self.DTO_2 = None

    def test_getters(self):
        self.assertEqual(self.DTO_1.get_person_id(), "1")
        self.assertEqual(self.DTO_1.get_number_of_events(), 3)
        self.assertEqual(self.DTO_2.get_event_id(), "2")
        self.assertEqual(self.DTO_2.get_number_of_people(), 5)

    def test_str(self):
        self.assertEqual(str(self.DTO_2), "2 | 5")