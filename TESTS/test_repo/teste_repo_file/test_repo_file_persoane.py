import unittest
import shutil
from REPOSITORIES.repo_file_persoane import repo_file_people
from DOMAIN.person import person_class
from DOMAIN.person_event import person_event_class
from DOMAIN.DTO import DTO_for_second_report
class test_repo_file_people(unittest.TestCase):
    def setUp(self) -> None:
        shutil.copyfile("TESTS/test_repo/teste_repo_file/test_repo_file_people_backup.txt", "TESTS/test_repo/teste_repo_file/test_repo_file_people.txt")
        self.__repo = repo_file_people("TESTS/test_repo/teste_repo_file/test_repo_file_people.txt")

    def tearDown(self) -> None:
        for person_id in self.__repo.get_all_ids():
            self.__repo.remove_person(person_id)

    def test_load_from_file(self):
        self.assertEqual(len(self.__repo), 2)
        self.assertEqual(self.__repo.get_person_through_id("1").get_person_id(), "1")
        self.assertEqual(self.__repo.get_person_through_id("1").get_person_name(), "Marian")
        self.assertEqual(self.__repo.get_person_through_id("1").get_country(), "Romania")
        self.assertEqual(self.__repo.get_person_through_id("1").get_city(), "Bucuresti")
        self.assertEqual(self.__repo.get_person_through_id("1").get_street(), "Unirii")
        self.assertEqual(self.__repo.get_person_through_id("1").get_number_of_the_house(), "123")
        self.assertEqual(self.__repo.get_person_through_id("1").get_number_of_events_person_joined(), 2)

        self.assertEqual(self.__repo.get_person_through_id("2").get_person_id(), "2")
        self.assertEqual(self.__repo.get_person_through_id("2").get_person_name(), "Obreja David")
        self.assertEqual(self.__repo.get_person_through_id("2").get_country(), "Romania")
        self.assertEqual(self.__repo.get_person_through_id("2").get_city(), "Cluj Napoca")
        self.assertEqual(self.__repo.get_person_through_id("2").get_street(), "Aurel Vlaicu")
        self.assertEqual(self.__repo.get_person_through_id("2").get_number_of_the_house(), "12E")
        self.assertEqual(self.__repo.get_person_through_id("2").get_number_of_events_person_joined(), 0)    
    
    def test_store_to_file(self):
        with open("TESTS/test_repo/teste_repo_file/test_repo_file_people.txt", "r") as file:
            lines = file.readlines()
            self.assertEqual(len(lines), 2)
            self.assertEqual(lines[1], "2;Obreja David;Romania;Cluj Napoca;Aurel Vlaicu;12E")

        self.__repo.remove_person("1")
        with open("TESTS/test_repo/teste_repo_file/test_repo_file_people.txt", "r") as file:
            lines = file.readlines()
            self.assertEqual(len(lines), 1)
            self.assertEqual(lines[0], "2;Obreja David;Romania;Cluj Napoca;Aurel Vlaicu;12E")

    def test_add_person_to_rep(self):
        person = person_class("3", "Plaiu Rares", "Romania", "Botosani", "Veteranilor", "31C", self.__repo.get_shared_person_event_class())
        person.add_person_to_event("J3")
        person.add_person_to_event("V12")
        self.__repo.add_person_to_rep(person)

        self.assertEqual(len(self.__repo), 3)
        self.assertEqual(self.__repo.get_person_through_id("3").get_person_id(), "3")
        self.assertEqual(self.__repo.get_person_through_id("3").get_person_name(), "Plaiu Rares")
        self.assertEqual(self.__repo.get_person_through_id("3").get_country(), "Romania")
        self.assertEqual(self.__repo.get_person_through_id("3").get_city(), "Botosani")
        self.assertEqual(self.__repo.get_person_through_id("3").get_street(), "Veteranilor")
        self.assertEqual(self.__repo.get_person_through_id("3").get_number_of_the_house(), "31C")
        self.assertEqual(self.__repo.get_person_through_id("3").get_number_of_events_person_joined(), 2)

    def test_remove_person(self):
        self.__repo.remove_person("2")
        self.assertEqual(len(self.__repo), 1)

        self.assertRaises(Exception, self.__repo.remove_person, "2")

        self.__repo.remove_person("1")

        self.assertRaises(Exception, self.__repo.remove_person, "1")

    def test_update_person(self):
        new_person = person_class("2", "Obreja David", "Germania", "Berlin", "Fasanerieallee", "100B", self.__repo.get_shared_person_event_class())
        new_person.add_person_to_event("4")
        self.__repo.update_person(new_person, "2")

        self.assertEqual(len(self.__repo), 2)
        self.assertEqual(self.__repo.get_person_through_id("2").get_person_id(), "2")
        self.assertEqual(self.__repo.get_person_through_id("2").get_person_name(), "Obreja David")
        self.assertEqual(self.__repo.get_person_through_id("2").get_country(), "Germania")
        self.assertEqual(self.__repo.get_person_through_id("2").get_city(), "Berlin")
        self.assertEqual(self.__repo.get_person_through_id("2").get_street(), "Fasanerieallee")
        self.assertEqual(self.__repo.get_person_through_id("2").get_number_of_the_house(), "100B")
        self.assertEqual(self.__repo.get_person_through_id("2").get_number_of_events_person_joined(), 1)

    def test_get_person_through_id(self):
        person = self.__repo.get_person_through_id("1")
        self.assertIsInstance(person, person_class)
        self.assertEqual(self.__repo.get_person_through_id("1").get_person_id(), "1")
        self.assertEqual(self.__repo.get_person_through_id("1").get_person_name(), "Marian")
        self.assertEqual(self.__repo.get_person_through_id("1").get_country(), "Romania")
        self.assertEqual(self.__repo.get_person_through_id("1").get_city(), "Bucuresti")
        self.assertEqual(self.__repo.get_person_through_id("1").get_street(), "Unirii")
        self.assertEqual(self.__repo.get_person_through_id("1").get_number_of_the_house(), "123")
        self.assertEqual(self.__repo.get_person_through_id("1").get_number_of_events_person_joined(), 2)

    def test_get_list_of_DTO_objs(self):
        list_of_DTO_objects = self.__repo.get_list_of_DTO_objs()
        self.assertIsInstance(list_of_DTO_objects, list)
        self.assertEqual(len(list_of_DTO_objects), 2)

        self.assertIsInstance(list_of_DTO_objects[0], DTO_for_second_report)
        self.assertEqual(list_of_DTO_objects[0].get_number_of_events(), 2)
        self.assertEqual(list_of_DTO_objects[0].get_person_id(), '1')

        self.assertIsInstance(list_of_DTO_objects[1], DTO_for_second_report)
        self.assertEqual(list_of_DTO_objects[1].get_number_of_events(), 0)
        self.assertEqual(list_of_DTO_objects[1].get_person_id(), '2')

    def test_get_all(self):
        people_as_list = self.__repo.get_all()
        self.assertIsInstance(people_as_list, list)

        person_1 = person_class("1", "Marian", "Romania", "Bucuresti", "Unirii", "123", self.__repo.get_shared_person_event_class())
        self.assertIsInstance(people_as_list[0], person_class)
        self.assertEqual(people_as_list[0], person_1)

        person_2 = person_class("2", "Obreja David", "Romania", "Cluj Napoca", "Aurel Vlaicu", "12E", self.__repo.get_shared_person_event_class())
        self.assertIsInstance(people_as_list[1], person_class)
        self.assertEqual(people_as_list[1], person_2)

    def test_get_all_ids(self):
        ids = self.__repo.get_all_ids()
        self.assertIsInstance(ids, list)
        self.assertEqual(ids, ["1", "2"])

    def test_size(self):
        self.assertEqual(len(self.__repo), 2)

    def test_get_shared_person_event_class(self):
        self.assertIsInstance(self.__repo.get_shared_person_event_class(), person_event_class)




    
