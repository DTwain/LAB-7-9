import unittest

from DOMAIN.person import person_class
from DOMAIN.DTO import DTO_for_second_report
from REPOSITORIES.repo_persoane import repo_people
from MY_CUSTOM_EXCEPTIONS.repo_custom_exception import dublicated_id_exception, inexistent_id_exception

class test_repo_people(unittest.TestCase):
    def setUp(self):
        self.__repo = repo_people()

    def tearDown(self):
        self.__repo = None

    def test_add_person(self):
        person1 = person_class("1", "John Doe", "USA", "New York", "Broadway", "12")
        person2 = person_class("1", "Jane Smith", "UK", "London", "Baker Street", "221B")
        self.__repo.add_person_to_rep(person1)
        with self.assertRaises(dublicated_id_exception):
            self.__repo.add_person_to_rep(person2)

    def test_remove_person(self):
        person = person_class("1", "John Doe", "USA", "New York", "Broadway", "12")
        self.__repo.add_person_to_rep(person)
        removed_person = self.__repo.remove_person("1")
        self.assertEqual(removed_person, person)
        self.assertEqual(self.__repo.size(), 0)
        self.assertEqual(self.__repo.get_all(), [])
        with self.assertRaises(inexistent_id_exception):
            self.__repo.remove_person("1")

    def test_update_person(self):
        person = person_class("1", "John Doe", "USA", "New York", "Broadway", "12")
        updated_person = person_class("2", "Jane Smith", "UK", "London", "Baker Street", "221B")
        self.__repo.add_person_to_rep(person)
        preupdate_person = self.__repo.update_person(updated_person, "1")
        self.assertEqual(preupdate_person, person)
        self.assertEqual(self.__repo.get_person_through_id("1"), updated_person)

    def test_update_person_inexistent_id(self):
        updated_person = person_class("1", "Jane Smith", "UK", "London", "Baker Street", "221B")
        with self.assertRaises(inexistent_id_exception):
            self.__repo.update_person(updated_person, "1")

    def test_get_person_through_id(self):
        person = person_class("1", "John Doe", "USA", "New York", "Broadway", "12")
        self.__repo.add_person_to_rep(person)
        retrieved_person = self.__repo.get_person_through_id("1")
        self.assertEqual(retrieved_person, person)

    def test_get_person_through_id_inexistent_id(self):
        with self.assertRaises(inexistent_id_exception):
            self.__repo.get_person_through_id("1")

    def test_get_list_of_DTO_objs(self):
        person1 = person_class("1", "John Doe", "USA", "New York", "Broadway", "12")
        person2 = person_class("2", "Jane Smith", "UK", "London", "Baker Street", "221B")
        self.__repo.add_person_to_rep(person1)
        self.__repo.add_person_to_rep(person2)
        DTO1 = DTO_for_second_report("1", 0)
        DTO2 = DTO_for_second_report("2", 0)
        expected_list = [DTO1, DTO2]
        self.assertEqual(self.__repo.get_list_of_DTO_objs(), expected_list)

    def test_get_all(self):
        person1 = person_class("1", "John Doe", "USA", "New York", "Broadway", "12")
        person2 = person_class("2", "Jane Smith", "UK", "London", "Baker Street", "221B")
        self.__repo.add_person_to_rep(person1)
        self.__repo.add_person_to_rep(person2)
        self.assertEqual(self.__repo.get_all(), [person1, person2])

    def test_get_all_ids(self):
        person1 = person_class("1", "John Doe", "USA", "New York", "Broadway", "12")
        person2 = person_class("2", "Jane Smith", "UK", "London", "Baker Street", "221B")
        self.__repo.add_person_to_rep(person1)
        self.__repo.add_person_to_rep(person2)
        self.assertEqual(self.__repo.get_all_ids(), ["1", "2"])

    def test_size(self):
        person1 = person_class("1", "John Doe", "USA", "New York", "Broadway", "12")
        person2 = person_class("2", "Jane Smith", "UK", "London", "Baker Street", "221B")
        self.__repo.add_person_to_rep(person1)
        self.__repo.add_person_to_rep(person2)
        self.assertEqual(self.__repo.size(), 2)

